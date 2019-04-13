def getDivisors(x):
    Divisors=set()
    for y in range(1,round(((x+1)/2)+0.5)):
        if x%y==0:
            Divisors.add(y)
    return(Divisors)

def isAbundant(x):
    y=getDivisors(x)
    if sum(y)>x:
        return(True)
    else:
        return(False)
