#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
'Jede natürliche Zahl ist entweder eine Primzahl oder lässt sich als Produkt von Primzahlen Schreiben, daraus folgt: dass heißt, jede Zahl, die keine Primzahl ist, ein Produkt aus vorrangehenden Primzahlen ist. Damit ist jede Zahl, die durch eine Zahl n teilbar ist, die keine Primzahl ist, auch durch die jeden Primfaktor der Zahl n teilbar '

def large_prime(number):
    factor=2
    prime=2
    list_of_factors=[]
    list_of_steps=[]
    count=0

    while not count==100:
        while not number%factor==0:
            factor=factor+1
        if number==1:
            break
        else:
            number=number/factor
            print(number)
            list_of_factors.append(factor)
            list_of_steps.append(number)
            factor=2
            count=count+1
            if number == 1:
                break
    print(list_of_factors)
    print(list_of_steps)

large_prime(600851475143)