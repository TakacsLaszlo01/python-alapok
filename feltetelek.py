nev = input("Adja meg a nevét: ")
hossz = len(nev)

if hossz >= 18:
    print("Hosszú nevet adott meg!")
elif hossz >= 10:
    print("Átlagos hosszú nevet adott meg!")
else:
    print("Rövid nevet adott meg!")

n = int(input("Adjon meg egy kétszámjegyű egész számot, ami 3-al osztható, de 9-el nem!"))
if n >= 10 and n < 100:
    if n % 3 == 0 and n % 9 > 0:
        print("A szám megfelel!")
    else:
        print("A szám oszthatósága nem megfelelő!")
else:
    print("Nem kétszámjegyű számot adott meg!")

#Kérj be egy valós számot, és vizsgálja meg, hogy az abszolútértéke nagyobb-e mint 900!
x = float(input("Adjon meg egy valós számot: "))
abszolutertek = abs(x)
if abszolutertek > 900:
    print(f"{x} abszolútértéke nagyobb mint 900!")
else:
    print(f"{x} abszolútértéke kisebb vagy egyenlő mint 900!")