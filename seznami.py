#stetje    0 1 2 3 4 5 .....
stevila = [5, 2, 8, 3]

#izpis vseh stevil
print(stevila)

stevila.sort()
print("Stevila smo uredili")
print(stevila)

#izpis stevila na mestu 1
print(stevila[1])

#izpis stevila na mestu 0
print(stevila[0])

#Count all elements
print("Count of all elements is: " + str(len(stevila)))

#Add elements in
stevila.append(7)
print("Dopolnjen seznam: ")
print(stevila)

#Delete elements
stevila.remove(3)
print("Spremenjen seznam: ")
print(stevila)

#Delete elements at specified index
del stevila[0]
print(stevila)

print("Vsi elementi prek for zanke")
for stevilo in stevila:
    print("Sedaj je stevilo enako " + str(stevilo))
