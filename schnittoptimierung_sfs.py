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

lagerlaenge = int(input("Bitte geben Sie die Lagerlänge ein: "))
schleife = 0
while schleife == 0:
    try:
        schnittlaengen_eingabe = input(
            "Bitte geben Sie die Schnittlängen ein (z.B. '3*400' für 3 Zuschnitte mit einer Länge von 400 mm): ")
        schnittlaengen = []
        for eintrag in schnittlaengen_eingabe.split():
            if '*' in eintrag:
                anzahl, laenge = map(int, eintrag.split('*'))
                schnittlaengen.extend([laenge] * anzahl)
            else:
                schnittlaengen.append(int(eintrag))

        anzahl_stangen, restlaengen, einteilung = schnittoptimierung(lagerlaenge, schnittlaengen)
        print(f"Ihre eingegebenen Schnittlängen:\n{schnittlaengen_eingabe}\n")
        print("Anzahl der benötigten Stangen:", anzahl_stangen)
        print(f"Restlängen: {restlaengen_ausgabe(restlaengen)}\n")

        gesamtlaenge = anzahl_stangen * lagerlaenge
        rest_in_prozent = sum(restlaengen) / gesamtlaenge * 100
        print(f"Restlängen in Prozent zur Gesamtlänge: {rest_in_prozent:.2f}%\n")

        print("Einteilung der Zuschnitte auf die Stangen:")
        for i, brett_einteilung in enumerate(einteilung):
            print(f"Stange {i + 1}: {brett_einteilung}")
            schleife += 1


    except ValueError:
        a = input(("Bitte geben Sie die Schnittlängen im Format: 2*300 ( Kein Leerzeichen beim *) mit \"enter\" bestätigen"))
