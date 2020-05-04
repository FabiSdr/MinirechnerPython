#Minirechner-Projekt in Python
#Erstellt von Sieder Fabian

Zahl1 = int(input("Zahl1: "))
Zahl2 = int(input("Zahl2: "))

def Add(Zahl1, Zahl2):
    return Zahl1 + Zahl2

def Sub(Zahl1, Zahl2):
    return Zahl1 - Zahl2

def Mul(Zahl1, Zahl2):
    return Zahl1 * Zahl2

def Div(Zahl1, Zahl2):
    return Zahl1 / Zahl2

print("Zahl1 + Zahl2 = " + str(Add(Zahl1,Zahl2)))
print("Zahl1 - Zahl2 = " + str(Sub(Zahl1,Zahl2)))
print("Zahl1 * Zahl2 = " + str(Mul(Zahl1,Zahl2)))
print("Zahl1 / Zahl2 = " + str(Div(Zahl1,Zahl2)))
