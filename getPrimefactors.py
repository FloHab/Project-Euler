#This function returns a set of all distinct primefactors of a input x.

def getPrimefactors(x):
    primefactors=set()
    devider=3
    while devider<round(x**(0.5)+1):
        if x%2==0:
            primefactors.add(2)
            x=x/2
        if x%devider==0:
            primefactors.add(int(devider))
            x=x/devider
            devider=3
        else:
            devider=devider+2
    primefactors.add(int(x))
    return(primefactors)
