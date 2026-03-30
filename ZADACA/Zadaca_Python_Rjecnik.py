import random

imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko", "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]
#ispis koliko je studenata
print("Broj studenata u listi iznosi:",len(imena))


#Definiranje Rijecnika
Random_Ocjene={}

#Definiranje logike za upis ocijena
for brojac in imena:
    Random_Ocjene[brojac]=random.randint(1,5)
    print(brojac,Random_Ocjene[brojac])

#Definiranje logike za izracun prosjeka(veci od 1)
prolaz=0

for brojac in Random_Ocjene:
    if Random_Ocjene[brojac]>1:
        prolaz+=1

postotak=(prolaz/len(Random_Ocjene))*100

print(f"Postotak prolaznosti: {postotak:.2f}%")
