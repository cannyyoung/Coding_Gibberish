# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: http://codingdojang.com/scode/266?answer_mode=hide
# create an m*n array that is spiral clockwise like this:
# 6 6
#
#  0   1   2   3   4   5
# 19  20  21  22  23   6
# 18  31  32  33  24   7
# 17  30  35  34  25   8
# 16  29  28  27  26   9
# 15  14  13  12  11  10
#my solution
def spiral(row, col):
    arr = [[None]*col for a in range(row)]
    counter,c,r,dc,dr = 0,0,0,1,0
    while counter < (row*col):
        arr[r][c] = counter
        counter += 1
#        print(r,c,dr,dc, counter) test blocks
        c, r = c+dc,r+dr
        if(c == col or r == row or c*r < 0 or arr[r][c] != None):
#            print('why')
            c,r = c - dc, r-dr
            dc,dr = -dr,dc
            c,r = c+dc, r+dr
    return arr
ROW, COL = input('enter two numbers, separated by a space: \n').split(' ')
for a  in spiral(int(ROW),int(COL)):
    print(a)
#shortest solution of this found online: credit to whoever made this solution.
X,Y = map(int,input().split(' '))
lis = [[-1 for i in range(Y)] for j in range(X)]
x,y = 0,0
dx,dy = 0,1
count = 0
while lis[x][y] == -1:
    lis[x][y] = count
    count+=1
    x,y = x+dx,y+dy
    if x in [-1,X] or y in [-1,Y] or lis[x][y] != -1:
        x,y = x-dx,y-dy
        dx,dy = dy,-dx
        x,y = x+dx,y+dy
for L in lis:
    print(L)