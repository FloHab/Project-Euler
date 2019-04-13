#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?
import time
start_time = time.clock()
coins=[1,2,5,10,20,50,100,200]
'Initialisiere dynamisches Array'
array={0:1}
for x in range(1,201):
    array[x]=0
for x in coins:
    for y in array:
        try:
            array[y]=array[y]+array[y-x]
        except KeyError:
            pass
print(array[200])
print(time.clock() - start_time, "seconds")

#Die inteligente Lösung hier ist dynamische Programmierung: Breche das Problem in kleiner Teilproblme runter, die aufeinander
#aufbauen. Bsp.: auf wie viele Arten kann man 5p mit 1p und 2p Münzen herausgeben.

#1. mit 1p Münzen:
#   1p:1, 2p:1, 3p:1 4p:1 5p:1

#2. mit 2p und 1p Münzen:
#   1p:1 2p:1+1=2 3p:1+1=2 4p:2+1=3 5p:2+1=3(auf 1 Weise mit 1p Münze + so viele Müglichkeiten wie man 5p-2p herausgeben kann)

#Anders: auf wie viele Weisen kann ich 5p mit einer 1p und einer 2p Münze zurück geben:

#nur mit 1p Münze auf eine Art+auf so viele Arten, wie ich 5p-2p=3p mit 1p und 2p Münzen zurück geben kann