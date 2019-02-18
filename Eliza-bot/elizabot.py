# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    Created by Shruthi Madishetty on 01/02/2019
"""

import re
import random

rulesList =[
            { r'(.*?)hi (.*)': ["Hi there. Please state your problem."] },
            { r'(.*) name (.*)' :
            ["Great, good to know that.",
             "I am not interested in names"] } ,
            { r'(.*) sorry (.*)' :
            ["Please don't apologize.",
             "Apologies are not necessary.",
             "What feelings do you have when you apologize?"
             ] } ,
            { r'(.*) I remember (.*)' :
            ["Do you often think of {1} ?",
             "Does thinking of {1} bring anything else to mind ?",
             "What else do you remember?",
             "Why do you recall {0} right now?",
             "{1} if {0}",
             "Do you really think it is likely that {0}?",
             "Do you wish that {0}?",
             "What do you think about {0}?",
             "Really-- if {0}?" ] } ,
            { r'(.*) dream (.*)' :
            ["Really-- {0}?",
             "What does this dream suggest to you?",
             "Do you dream often?"
             "Have you dreamt {1} before?",
             "{0} dream about {1}?",
             "How do you feel about {1} in reality?" ] },
            { r'(.*)\s?my mother(.*)' :
            [ "Who else in your family {1}?",
             "Tell me more about your family." ] },
            { r'(.*)\s?my father\s?(.*)' :
            ["{0}my father {1}",
             "Your father?",
             "Does he influence you strongly?",
             "What else comes to mind when you think of your father?"] },
            { r'(.*) I want (.*)' :
            ["What would it mean for you if you got {1}",
             "Why do you want {1}",
             "Suppose you got {1} soon"
             ] },
            { r'(.*) I am glad (.*)' :
            ["How have I helped you to be {1}",
             "What makes you happy just now",
             "Can you explain why you are suddenly {1}" ]},
            { r'(.*) I am sad (.*)' :
            ["I am sorry to hear you are depressed",
             "I am sure it’s not pleasant to be sad" ,
             "{0} are like {1}",
             "What resemblance do you see between {0} and {1}"] },
            { r'(.*) is like (.*)' :
            ["In what way is it that {0} is like {1}",
             "What resemblance do you see?" ,
             "Could there really be some connection?"] },
            { r'(.*) alike(.*)' :
            ["In what way?",
             "What similarities are there?"] },
            { r'(.*)same(.*)' :
            ["What other connections do you see?"] },
            { r'(.*) I was (.*)' :
            ["Were you really?",
             "Why do you tell me you were {1} now?" ] },
            { r'(.*)I am(.*)' :
            ["In what way are you {1}",
             "Do you want to be{1}?" ] },
            { r'(.*) am I (.*)' :
            ["Do you believe you are {1}",
             "Would you want to be {1}" ,
             "You wish I would tell you you are {1}",
             "What would it mean if you were {1}"] },
            { r'(.*)\s?you are (.*)' :
            ["What makes you think I am {1}?"] },
            { r'(.*) because (.*)' :
            ["Is that the real reason?",
             "What other reasons might there be?" ,
             "Does that reason seem to explain anything else?"] },
            { r'(.*)were you(.*)' :
            ["Perhaps I was %Y",
             "What do you think?" ,
             "What if I had been %Y"] },
            { r'(.*) I can\'t (.*)' :
            ["Maybe you could {1} now",
             "What if you could {1}?" ] },
            { r'(.*) I feel (.*)' :
            ["Do you often feel {1}?"] },
            { r'(.*)I felt(.*)' :
            ["What other feelings do you have?"] },
            { r'(.*)why don\'t you (.*)' :
            ["Should you {1} yourself?",
             "Do you believe I don't {1}" ,
             "Perhaps I will {1} in good time"] },
            { r'(.*) yes (.*)' :
            ["You seem quite positive",
             "Are you sure?" ,
             "I understand"] },
            { r'(.*) no (.*)' :
            ["Why not?",
             "You are being a bit negative" ,
             "Are you saying \"NO\" just to be negative?"] },
            { r'(.*) someone (.*)' :
            ["Can you be more specific?"] },
            { r'(.*) everyone (.*)' :
            ["Can you think of anyone in particular?",
             "Who for example?"] },
            { r'(.*)\s?always(.*)' :
            ["Can you think of a specific example?",
             "What incident are you thinking of?" ,
             "Really—always"] },
            { r'(.*) perhaps(.*)' :
            ["You do not seem quite certain" ] },
            { r'(.*) are (.*)' :
            ["Did you think they might not be {1}?",
             "Possibly they are {1}" ] },
            { r'(.*?)\s?help\s?(.*)': ["What would it mean to you if you got some help"] },
            { r'(.*)' : ["Very interesting",
                         "I am not sure I understand you fully",
                         "Please continue",
                         "Do you feel strongly about discussing such things?",
                         "Why do you say that?"] }
            ]

pronouns_map = {
    "you":"I" ,
        "i":"you",
        "me":"you",
        "me.":"you.",
        "your":"my" ,
        "my":"your" ,
        "are": "am",
        "well" : "",
        "in that case": ""
}
prefixes = ["you", "will you", "can you"]

def process_response(stmt):
    """ Try to find the keyword and get the set of possible replies"""
    """print(stmt)"""
    
    foundKey = ""
    full_resp = ""
    
    for rule in rulesList :
        for keyword, definitions in rule.items() :
            foundKey = re.match(keyword, stmt, re.I)
            if foundKey:
                resp = random.choice(definitions)
                if len(re.findall(r'[^{]*[^}]', resp)) >= 2:
                    """full_resp = process_subject_to_object(stmt)"""
                    full_resp = resp.format(foundKey.group(1), process_subject_to_object(foundKey.group(2)) )
                else:
                    full_resp = resp
                if resp == "":
                    full_resp =  process_subject_to_object(stmt)
                    if stmt.lower().startswith(tuple(prefixes)):
                        full_resp = "Why do you think {}".format(full_resp)
                        return full_resp
                return full_resp


def process_subject_to_object(obj) :
    return ' '.join([pronouns_map.get(word, word) for word in obj.lower().split()])


if __name__ == '__main__':
    print("\nEliza: You are connected with Eliza....");
    
    while True :
        stmt = input("Me: ")
        if(stmt == "quit" or stmt=="exit") :
            print("\nEliza: Bye.. Meet you another time...")
            break;
        print("\nEliza: {}".format(process_response(stmt)))




