import os
import math

def clear():
    os.system('cls')

def skriv_meny():
    print("\nHovedmeny for beregning av areal\n")
    print("1. Beregn areal for kvadrat")
    print("2. Beregn areal for rektangel")
    print("3. Beregn areal for trekant")
    print("4. Beregn areal for parallellogram")
    print("5. Beregn areal for rombe")
    print("6. Beregn areal for trapes")
    print("7. Beregn areal for sirkel")
    print("8. Avslutt")

def read_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Verdien må være større enn 0. Prøv igjen.")
                continue
            return val
        except ValueError:
            print("Ugyldig tall. Oppgi et tall (f.eks. 3.5).")


def area_kvadrat(s):
    return s * s


def area_rektangel(g, h):
    return g * h


def area_trekant(g, h):
    return 0.5 * g * h


def area_parallellogram(g, h):
    return g * h


def area_rombe(d1, d2):
    return 0.5 * d1 * d2


def area_trapes(a, b, h):
    return 0.5 * (a + b) * h


def area_sirkel(r):
    return math.pi * (r ** 2)


ans = "Start"
while ans != "8":
    clear()
    skriv_meny()

    ans = input("Hva ønsker du å gjøre. Velg tall? ")
    if ans == "1":
        clear()
        print("\nBeregning av arealet av et kvadrat")
        s = read_positive_float("Oppgi side (s): ")
        print(f"Areal kvadrat = {area_kvadrat(s):.4f}")
        input("Trykk ENTER for å fortsette...")
    elif ans == "2":
        clear()
        print("\nBeregning av arealet av et rektangel")
        g = read_positive_float("Oppgi grunnlinje (g): ")
        h = read_positive_float("Oppgi høyde (h): ")
        print(f"Areal rektangel = {area_rektangel(g, h):.4f}")
        input("Trykk ENTER for å fortsette...")
    elif ans == "3":
        clear()
        print("\nBeregning av arealet av en trekant")
        g = read_positive_float("Oppgi grunnlinje (g): ")
        h = read_positive_float("Oppgi høyde (h): ")
        print(f"Areal trekant = {area_trekant(g, h):.4f}")
        input("Trykk ENTER for å fortsette...")
    elif ans == "4":
        clear()
        print("\nBeregning av arealet av et parallellogram")
        g = read_positive_float("Oppgi grunnlinje (g): ")
        h = read_positive_float("Oppgi høyde (h): ")
        print(f"Areal parallellogram = {area_parallellogram(g, h):.4f}")
        input("Trykk ENTER for å fortsette...")
    elif ans == "5":
        clear()
        print("\nBeregning av arealet av en rombe")
        d1 = read_positive_float("Oppgi diagonal 1: ")
        d2 = read_positive_float("Oppgi diagonal 2: ")
        print(f"Areal rombe = {area_rombe(d1, d2):.4f}")
        input("Trykk ENTER for å fortsette...")
    elif ans == "6":
        clear()
        print("\nBeregning av arealet av en trapes")
        a = read_positive_float("Oppgi lengde av side a: ")
        b = read_positive_float("Oppgi lengde av side b: ")
        h = read_positive_float("Oppgi høyde (h): ")
        print(f"Areal trapes = {area_trapes(a, b, h):.4f}")
        input("Trykk ENTER for å fortsette...")
    elif ans == "7":
        clear()
        print("\nBeregning av arealet av en sirkel")
        r = read_positive_float("Oppgi radius (r): ")
        print(f"Areal sirkel = {area_sirkel(r):.4f}")
        input("Trykk ENTER for å fortsette...")

print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")

