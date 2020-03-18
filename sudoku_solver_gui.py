'''
Walter Biribicchi

@ Sudoku solver @

14/03/2020
'''
    
import numpy as np

############### Sudoku input ###########################

sudo=np.zeros((9,9),'int8')
        
def pr():
    
    for i in range(9):
        a=entries[i].get()
        b=entries[i+9*1].get()
        c=entries[i+9*2].get()
        sudo[0,i]=a
        sudo[1,i]=b
        sudo[2,i]=c
        
        d=entries[i+9*3].get()
        e=entries[i+9*4].get()
        f=entries[i+9*5].get()
        sudo[3,i]=d
        sudo[4,i]=e
        sudo[5,i]=f
        
        g=entries[i+9*6].get()
        h=entries[i+9*7].get()
        l=entries[i+9*8].get()
        sudo[6,i]=g       
        sudo[7,i]=h
        sudo[8,i]=l
        
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
       
def solv():
    
    print(sudo)
    if sudo_solve(sudo):
        print('\n++++++++++++++++++++++++++++++')
        print('Finito!')
        print('++++++++++++++++++++++++++++++\n')
        print(sudo)
        
    else:
        print('Nessuna soluzione!')

def showsol():
    txt=tk.Label(frames,text='{}'.format(sudo))
    txt.pack()
############### GUI ###########################
        
import tkinter as tk

root=tk.Tk()

f1=tk.Frame(root)
f2=tk.Frame(root)

frameg=tk.Frame(f1)
frameb=tk.Frame(f1)
frames=tk.Frame(f2)
framesh=tk.Frame(f2)

entries=[]

for i in range(9):
    for j in range(9):
        wid=tk.Entry(frameg,width=3)
        wid.grid(row=i,column=j)
        entries.append(wid)


bins=tk.Button(frameb,text='Inserisci',command=pr)
bsolve=tk.Button(frameb,text='Risolvi',command=solv)
bshow=tk.Button(framesh,text='Mostra Soluzione',command=showsol)



f1.pack(side=tk.LEFT)
f2.pack(side=tk.RIGHT)

frameg.pack()
frameb.pack()
frames.pack()
framesh.pack()

bins.pack()
bsolve.pack()
bshow.pack()


root.mainloop()

        

    


    
    
    

 
                    
                        
                        
    
    
    
    
    
    