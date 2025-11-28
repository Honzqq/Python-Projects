def scitani(a,b):
    return a + b

def odcitani(a,b):
    return a - b

def nasobeni(a,b):
    return a * b

def deleni(a,b):
    if a == 0 or b == 0:
        return "Chyba: Nulou nelze dělit"
    return a / b

a = int(input("Zadej první číslo: "))
b = int(input("Zadej první číslo: "))
operace = input("Zadej známenko pro operaci(+,-,*,/): ")

if operace == "+":
    print(f"Výsledek sčítání je: {scitani(a,b)}")
elif operace == "-":
    print(f"Výsledek odčítání je: {odcitani(a,b)}")
elif operace == "*":
    print(f"Výsledek násobení je: {nasobeni(a,b)}")
elif operace == "/":
    print(f"Výsledek dělení je: {deleni(a,b)}")
else:
    print("Chyba: Musíš zadat znaménko")