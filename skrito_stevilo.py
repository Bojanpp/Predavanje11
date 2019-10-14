import random
import json

skrito_stevilo = random.randint(1, 10)

with open("tocke.txt") as datoteka:
    tocke = json.loads(datoteka.read())

print("Tocke do sedaj: ")
for tocka in tocke:
    print("   " + str(tocka))


stevec = 0
while True:
    stevilo = int(input("Vpisi stevilo: "))
    stevec = stevec + 1

    if stevilo == skrito_stevilo:
        print("Cestitke")
        break
    elif stevilo > skrito_stevilo:
        print("Stevilo je manjse")
    else:
        print("Stevilo je vecje")

print("Stevilo poskuskov je bilo: " + str(stevec))

tocke.append(stevec)

with open("tocke.txt", "w") as datoteka:
    datoteka.write(json.dumps (tocke))
