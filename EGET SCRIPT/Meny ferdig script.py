from Funksjoner import høyest_ppg

while True:
    valg = input("""
MENYVALG FOR FANTASY SCRIPT:
                 
                 """)
    if valg.lower == "avslutt":
        break
    try:
        valg = int(valg)
    except ValueError:
        print("Tast inn et tall")
        continue

    if valg == 1:
        hppg = høyest_ppg()
        print(hppg)
    #elif valg == 2:
    
    #elif valg == 3:
    
    #elif valg == 4:

    #elif valg == 5:

    else:
        print("Tast inn et gyldig tall eller avslutt")
        continue

