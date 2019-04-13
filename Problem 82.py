'''The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell 
in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 
80 matrix, from the left column to the right column.'''

import time
import numpy as np
import matplotlib.pyplot as plt
start_time = time.clock()

def read_matrix(path):
    '''This function opens a text file specified by the variable path as it is given for problem 81,82 and 83 and 
    returns the corresponding matrix.'''

    f=open(path,'r')
    file=f.read()
    f.close()

    element=''
    elements=[]
    matrix=[]
    for x in file:
        if x=='\n':
            elements.append(int(element))
            matrix.append(elements)
            elements=[]
            element=""
        if x==",":
            elements.append(int(element))
            element=""
        if x!='\n' and x!=',':
            element=element+x
    matrix=np.asarray(matrix)
    return(matrix)

matrix_orig=read_matrix('p082_matrix.txt')

(lines,columns)=np.shape(matrix_orig)
matrix_dyn=matrix_orig.copy()
matrix_dyn[:,1]=matrix_orig[:,0]+matrix_orig[:,1]


for column in range(2,columns):
    new_col=[]
    for line in range(0,lines):
        paths= []
        for x in range(0,lines):
            if x==line:
                path = matrix_dyn[line, column - 1] + matrix_orig[line,column]
                paths.append(path)
            if x<line:
                path = matrix_dyn[x, column - 1] + sum(matrix_orig[x:line+1, column])
                paths.append(path)
            if x>line:
                path = matrix_dyn[x, column - 1] + sum(matrix_orig[line:x+1, column])
                paths.append(path)
        new_col.append(min(paths))
    matrix_dyn[:,column]=new_col

print(min(matrix_dyn[:,-1]))
print(time.clock() - start_time, "seconds")

plt.imshow(matrix_dyn)
plt.colorbar()
plt.show()