wortel = 5
while wortel != 0:
    x = input("Voer een getal in: ")
    wortel = float(x)
    if wortel < 0:
        print("Dombo, geen negatief getal")
    else:
        print(wortel**0.5)
