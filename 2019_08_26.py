# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: http://codingdojang.com/scode/488?answer_mode=hide

#make a code that tests if all characters of '0123456789'exists once in a given
#input of int strings
# plan: just compare the sorted() output of the input with sorted('0123456789')
#my_solution:
Ex_inp = (input('enter Numbers only: \n')).split(' ')
#Ex_inp = '0123456789 01234 01234567890 6789012345 012322456789'.split(' ')
# testing the inputs given in the problem, it works!
for S in Ex_inp:
    print(sorted(S) == sorted('0123456789'))
#other solutions
n = [''.join(sorted(x)) for x in input().split(' ')]
for x in n:
    print(True if x=='0123456789' else 'false') 