Card_Numbers=[2,1,3,4,1,2,3,4]
Card_id=[1,2,3,4,5,6,7,8]
while True:
    num_of_players=input("Πόσοι παικτες θα παίξουν")
    if num_of_players.isdigit():
        break
for i in range(num_of_players):

    while len(Card_id)!=0:
        print(f"Οι κάρτες που είναι διαθέσιμες είναι{Card_id}")
        χ=int(input("Επελεξε 1η κάρτα."))
        if χ.is_integer() and χ in Card_id :
            print(f"Επέλεξες τον {Card_Numbers[χ-1]} στη θέση {χ}")
        y = int(input("Επελεξε 2η κάρτα."))
        if y.is_integer() and y in Card_id:
            print(f"Επέλεξες τον {Card_Numbers[y-1]} στη θέση {y}")
        if Card_Numbers[χ-1]==Card_Numbers[y-1]:
            print(f"Μπράβο βρήκες τις 2 κάρτες")
            if χ > y:
                Card_Numbers.pop(χ - 1)
                Card_Numbers.pop(y - 1)
                Card_id.remove(χ)
                Card_id.remove(y)
            else:
                Card_Numbers.pop(y - 1)
                Card_Numbers.pop(χ - 1)
                Card_id.remove(y)
                Card_id.remove(χ)
        else:
            print(f"Δυστυχώς δε τα κατάφερες.Προσπάθησε Ξανά")
