'''
Walter Biribicchi

@ Sudoku solver @

14/03/2020
'''
    
import numpy as np
import itertools as it

############### Sudoku input ###########################

sudo0=np.array([[0,0,8,0,0,0,9,0,2],
                [0,6,5,0,1,8,0,0,0],
                [0,9,0,0,0,0,0,0,0],
                [0,0,3,6,0,7,5,0,0],
                [9,0,0,0,0,0,0,0,6],
                [0,0,1,4,0,9,8,0,0],
                [0,0,0,0,0,0,0,4,0],
                [0,0,0,1,6,0,2,9,0],
                [7,0,9,0,0,0,1,0,0]])

sudo=np.copy(sudo0)


############### Functions ############################  

def c_row(a,i):
    # a = num to check
    # i = row to check
    if a in sudo[i[0],:]:
        return True
    else:
        return False
    
def c_col(a,i):
    # a = num to check
    # i = col to check
    if a in sudo[:,i[1]]:
        return True
    else:
        return False
    
def block(a):
    # a,b = coord of up-left 
    return sudo[a[0]:a[0]+3,a[1]:a[1]+3]

def ind_bl(a):
    # a,b = coord of num to check
    # return index of block
    if a[0] in range(0,3):
        if a[1] in range(0,3):
            return [0,0]
        if a[1] in range(3,6):
            return [0,3]
        if a[1] in range(6,9):
            return [0,6]
    
    if a[0] in range(3,6):
        if a[1] in range(0,3):
            return [3,0]
        if a[1] in range(3,6):
            return [3,3]
        if a[1] in range(6,9):
            return [3,6]
        
    if a[0] in range(6,9):
        if a[1] in range(0,3):
            return [6,0]
        if a[1] in range(3,6):
            return [6,3]
        if a[1] in range(6,9):
            return [6,6]
        
def c_block(a,i):
    # a = num to check
    # i = coord of num to check
    if a in block(ind_bl(i)):
        return True
    else:
        return False

def multic(a,b):
    if c_block(a,b) or c_col(a,b) or c_row(a,b):
        return True
    return False

def valid(a,b):
    # a,b = coord of possible zero
    if sudo[a,b]==0:
        return True
    else:
        return False
    
def findz(s):
    for i in range(0,9):
        for j in range(0,9):
            if s[i,j]==0:
                return(i,j)
       
        
############### Algorithm ###########################   

def sudo_solve(s):
    
    left=np.shape(np.where(s==0))[1]
    
    if left==0:
        return True
    [i,j]=findz(s)            
    if valid(i,j):
        for n in range(1,10):
            if multic(n,[i,j])==False:
                s[i,j]=n
                print(left)
                if sudo_solve(s):
                    return True
                s[i,j]=0
    return False
    
    
############### Output ###########################       
    
if sudo_solve(sudo):
    print('Finito!')
    
else:
    print('Nessuna soluzione!')
    
    
    
    
    
    
    

 
                    
                        
                        
    
    
    
    
    
    