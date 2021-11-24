gegevenWoord = "input"
inputWoord = "input"

def vergelijk(woord1, woord2):
    for letter1, letter2 in zip(woord1, woord2):
        if letter1 == letter2:
            print("Dik trots letters kloppen, en door")
        else:
            print("Je naait")

vergelijk(gegevenWoord, inputWoord)


    