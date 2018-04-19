# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:18:49 2018
8-queens local beam search
@author: Yufeng Zhou
"""

#Q2 a) attacking paris
import random
import time
def random_state():
    """
    generate an initial state, like "31046715"
    return: a random state
    """
    s=""
    for i in range(0,8):
         s += str(random.randint(0, 7))
    return s


def attacking_pairs(s): 
    """
    check how many attacking pairs in the state
    param state: input state
    return:  number of attacking pairs
    """
    counter=0
    for i in range(0,7):
        for j in range(i+1,8):
            if abs(int(s[i])-int(s[j])) == abs(i - j) or s[i] == s[j]:
                counter+=1
    return counter


#Q2 b) local beam search
def generate_successor(s):
    """
    generate all 56 possible next state
    param state: input state
    return: a list of new states
    """
    res=[]
    for index, i in enumerate(s):
        for j in range(8):
            if j != int(i):
                res.append(s[:index] + str(j) + s[index + 1:])
    return res

def lbs(k):
    """
    do the local beam search
    param: beam size
    return: number of iteration until found the goal, goal state
    """
    goal_state=[]
    F=list()
    max_iter=100
    iteration=0
#generate k states in F 
    for i in range(k):
        s=random_state()
        F.append((s,attacking_pairs(s)))
        
    while is_goal(F) == False and iteration<max_iter:
        F_prime=list() 
        for i in range(k):
                for ns in generate_successor(F[i][0]):
                    F_prime.append((ns, attacking_pairs(ns)))
# sorted the successors by performance               
        F_prime = sorted(F_prime, key=lambda x:x[1], reverse=False)
        
#select k best
        F=list()
        for i in range(k):
             F.append(F_prime[i])
        iteration +=1
    goal_state=F[0]
    return iteration, goal_state
          
def is_goal(F):
    """
    check if it satisfy the goal, 0 attacking pairs
    param: input list contains a state and a number of attacking pairs
    return: Ture or False
    """
    if F[0][1] == 0:
        return True
    else:
        return False
           
if __name__ == "__main__":
    for k in [1,10,50]:
        print("beam size k =",k)
        start=time.time()
        counter=0
        sum_iter=0
# for each k, run 50 times, count their iterations and number of goal state found        
        for i in range(50):
            Result=lbs(k)
            end=time.time()
            iteration=Result[0]
            goal_state=Result[1]
            sum_iter +=iteration
        
            if goal_state[1] == 0:
                counter +=1
                
        past = end - start    
        print ("total time:", past)
        print ("number of goal state found:", counter)
        print(sum_iter)

    
            
                    
    
