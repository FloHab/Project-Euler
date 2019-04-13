n=100
fakultät=1
for x in range(100):
    fakultät=fakultät*n
    n=n-1
fakultät=str(fakultät)
result=0
for x in fakultät:
    result=result+int(x)
print(result)