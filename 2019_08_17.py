# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: http://codingdojang.com/scode/350#answer-filter-area
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#my solution
SUM = 0
for num in range(1000):
    if num%3 == 0:
        SUM += num
    elif num%5 == 0:
        SUM += num
print(SUM)

#shortest solution of this found online:
print(sum(list([num for num in range(1000) if num%3 == 0 or num % 5 == 0])))

#another one that I actually like:
set_3 = set(range(3,1000,3))
set_5 = set(range(5,1000,5))
print(sum(set_3 | set_5))