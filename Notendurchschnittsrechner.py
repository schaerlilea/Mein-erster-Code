note = []
summe = 0

while True:                              #solange die oben genannten Variablen stimmen, dann wird das Programm ausgeführt
    i = input("Note eingeben ")          # i ist das, was man in der Kommandozeile eingibt, also eine Note
    if i == "exit":                      # wenn man in die Kommandozeile "exit" eingibt, wird das Programm beendet     
         break


    note.append(i)                      # der note wird (immernoch in der while-Schleife) immer die Note angefügt, die man neu in die Kommandozeile schreibt

    summe = summe+float(i)              # die Summe der Noten ist die summe + die eingegebene Note 

    
    print(note)                         # die Note wird im Terminal aufgezeigt
    
    laenge= len(note)                   # die länge ist die Länge der Anzahl aller noten
    
    durchschnitt=summe/laenge           # Der Durchschnitt ist die Summe der Noten geteilt durch die Länge 
    print(durchschnitt)                 # der Druchschnitt wird im Terminal angezeigt

 

                 #der Note wird dann angehängt, dass nochmals "Note eingeben" in der Kommandozeile steht

           #die Summe der Noten beträgt dann die neue Note und die Noten, die schon eingegeben wurden

               # wenn man "exit" in die Kommandozeile schreibt, wird das Programm beendet
