import random

# 1. POSTAVKE MATRICE
redak = 7
stupac = 7
matrica = []

# 2. GENERIRANJE MATRICE
# Vanjska petlja stvara retke
for i in range(redak):
    red = []
    # Unutarnja petlja popunjava svaki redak stupcima (brojevima)
    for j in range(stupac):
        unos = random.randint(1, 9)
        red.append(unos)
    matrica.append(red)

# 3. ISPIS MATRICE (da izgleda kao tablica)
print("Generirana matrica:")
for red in matrica:
    print(red)

print("-" * 20) # Vizualna linija za razdvajanje

# 4. IZRAČUN SUME RUBOVA
# Prolazimo kroz svako polje i provjeravamo je li na rubu
suma_rubova = 0
for i in range(redak):
    for j in range(stupac):
        # Provjera: prvi red, zadnji red, prvi stupac ili zadnji stupac
        if i == 0 or i == redak - 1 or j == 0 or j == stupac - 1:
            suma_rubova += matrica[i][j]
print("Suma na rubovima matrice iznosi:", suma_rubova)


# 5. IZRAČUN GLAVNE DIJAGONALE
# Kod dijagonale su indeksi i i j uvijek isti (0,0), (1,1), (2,2)...
suma_dijagonale = 0
for i in range(redak):
    for j in range(stupac):
        if i==j:
            suma_dijagonale += matrica[i][i]

print("Suma na dijagonalama iznosi:",suma_dijagonale)