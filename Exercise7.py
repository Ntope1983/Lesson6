#Παιχνίδι κάρτας μνήμης
#έλεγχος τιμής εισαγωγής να είναι string-ακέραιο
def input_integer_value(x):
    while True:  # Έλεγχος εισαγωγής 1ης κάρτας
        try:
             value=int(input(f" Επέλεξε {x} η κάρτα."))
             return value
        except ValueError:
            print("Λάθος εισαγωγή Προσπάθησε Ξανά")


Card_Numbers=[2,1,3,4,1,2,3,4]# Οι αριθμοί των καρτών
Card_id=[1,2,3,4,5,6,7,8]# Η θέση της κάθε κάρτας
List_Players_List_Card=[]# Η λίστες με τους παίχτες που περιέχουν τις λίστες με τις κερδισμένες κάρτες
while True:# Τιμή εισόδου αριθμών παικτών
    num_of_players=input("Πόσοι παίκτες θα παίξουν")
    if num_of_players.isdigit():
        break
num_of_players=int(num_of_players)#Μετατροπή σε ακέραιο
for i in range(num_of_players):# Δημιουργία Λίστας για τους αντίστοιχους παίκτες
    List_Players_List_Card.append([])
while len(Card_id) > 0:
    turn_player=0
    while (turn_player < num_of_players) and len(Card_id ) > 0:#Για κάθε παίκτη
        print(f"O παίχτης {turn_player + 1} Έχει σειρά να παίξει")
        print(f"Οι κάρτες που είναι διαθέσιμες είναι{Card_id}")

        first_card = input_integer_value(1)#Αποθήκευση με έλεγχο εισαγωγής την πρώτη κάρτα
        while not (first_card in Card_id):
            print("Επέλεξε έγκυρο αριθμό κάρτας")
            first_card=input_integer_value(1)

        second_card = input_integer_value(2)#Αποθήκευση με έλεγχο εισαγωγής τη δεύτερή κάρτα
        while second_card == first_card:
            print("Δεν μπορείς να επιλέξεις την ίδια κάρτα με τη πρώτη")
            second_card = input_integer_value(2)
        while not (second_card in Card_id) :
            print("Επέλεξε έγκυρο αριθμό κάρτας")
            second_card = input_integer_value(2)

        if Card_Numbers[first_card - 1] == Card_Numbers[second_card - 1]:#Εάν είναι ίδιες τις κέρδισε και συνεχίζει γιατί δεν αυξάνει το turn κατά 1
            print(f"Μπράβο βρήκες τις 2 κάρτες")
            List_Players_List_Card[turn_player].append((first_card, second_card))
            Card_id.remove(first_card)
            Card_id.remove(second_card)
        else:
            print(f"Δυστυχώς δε τα κατάφερες.O επόμενος παίκτης παρακαλώ!!!")
            turn_player = turn_player + 1


print(f"Τέλος Παιχνιδιού {List_Players_List_Card}")#Εμφάνισή κερδισμένων καρτών!