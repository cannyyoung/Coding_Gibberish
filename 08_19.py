# find the number of times a number appears in any digit from 1~1000. (how many times does 1's appear? 2's? 3's?
# http://codingdojang.com/scode/504?answer_mode=hide
#my code
all_num = [str(num) for num in range(1,1001)]
all_digit = '0123456789'
ans = [0]*10
for num in all_num:
    for digit in all_digit:
        ans[int(digit)] += num.count(digit)
print(ans)

#shortest answers found: (quite close this time)
count = { x:0 for x in range(0,10)}
for x in range(1,1001):
    for i in str(x):
        count[int(i)]+=1
print(sorted(count.items()))

#sol.no.2
from collections import defaultdict

d = defaultdict(int)
for n in range(1,1001):
    for x in str(n):
        d[x]+=1
print(d)