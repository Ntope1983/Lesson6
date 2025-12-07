#Παιχνίδι κάρτας μνημης
from Exercise7 import second_card

Card_Numbers=[2,1,3,4,1,2,3,4]# Οι αριθμοί των καρτών
Card_id=[1,2,3,4,5,6,7,8]# Η θέση της κάθε κάρτας
List_Players_List_Card=[]# Η λίστες με τους παιχτες που περιεχουν τις λίστες με τις κερδισμένες κάρτες
while True:# Τιμή εισόδου αριθμών παικτών
    num_of_players=input("Πόσοι παικτες θα παίξουν")
    if num_of_players.isdigit():
        break
num_of_players=int(num_of_players)#Μετατροπή σε ακέραιο
for i in range(num_of_players):# Δημιουργία Λίστας για τους αντιστοιχους παίκτες
    List_Players_List_Card.append([])
for i in range(num_of_players):#Για κάθε παικτη
    while len(Card_id) > 0:#Οσο υπάρχουν κάρτες
        print(f"O παίχτης {i + 1} εχει σειρά να παίξει")
        print(f"Οι κάρτες που είναι διαθέσιμες είναι{Card_id}")
        while True:#Έλεγχος εισαγωγής 1ης καρτας
            try:
                first_card = int(input("Επελεξε 1η κάρτα."))
                if first_card in Card_id:
                    break
                else:
                    print("H καρτα δεν είναι διαθεσιμη")
            except ValueError:
                print("Λαθος εισαγωγή Προσπάθησε Ξανά")
                continue
        while True:
            try:
                second_card = int(input("Επελεξε 2η κάρτα."))#Έλεγχος εισαγωγης 2ης καρτας
                if second_card in Card_id:
                    break
                else:
                    print("H καρτα δεν είναι διαθεσιμη")
            except ValueError:
                print("Λαθος εισαγωγή Προσπάθησε Ξανά")
                continue

        if Card_Numbers[first_card - 1] == Card_Numbers[second_card - 1]:#Εάν είναι ίδιες τις κέρδισε και συνεχίζει
            print(f"Μπράβο βρήκες τις 2 κάρτες")
            List_Players_List_Card[i].append(first_card)
            List_Players_List_Card[i].append(second_card)
            Card_id.remove(first_card)
            Card_id.remove(second_card)
            continue
        else:
            print(f"Δυστυχώς δε τα κατάφερες.O επόμενος παίκτης παρακαλώ!!!")
            break


print(List_Players_List_Card)#Εμφανιση κερδισμενων καρτων!