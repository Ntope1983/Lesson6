#Save in Tuple the first prime numbers i range 2-100
def checkprime (N):
    if N == 0 or N == 1:
        prime = False
    else:
        prime = True
        for i in range(2, N):
            if N % i == 0:
                prime = False
                break
    return prime

ListPrimes=[]
for i in range(100):
    if checkprime(i):
        ListPrimes.append(i)
TuplePrimes=tuple(ListPrimes)
print(TuplePrimes)












