def isPrime(number):
    current=number
    faktor=2
    while faktor<=(number/2+1):
        if current%faktor==0:
            return(False)
        else:
            faktor=faktor+1
    return(True)
