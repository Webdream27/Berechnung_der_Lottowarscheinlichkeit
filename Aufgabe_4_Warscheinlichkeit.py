import math

# Die Zahlen für Lotto "6 aus 49"
n = 49 # Gesamtzahl der Kugeln
k = 6  # Anzahl der zu ziehenden Kugeln

# Die Anzahl aller möglichen Kombinationen berechnen
anzahl_kombinationen = math.comb(n, k)

# Die Gewinnwahrscheinlichkeit ist 1 geteilt durch die Gesamtzahl der Kombinationen
wahrscheinlichkeit = 1 / anzahl_kombinationen

# Das Ergebnis ausgeben
print(f"Die Anzahl der möglichen Kombinationen bei '6 aus 49' ist: {anzahl_kombinationen}")
print(f"Die Wahrscheinlichkeit zu gewinnen beträgt 1 zu {anzahl_kombinationen}.")
print(f"Das entspricht: {wahrscheinlichkeit}")

