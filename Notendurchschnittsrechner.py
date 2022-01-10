note = []
summe = 0

while True: 
    i = input("Note eingeben ")

    note.append(i)

    summe = summe+float(i)

    if input == "exit":
         break

    print(note)
    
    laenge= len(note)
    
    durchschnitt=summe/laenge
    print(durchschnitt)

