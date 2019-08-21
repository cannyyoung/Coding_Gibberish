# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: http://codingdojang.com/scode/465?answer_mode=hide
#make a program that re-interprets a string as following:
#aaabbcccccca--> a3b2c6a1
#in other words, a string compressor XD
#my solution
THE_STRING = input('enter any string: \n')
counter = 0
ANS = []
for Char in THE_STRING:
    if ANS == []: # if it's the start of the string
        ANS.append(Char)
        counter+= 1
    elif ANS[-1] == Char: #if the next char == the previous one
        counter+= 1
    else: #if not, then it must be a new character
        ANS.append(str(counter))
        counter = 1
        ANS.append(Char)
ANS.append(str(counter))
print(''.join(ANS))

#shortest or just a different solution of this found online: credit to whoever made this solution.
#this one is basically the same as mine.
S = input('enter any string: \n')
result = S[0]
count = 0

for St in S:
    if St == result[-1]:
        count+=1
    else:
        result += str(count) + St
        count = 1
result+= str(count)

print(result)