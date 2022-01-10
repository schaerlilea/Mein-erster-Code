note = []
summe = 0

while True: 
    i = input("Note eingeben ")
    if i == "exit":
         break


    note.append(i)

    summe = summe+float(i)

    
    print(note)
    
    laenge= len(note)
    
    durchschnitt=summe/laenge
    print(durchschnitt)

