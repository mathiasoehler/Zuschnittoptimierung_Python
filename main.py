import pandas as pd


def schnittoptimierung(lagerlaenge, schnittlaengen):
    schnittlaengen.sort(reverse=True)
    anzahl_bretter = 0
    restlaengen = []
    einteilung = []
    while len(schnittlaengen) > 0:
        anzahl_bretter += 1
        verbleibende_laenge = lagerlaenge
        i = 0
        brett_einteilung = []
        while i < len(schnittlaengen):
            if schnittlaengen[i] <= verbleibende_laenge:
                verbleibende_laenge -= schnittlaengen[i]
                brett_einteilung.append(schnittlaengen.pop(i))
            else:
                i += 1
        restlaengen.append(verbleibende_laenge)
        einteilung.append(brett_einteilung)
    return anzahl_bretter, restlaengen, einteilung


def restlaengen_ausgabe(restlaengen):
    rest_dict = {}
    for rest in restlaengen:
        if rest in rest_dict:
            rest_dict[rest] += 1
        else:
            rest_dict[rest] = 1
    ausgabe = []
    for rest, anzahl in rest_dict.items():
        if anzahl > 1:
            ausgabe.append(f"{anzahl} * {rest}")
        else:
            ausgabe.append(str(rest))
    return ', '.join(ausgabe)


def schnittlaengen_einlesen():
    # Frage den Benutzer, ob er die Schnittlängen aus einer Excel-Datei einlesen oder manuell eingeben möchte
    einlese_option = input(
        "Möchtest du die Schnittlängen aus einer Excel-Datei einlesen (E) oder manuell eingeben (M)? ")
    if einlese_option.upper() == 'E':
        # Lese die Schnittlängen aus einer Excel-Datei ein
        dateipfad = input("Bitte gib den Pfad zur Excel-Datei an: ")
        df = pd.read_excel(dateipfad)

        # Konvertiere die Daten in eine Liste von Schnittlängen
        schnittlaengen = []
        for _, row in df.iterrows():
            anzahl = int(row['stk'])
            laenge = row['laenge']
            schnittlaengen.extend([laenge] * anzahl)
    else:
        # Lese die Schnittlängen manuell ein
        schnittlaengen_eingabe = input(
            "Bitte gib die Schnittlängen ein (z.B. '3 * 400' für 3 Zuschnitte mit einer Länge von 400 mm): ")
        schnittlaengen = []
        for eintrag in schnittlaengen_eingabe.split():
            if '*' in eintrag:
                anzahl, laenge = map(int, eintrag.split('*'))
                schnittlaengen.extend([laenge] * anzahl)
            else:
                schnittlaengen.append(int(eintrag))
    return schnittlaengen


# Führe die Schnittoptimierung durch
lagerlaenge = int(input("Bitte gib die Lagerlänge ein: "))
schnittlaengen = schnittlaengen_einlesen()
anzahl_stangen, restlaengen, einteilung = schnittoptimierung(lagerlaenge, schnittlaengen)

# Gebe die Ergebnisse aus
print("Anzahl der benötigten Stangen:", anzahl_stangen)
print("Restlängen:", restlaengen_ausgabe(restlaengen))

gesamtlaenge = anzahl_stangen * lagerlaenge
rest_in_prozent = sum(restlaengen) / gesamtlaenge * 100
print(f"Restlängen in Prozent zur Gesamtlänge: {rest_in_prozent:.2f}%")

print("Einteilung der Zuschnitte auf die Stangen:")
for i, brett_einteilung in enumerate(einteilung):
    print(f"Stange {i + 1}: {brett_einteilung}")
