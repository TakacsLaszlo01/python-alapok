a = 9
b = 22

print(f"{a} és {b} összege {a+b}")
print(str(a) + " és " + str(b) + " összege " + str(a + b))

if a > 5 and a < 20:
    print(f"{a} nagyobb mint 5, de kisebb mint 20")

if b <= 10 or b >= 22:
    print(f"{b} vagy kisebb egyenlő mint 10, vagy nagyobb egyenlő mint 22!")

maxPont = int(input("Adja meg a dolgozat maximális pontszámát: "))
elertPont = int(input("Adja meg az elért pontszámot: "))
szazalek = float(100 * elertPont / maxPont)

print(f"{szazalek:.2f}% lett a dolgozat eredménye!")
if szazalek >= 85:
    print("Jeles (5) lett a dolgozat!")
    if szazalek > 100:
        print("Túlteljesítette az elvárásokat!")
    elif szazalek == 100:
        print("Hibátlan lett!")
elif szazalek >= 70:
    print("Jó (4) lett a dolgozat!")
elif szazalek >= 60:
    print("Közepes (3) lett a dolgozat!")
elif szazalek >= 50:
    print("Elégséges (2) lett a dolgozat!")
else:
    print("Elégtelen (1) lett a dolgozat!")
    if szazalek < 10:
        print("Gratulálok a csodálatos teljesítményért!")

egesz = int(input("Adjon meg egy egész számot: "))
if egesz % 4 == 0:
    print(f"{egesz} osztható 4-gyel!")

valos = float(input("Adjon meg egy valós számot: "))
if valos > 120:
    print(f"{valos} nagyobb mint 120!")