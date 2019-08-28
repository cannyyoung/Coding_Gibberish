# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#use_save_as_before_starting_the_code
#problem found from: http://codingdojang.com/scode/409?answer_mode=hide
#https://en.wikipedia.org/wiki/Collatz_conjecture
# given two numbers a and b. find the maximum number of cycles of a sequence that is given
# from a number between a and b, where the sequence pattern is:
# the number following a number n, is 3n+1 if odd, and is n//2 if even
#LOGIC:
# Make a list and append the appropriate number using a for/while loop 'till one
# and save the size of the list if the number is bigger than the previous one.
# repeat the process for all numbers between a and b
#
#my_solution:
Ex_inp = (input('enter two Numbers only: \n')).split(' ')
def make_seq(se): #making the sequence
    colla = [se] #starting number = first number in the collatz sequence
    while colla[-1] != 1:
        if(colla[-1]%2):
            colla.append(3*colla[-1] + 1)
        else:
            colla.append(colla[-1]/2)
    return(len(colla))
ans = 0
for num in range(int(Ex_inp[0]),int(Ex_inp[1])+1): #repeating the process
    ans = make_seq(num) if make_seq(num) > ans else ans
print(ans)
#other_solution:
# you didn't even need to save it in a sequence. and this did exactly that
def cypro(k):
    cl=1
    while k != 1:
        if k%2==0:
            k=k/2
            cl+=1
        else:
            k=3*k+1
            cl+=1
    return cl

i=int(input('INPUT MIN NUM : '))
j=int(input('INPUT MAX NUM : '))
#t=0 this doesn't need to exist
#arw=[] if you're going for efficiency, even this is inefficient
ans = 0
for t in range(i,j+1):
    ans = cypro(t) if cypro(t)>ans else ans
print(ans)