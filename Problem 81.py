#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and
#down, is indicated in bold red and is equal to 2427.
#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80
#by 80 matrix, from the top left to the bottom right by only moving right and down.
import time, math
start_time = time.clock()

'Open file and read content'
f=open('p081_matrix.txt','r')
file=f.read()
f.close()

'Sort matrix elements in lists in lists'
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

'Dynamic Matrix Manipulation'
for x in range(1,159):
    for y in range(x+1):
        try:
            a=matrix[(x-y)-1][y]
            if (x-y-1)<0:
                a=math.inf
        except IndexError:
            a=math.inf
        try:
            b=matrix[x-y][y-1]
            if y-1<0:
                b=math.inf
        except IndexError:
            b=math.inf
        try:
            matrix[x-y][y]=matrix[x-y][y]+min(a,b)
        except IndexError:
            pass
print(matrix[79][79])
print(time.clock() - start_time, "seconds")