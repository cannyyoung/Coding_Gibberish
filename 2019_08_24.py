# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: http://codingdojang.com/scode/661?answer_mode=hide
#Goldbach's conjecture says any even number bigger than 2 can be represented as
#the sum of two prime numbers. (where the two numbers can be the same number)
#check wiki for details: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
#make a program that shows all possible prime number pairs fulfilling these conditions

#my solution
prob = int(input('please give me an even number bigger than 2: \n')) #getting input
not_prime = [] #this is collection of non-prime numbers
for num in range(2,prob): # for all numbers that might be prime
    all_n = range(2,num) 
    for n in all_n: 
        if num % n == 0: not_prime.append(num); break;
prime = sorted(set(range(2,prob)) - set(not_prime))
sol = [(num1,num2) for num1 in prime for num2 in prime if num1 + num2 == prob and num1<=num2]
#the ifs allow filtering of repeats and gets two primes whose sum equals 'n'.
print(sol) 

#shortest solution of this found online: credit to whoever made this solution.'''
def check_prime(num): #function checking if a number is prime
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True 

answer = []
n = int(input())
if n >= 4 and n % 2 == 0 : #the minimum of two sums of prime must be greater than 4, seems minor
    for i in range(2, int(n/2) + 1): #only going through half the numbers, nice
        if check_prime(i) and check_prime(n - i) : #checking the number and its difference, nice idea
            answer += [[i, n - i]]
print(answer)

#another I like this one, it has two new ideas:
def get_primes(n: int):
    primelst = []
    pool = list(range(2, n + 1))
    while pool: #will escape once no prime remain in the pool, nice idea, I like it.
        newprime = pool[0] #adds 2 to the new prime list
        primelst.append(newprime)
        pool = [x for x in pool if x % newprime != 0] #checks each object in iterable and pops non-prime
    return primelst


def main():
    n = int(input('n=? '))
    if n % 2 != 0 or n <= 2: return
    primes = get_primes(n)
    rst_set = set((min(prime, n - prime), max(prime, n - prime)) for prime in primes if (n - prime) in primes)
    #ok so they get all sets of prime and n-prime if n-prime is also a prime, seems like I'm the only one
    #that just stupidly added all the primes together that gets n, lol
    print(sorted(rst_set))


if __name__ == "__main__":
    main()
