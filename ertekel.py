def ertekeles():
    het_napja: str= input("Adja meg a hét napját: ")
    ora_neve: str= input("Adja meg az óra nevét: ")
    ertekel: int= int(input("Adja meg az értékelést (0-5): "))
    if ertekel < 0: 
        print("Az értékelés nem lehet negatív!")
    elif ertekel > 5: 
        print("5 pont feletti értékelés nem elfogadható!")
    else: 
        print("Köszönjük az értékelést!")
        print(f"Hét napja: {het_napja}\nÓra neve: {ora_neve}\nÉrtékelés (0-5): {ertekel}")