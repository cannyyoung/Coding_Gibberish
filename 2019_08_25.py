# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:11:04 2019

@author: Wooyoung Cho
"""
#problem found from: https://www.careercup.com/question?id=15422849
#problem is complicated, but put simply, the players pick a pot with gold from either end
#of the line of pots and the player with most gold at the end is the winner. And you must
#make an algorithm where player that goes 1st wins the most gold, where B plays optimally as well
#thinking about the game, the involved 'pots' in the game in making a decision is really the 
#2 pots on each end of the line of pots.
#So the optimal decision would be to choose a pot in which (my_choice) - (opponent_best_choice) 
#is the maximum.
#of course, based on the number of gold arrangement, there may be a situation that the player would
#be half forced to lose, though.
#I have an ideas to solve this:
#
#have a function that gets all possibilities, test every single possibility and
#select ones with win or loss
#and repeat that process?

# I tried for hours, but I couldn't get it to work somehow. I threw in a blank towel and will comeback to this
#problem someday. For now, someone else's solution
# I learned that I need to come up with a definite, clear plan before jumping in
import random
import math
pots = list(math.ceil(random.random()*10) for a in range(math.ceil(random.random() * 20)))
choices, final_choice = [] , []
#creating random number of pots of random number of golds
def cho(pot,st,ed):
    if st >= ed: 
        return(0) 
    choice_st = pot[st] + min(cho(pot,st+2,ed),cho(pot,st+1,ed-1))
    choice_ed = pot[ed-1] + min(cho(pot,st,ed-2),cho(pot,st+1,ed-1))

    return(max(choice_st, choice_ed)) 
print(pots)
res = cho(pots,0,len(pots))
print(res, sum(pots) - res)