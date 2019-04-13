file=open("C:\\Users\\Florian Habenstein\\PycharmProjects\\Project Euler\\p067_triangle.txt","r")
triangle=[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
count=0
for line in file:
    x=line.split()
    triangle[count]=x
    count=count+1
print(triangle)
print(len(triangle))
for x in range(98,-1,-1):
    for y in range(len(triangle[x])):
        triangle[x][y]=int(triangle[x][y])+max(int(triangle[x+1][y]),int(triangle[x+1][y+1]))
print(triangle[0][0])
print(triangle)