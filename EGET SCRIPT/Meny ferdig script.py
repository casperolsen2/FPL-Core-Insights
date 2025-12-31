from Funksjoner import høyest_ppg, print_spiller
from Lese_Nyeste_GW import siste_stats_per_spiller

import pandas as pd

ps = pd.read_csv("data/2025-2026/playerstats.csv")
ps_clean = siste_stats_per_spiller(ps)

while True:
    valg = input("""
MENYVALG FOR FANTASY SCRIPT:
1: Høyeste PPG spiller
2: Topp 3 anbefalte kjøp
3: Sjekk stats til en spiller
""")
    
    if valg.lower() == "avslutt":
        print(f"Avslutter programmet.")
        break
    
    try:
        valg = int(valg)
    except ValueError:
        print("Tast inn et tall")
        continue

    if valg == 1:
        hppg = høyest_ppg(ps_clean)
        print(f'Navn: {hppg['web_name']}, {hppg['first_name']}')
        print(f'Totale poeng: {hppg['total_points']}')
        print(f'Pris: {hppg['now_cost']}m')
    
    #elif valg == 2:
    
    elif valg == 3:
        while True:
            spiller = input("""Skriv inn etternavn på spilleren (fornavn hvis ønskelig)
""")
            print()
            spiller = spiller.split(" ")
            if len(spiller) == 1:
                etternavn = spiller[0].lower().strip()
                fornavn = None
            else:
                fornavn = spiller[0].lower().strip()
                etternavn = spiller[1].lower().strip()
            print(print_spiller(ps_clean, etternavn, fornavn))
            print()
            fortsette = input("Vil du søke på en til spiller? Ja/Nei: ")
            if fortsette.lower() == "ja":
                print()
                continue
            else:
                print()
                break
        
    #elif valg == 4:

    #elif valg == 5:

    else:
        print("Tast inn et gyldig tall eller avslutt")
        continue

