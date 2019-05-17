#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:54:34 2019
@author: pavanshru
"""
import numpy 


"""def operation(distArr , i, j, s1Char, s2Char):
    opcost = 0
    if s1Char[i-1] == s2Char[j-1] :
        opcost = 0
    else:
        print("sub")
        opcost = 2
        
    insertioncost = distArr[i-1, j] + 1
    deletioncost = distArr[i, j-1] + 1
    subscost = distArr[i-1, j-1] + opcost
    lowcost = min(insertioncost, deletioncost, subscost)
    return lowcost"""
    

def editDistance(s1, s2, s3) :
    """Source - Human Species """
    m1 = len(s1)
    """Destination - Mice Species """
    m2= len(s2)
    distArr = numpy.zeros((m1+1, m2+1))
    
    for i in range(1, m1+1):
        distArr[i, 0] = i
    for j in range(1, m2+1):
        distArr[0, j] = j
        
    for i in range(1, m1+1):
        for j in range(1, m2+1):
            if s1[i-1] == s2[j-1]:
                distArr[i, j] = distArr[i-1, j-1]                
            else :
                insertioncost = distArr[i-1, j] + 1
                deletioncost = distArr[i, j-1] + 1
                subscost = distArr[i-1, j-1] + 2
                distArr[i,j] = min(insertioncost, deletioncost, subscost)
    return distArr
            
def printTrace(s1, s2, distArr):
    s4 = ""
    s5 = ""
    i = len(s1)
    j = len(s2)
    
    while i>0 or j>0:
        if (distArr[i,j] == distArr[i-1, j-1]) :
            s4 += (s1[i-1])
            s5 += (s2[j-1])
            i -= 1
            j -=1
        elif (distArr[i, j-1]+1 <= distArr[i,j]):
            s4 += ("-")
            s5 += s2[j-1] 
            j -= 1
        elif (distArr[i-1, j]+1 <= distArr[i,j]):
            s4 += (s1[i-1])
            s5 += ("-")
            i -= 1
        elif (distArr[i,j] == distArr[i-1, j-1]+2) :
            s4 += (s1[i-1])
            s5 += (s2[j-1])
            i -= 1
            j -= 1
    with open('alignment.txt', 'w+') as resultfile:
        resultfile.truncate(0)
        resultfile.write(s4[::-1])
        resultfile.write("\n\n")
        resultfile.write(s5[::-1])
        
    
if __name__ == '__main__':
    print("\nEdit Distance for Human and Mice Species DNA")
    percentage = input("Please provide % to compare\n")
    with open('human.txt', 'r') as file:
        s1 = file.read().replace('\n', '')
    with open('mice.txt', 'r') as file:
        s2 = file.read().replace('\n', '')
    
    s3 = ""
    s1_len = int((len(s1) * int(percentage))/100)
    s2_len = int((len(s1) * int(percentage))/100)
    distArr = numpy.zeros((s1_len+1 , s2_len+1 ))
    distArr = editDistance(s1, s2,s3)
    printTrace(s1,s2, distArr)