import random

lista = []

def sorozatok():
    for i in range(0, 8, 1):
        szam: int= random.randint(-100, 859)
        lista.append(szam)
        if i < 7:
            print(szam, end = "; ")
        else:
            print(szam, end = " ")