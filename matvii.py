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

print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")

