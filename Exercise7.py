Card_List=[2,1,3,4,1,2,3,4]
Card_List_Open=[]
while len(Card_List_Open)<8:
    χ=int(input("Επελεξε 1η κάρτα."))
    if χ.is_integer() and 9>χ>0 and χ not in Card_List_Open:
        print(f"Επέλεξες τον {Card_List[χ]} στη θέση {χ}")
    y = int(input("Επελεξε 2η κάρτα."))
    if y.is_integer() and 9>y>0 and y!=χ and y not in Card_List_Open:
        print(f"Επέλεξες τον {Card_List[y]} στη θέση {y}")
    if χ==y:
        print(f"Μπράβο βρήκες τις 2 κάρτες")
        Card_List_Open.append(χ)
    else:



