#check N prime numbers  1-100
N=62
if N==0 or N==1:
    prime=False
else:
    prime=True
    for i in range(2,N):
        if N % i== 0 :
            prime=False

            break
if prime:
    print(f"Ο αριθμός {N} είναι πρώτος")
else:
    print(f"Ο αριθμός {N} δεν είναι πρώτος")