#'Man kann die Fragestellung mit der Gleichung phi(x)=n*Produkt der Produkte aus (1-1/p) wobei p die Primfaktoren der Zahl n sind.
#So lässt sich das Problem verstehen, als die Suche nach dem der Zahl, bei der folgende Funktion maximal wird:

#1/Produkt aus (1-1/p)

# wobei P die Primfaktoren von der gesuchten Zahl sind. Die Funktion wird dann maximal, wenn die
# gesuchte Zahl n aus möglichst vielen Primfaktoren zusammengestzt ist.

#Man kann also die Fragestellung auch Formulieren, als die Suche nach der Zahl unter 1000000, die die meißten unterschiedlichen Primfaktoren enthält.
from isPrime import isPrime
primes=[]

for x in range(2,400):
    if isPrime(x)==True:
        primes.append(x)
product=1
for x in primes:
    if product*x<1000000:
        product=product*x

print(product)
