#!/usr/bin/env python
# coding: utf-8

# In[180]:


import numpy as np
import copy as cp

board =[[0, 4, 3, 0, 8, 0, 2, 5, 0],
       [6, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 9, 4],
       [9, 0, 0, 0, 0, 4, 0, 7, 0],
       [0, 0, 0, 6, 0, 8, 0, 0, 0],
       [0, 1, 0, 2, 0, 0, 0, 0, 3],
       [8, 2, 0, 5, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 5],
       [0, 3, 4, 0, 9, 0, 7, 1, 0]]

board = np.array(board)
unsolved_board = cp.deepcopy(board)


# In[181]:


def in_row(number, row):
    return number in board[row]
in_row(2, 0) #returns true if 2 is in row 0, else false


# In[182]:


def in_column(number, column):
    return number in board[:,column]
in_column(1, 0) #returns true if 1 is in row 0, else false


# In[183]:


def in_square(number, sqr):
    insqr = False
    for l in board[sqr[0]*3:(sqr[0]+1)*3,sqr[1]*3:(sqr[1]+1)*3]:
        if number in l:
            insqr = True
    return insqr
in_square(1, (0,0)) #returns true if 2 is in the square (0,0) (the one in the board's upper left), else false


# In[158]:


def check(number, row, column):
    return (not in_row(number, row) 
            and not in_column(number, column) 
            and not in_square(number, (row//3, column//3))) #returns true or false 


# In[159]:


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None #find empty cells of the board (those with containing 0)


# In[170]:


def solve(board): 
    
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row = empty[0]
        column = empty[1]      
    
    for i in range(1,10):
        if check (i , row, column):
            board[row][column] = i
            
            if solve(board):
                return True
            else:
                board[row][column] = 0        
    return False #recursive methode to solve the board


# In[179]:


print("Unsolved board")
print(unsolved_board,"\n")
solve(board)
print("Solved board")
print(board)

