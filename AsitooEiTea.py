#1
taisarvude_arv = 0

for i in range(15):
    arv = float(input(f"Sisesta {i + 1}. arv: "))
    if arv.is_integer():
        taisarvude_arv += 1

print("Täisarve kokku:", taisarvude_arv)

#------------------------------------
#2

A = int(input("Sisesta naturaalarv A: "))
summa = 0

for i in range(1, A + 1):
    summa += i

print(f"Arvude summa vahemikus 1 kuni {A} on:", summa)

#------------------------------------
#3

korrutis = 1
positiivseid_leitud = False

for i in range(8):
    arv = float(input(f"Sisesta {i + 1}. arv: "))
    if arv > 0:
        korrutis *= arv
        positiivseid_leitud = True

#------------------------------------
#4

if positiivseid_leitud:
    print("Positiivsete arvude korrutis on:", korrutis)
else:
    print("Positiivseid arve ei sisestatud.")

for arv in range(10, 21):
    print(f"{arv} ruudus on {arv ** 2}")

#------------------------------------
#5

N = int(input("Mitu arvu soovid sisestada (N)? "))
negatiivsete_summa = 0

for i in range(N):
    arv = float(input(f"Sisesta {i + 1}. arv: "))
    if arv < 0:
        negatiivsete_summa += arv

print("Negatiivsete arvude summa on:", negatiivsete_summa)

#------------------------------------
#6

N = int(input("Mitu arvu soovid sisestada (N)? "))
negatiivsed = 0
positiivsed = 0
nullid = 0

for i in range(N):
    arv = float(input(f"Sisesta {i + 1}. arv: "))
    if arv < 0:
        negatiivsed += 1
    elif arv > 0:
        positiivsed += 1
    else:
        nullid += 1

print("Negatiivseid arve:", negatiivsed)
print("Positiivseid arve:", positiivsed)
print("Nulle:", nullid)

#------------------------------------
#7

A = int(input("Sisesta vahemiku algus (A): "))
B = int(input("Sisesta vahemiku lõpp (B): "))
K = int(input("Sisesta jagaja (K): "))

print(f"Arvud vahemikus [{A}, {B}], mis jaguvad arvuga {K}:")
for arv in range(A, B + 1):
    if arv % K == 0:
        print(arv)

#------------------------------------
#9

S = float(input("Sisesta algsumma (S eurot): "))
N = int(input("Sisesta aastate arv (N): "))

for aasta in range(N):
    S *= 1.03

print(f"Summa {N} aasta järel on: {S:.2f} eurot")

#------------------------------------
#20
summa = 0
for arv in range(1, 51):
    if arv % 5 == 0 or arv % 7 == 0:
        summa += arv

print(f"Summa on: {summa}")

#------------------------------------
#19
for arv in range(35, 88):
    if arv % 7 in (1, 2, 5):
        print(arv, end=" ")

#------------------------------------
#18
for arv in range(20, 51):
    if arv % 3 == 0 and arv % 5 != 0:
        print(arv, end=" ")

#------------------------------------
#17
arv = int(input("Sisesta arv, mille korrutustabelit soovid: "))

for i in range(1, 11):
    print(f"{arv}*{i}={arv * i}")
