# make a code that finds numbers that don't have any generator, known as a self number. Find all self-numbers below 5000
# The number that is sum of its digits and its numbers are important.
# http://codingdojang.com/scode/365?answer_mode=hide
#my code
set_1 = set(list(range(5000)))
L_1 = [str(x) for x in range(5000)]
L_2 = []
print('hello')
for num  in L_1:
    number = 0
    for i in range(len(num)):
        number += int(num[i])
    number += int(num)
    L_2.append(number)
print(sorted(set_1 - set(L_2)))

#shortest code/ master of comprehension :O
print(sorted(set(range(1,5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1,5000)}))