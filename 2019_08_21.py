# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: http://codingdojang.com/scode/539?answer_mode=hide
#Make a program that finds all perfect numbers under a given number: a perfect number is a number where 
#the sum of its factors excluding itself would equal the number
#EX) 6= 1+2+3 (its factors) hence 6 is a perfect number
#my solution
num = int(input('enter one number: \n'))
Perfect_NUM = []
for NUM in range(1,num+1):
    Factors = []
    for Number in range(1,NUM//2+1):
        if NUM % Number == 0:
            Factors.append(Number)
    if sum(Factors) == NUM: 
        Perfect_NUM.append(NUM)
print(Perfect_NUM)

#shortest or just a different solution of this found online: credit to whoever made this solution.
#I_NEVER_KNEW_COMPREHENSION_COULD_BE_THIS_POWERFUL.py XD
#come to think of it, yeah, you should be able to use sum on just a generator
num = int(input('enter one number: \n'))
print([x for x in range(1,num+1) if x==sum(y for y in range(1,x//2+1) if x%y == 0)])