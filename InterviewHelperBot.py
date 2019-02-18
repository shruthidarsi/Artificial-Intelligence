# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    Created by Shruthi Madishetty on 02/17/2019
    """

import re
import random

rulesList =[
            { r'(.*?)hi (.*)':
            ["Hi there. Tell me how can I help you for Interview Process."] },
            { r'(.*)\s?find a job\s?(.*)' :
            ["You can get open jobs in glassdoor.com, dice.com, linkedin.com..etc",
             "You can get latest jobs from any of the job portals in internet"] },
            { r'(.*)\s?should i\s?(.*)' :
            ["You can always do {1}",
             "Well, it's a personal choice"] } ,
            { r'(.*)\s?dream\s?(.*)' :
            ["Really-- {1}?",
             "What does this dream suggest to you?",
             "You can always build your profile to get your dream job" ] },
            { r'(.*)\s?search\s?(.*)' :
            [ "You can always search for Jobs in linkedin.com or dice.com or any other portals similar to it",
             "Do you often search relevant jobs and then apply?"] },
            { r'(.*)\s?need help\s?(.*)' :
            ["I can always help for {1} ",
             "Why do you want {1}",
             "Explain more about {1}" ] },
            { r'(.*) I am glad (.*)' :
            ["How have I helped you to be {1}",
             "What makes you happy just now",
             "Can you explain why you are suddenly {1}" ]},
            { r'(.*)\s?details\s?(.*)' :
            ["You should always keep your {0} details seperately as per resume standards",
             "Keep work on resume with {0} details" ] },
            { r'(.*)\s?yes\s?(.*)' :
            ["You seem quite positive",
             "Are you sure?" ,
             "I understand"] },
            { r'(.*)\s?no\s?(.*)' :
            ["Why not?",
             "You are being a bit negative" ,
             "Are you saying \"NO\" just to be negative?"] },
            { r'(.*) perhaps(.*)' :
            ["You do not seem quite certain" ,
             "You should always be certain to put things on resume while interview processing"] },
            { r'(.*?)\s?help\s?(.*)': ["I can always give suggestions for your interview process.."] },
            {r'(.*)include\s?(.*)':
            ["Some essential things to include {1} are : Personal Details, Education History, Work Experience,"
             "Skills and achievements"]},
            { r'(.*)' : ["Very interesting",
                         "I am not sure I understand you fully",
                         "Please continue"] }
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
    print("\nErica: You are connected with Erica....");
    
    while True :
        stmt = input("Me: ")
        if(stmt == "quit" or stmt=="exit") :
            print("\nErica: Bye.. Meet you another time...")
            break;
        print("\nErica: {}".format(process_response(stmt)))





