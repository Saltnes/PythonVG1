from random import randint

sant = 1  # Setter sant til 1 så while løken kjøres + kjøres igjen når du trykker 1
runde = 1  # Setter runde til 1 så man begynner på runde 1
print("Hei! Velkommen til terningkast spill!")
while (sant == 1):
    print("***RUNDE " + str(runde) + "***")  # Skriver ***RUNDE+ hvem runde det er + ***
    print("Spiller 1: ", randint(1, 20))  # Velger et random nr mellom 1 og 20 for spiller 1
    print("Spiller 2: ", randint(1, 20))  # Velger et random nr mellom 1 og 20 for spiller 2
    sant = int(input(
        "Trykk 1 for å kjøre igjen, 0 for å stoppe: "))  # Gjør sant variablen til inputen til brukeren 1 gjør så while løkken kjøres på nytt
    runde += 1  # Øker runde med 1 vær gang løkken kjøres
