#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid? Allgemein NxN

#Die Lösung dieses Problems ist der Binominal Koeffizient: Man läuft genau 2N Schritte von oben rechts nach unten links. Wenn man alle Schritte nach Rechts verteilt,
#müssen die Schritte die übrig bleiben, die Schritte nach unten sein. Die Frage ist also, wie viele Möglichkeiten gibt es N Elemente auf 2N Stellen zu verteilen?

#1. Möglichkeiten: für die erste Ziehung hat man 20, dann 19, 18,17,...10 Möglichkeiten das entsprechende Element zu verteilen.

#2N(2N-1)(2N-2)...(2N-N+1)

#2. Die meißten sind nur Wdh: Die obige Formel ergibt alle Möglichkeiten und beinhaltet auch Permutationen (alle Rs sind gleich, es ist als egal, welches R zuerst gezogen wird)
#Man kann N Zahlen N!=N*N-1*...*1 mal permutieren. Bsp. 123, 132, 213, 231, 321, 312.

#Das Ergebnis ist also (20*19*18*...*10)/(10*9*8*...*1)

N=20

one=list(range(21,41))
two=list(range(1,21))
Zähler=1
Nenner=1

for x in one:
    Zähler=Zähler*x

for y in two:
    Nenner=Nenner*y

Ways=Zähler/Nenner

print(one)
print(two)
print(Ways)