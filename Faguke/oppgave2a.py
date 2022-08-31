import turtle
from tkinter import messagebox

Luthien = turtle.Turtle()  # legger til en skilpade med navn Luthien
Luthien.shape("arrow")  # Gjør så Luthien er en "arrow"
Luthien.speed(7)  # Endrer farten til Luthien

vindu = turtle.Screen()  # Navngir vinduet som popper op med grafisk informasjon

farge = vindu.textinput("farge", "Fill Colour:  ")  # definerer farge så brukeren kan velge farge til figuren
linje = vindu.textinput("linje", "Outside Colour:  ")  # definerer linjefarge så brukeren kan velge farge til figuren
sider = vindu.textinput("sider",
                        "Åssen figur vil du tegne: ")  # Definerer sider så når bruker skriver "Firkant" så er sider == firkant å en firkant blir tegnet.
lengde = int(vindu.numinput("lengde", "Hvor stor skal figuren være: "))

if sider == "firkant":  # Hvis sider er firkant så kjører koden
    Luthien.color(linje, farge)  # Setter fargene på figuren som bruker velger
    Luthien.begin_fill()  # Begynner å fylle figuren med fargen brukeren valgte
    for i in range(4):  # Gjør det under 4 / x antal ganger.
        Luthien.forward(lengde)  # Går fremover x antall pixler som bruker har definert
        Luthien.left(360 / 4)  # Går (360 / 4) 90 grader til venstre
    Luthien.end_fill()  # fyller figuren med farge brukeren har valgt
    messagebox.showinfo("Suksess",
                        "Du har tegnet en firkant!")  # en boks kommer opp med teksten "Suksess", "Du har tegnet en firkant!"
    exit()  # Slutter programmet når du trykker ok på melding boksen
elif sider == "trekant":  # Eller hvis sider er trekant kjør denne koden
    Luthien.color(linje, farge)
    Luthien.begin_fill()
    for i in range(3):
        Luthien.forward(lengde)
        Luthien.left(360 / 3)
    Luthien.end_fill()
    messagebox.showinfo("Suksess", "Du har tegnet en trekant!")
    exit()
elif sider == "femkant":  # Eller hvis sider er femkant...
    Luthien.color(linje, farge)
    Luthien.begin_fill()
    for i in range(5):
        Luthien.forward(lengde)
        Luthien.left(360 / 5)
    Luthien.end_fill()
    messagebox.showinfo("Suksess", "Du har tegnet en femkant!")
    exit()
elif sider == "sekskant":  # Hvis sider er sekskant...
    Luthien.color(linje, farge)
    Luthien.begin_fill()
    for i in range(6):
        Luthien.forward(lengde)
        Luthien.left(360 / 6)
    Luthien.end_fill()
    messagebox.showinfo("Suksess", "Du har tegnet en sekskant!")
    exit()
