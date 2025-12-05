#Read numbers (1-10) and sign in the list -> then  create a tuple with this list and second tuple squared sorted from this lis
ListIntegers=[]
for i in range(11):
    while True:
        try:
            χ=int(input("Δώσε έναν ακεραιο αριθμό μεταξύ του 1 και 10"))
            if χ.is_integer():
                if 20 >= χ >= 10:
                    ListIntegers.append(χ)
                    break
                else:
                    continue
        except ValueError:
            print("Λαθος εισαγωγή ακεραίου")
            continue
tuple1=tuple[ListIntegers[:]]
ListIntegers.sort()
for index in range(len(ListIntegers)):
    ListIntegers[index]=ListIntegers[index]**2
tuple2=ListIntegers.copy()
print(tuple1)
print(tuple2)
