#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
#For which value of p ≤ 1000, is the number of solutions maximised?
count={}
for x in range(1,1001):
    count[x]=0
for a in range(1,1000):
    for b in range(1,1000):
        d=a+b+(a**2+b**2)**(0.5)
        if d>1000:
            break
        if d-int(d)==0:
            count[d]=count[d]+1
max=0
key=0
for x in count:
    if count[x]>max:
        max=count[x]
        key=x
print(key)
