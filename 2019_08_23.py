# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: https://projecteuler.net/problem=59
#make code that decodes the ASCII code of text file p059_cipher.txt, and finds the sum of
#the decoded ASCII values.
#The code is encoded using xor and cyclic use of three lower case characters.
#See the text file for better understanding

#my solution
#It took me a while to get this problem going,
alph = 'abcdefghijklmnopqrstuvwxyz'
sol = []
for c1 in alph:
    for c2 in alph:
        for c3 in alph:
            key= c1+c2+c3
            sol.append(key) #finding all the possible keys
sol_d = {}.fromkeys(sol,0) #making a dict with all the keys and associated count value
prob = open('p059_cipher.txt')
code = []
ans = {}.fromkeys(sol,None) #making a dict with keys and deciphered text + sum
for line in prob:
    code = line.split(',')
for key in sol_d:
    decipher = []
    SUM = 0
    for i in range(len(code)):
        ASC = int(code[i]) ^ ord(key[i%3])
        decipher.append(chr(ASC))
        SUM += ASC
    solu = ''.join(decipher)
    sol_d[key] = solu.count('the') #counting 'and' did not work somehow
    ans[key] = (solu,SUM)
h_val = sorted(sol_d.values())[-1]
the_code = [k for (k,v) in sol_d.items() if v == h_val][0]
print(ans[the_code])
#another solution of this found online: credit to whoever made this solution.''

def main():
    with open("p059_cipher.txt", 'r') as f:
        encrypt = f.read()
    encrypt = tuple(map(int, encrypt.split(','))) #Why did I never think about doing this?

    # 소문자 ascii: [97,122]
    lower_range = range(97, 123)
    keys = [(p, m, s) for p in lower_range for m in lower_range for s in lower_range] #good approach
    # 공백이 제일 많이 검출되는 (영어 문장이라 판단되는) 키에 대한 메세지
    max_spaces, decrypt_key, decrypt_msg = 0, None, None  # 최대 공백수, 암호화키, 해독 문자열
    for key in keys:
        tmp_decrypt = tuple(e ^ key[idx % 3] for idx, e in enumerate(encrypt)) #enumerate is used instead of a for loop
        foo = tmp_decrypt.count(32)  # counting blanks
        if foo > max_spaces: #checks just the no.blanks and saves only the maximum one. Nice one there
            max_spaces = foo
            decrypt_key = key
            decrypt_msg = tmp_decrypt[:]

    print("encryption key:", "".join(chr(c) for c in decrypt_key))  # god
    print("decrypted message:", "".join(chr(c) for c in decrypt_msg))  # (The Gospel..)
    print("sum of ascii values in decrypted message: ", sum(decrypt_msg))  # 107359


if __name__ == "__main__":
    main()
'