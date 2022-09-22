# Importerer bibliotek / moduler
import turtle
from tkinter import *
from tkinter import messagebox

Luthien = turtle.Turtle()  # legger til en skilpade med navn Luthien
Luthien.shape("arrow")  # Gjør så Luthien er en "arrow"
Luthien.speed(7)  # Endre farten til Luthien

vindu = turtle.Screen()  # Navngir vinduet som popper op med grafisk informasjon

master = Tk()  # Lager meny objektet
master.geometry("300x300")  # setter størrelsen på drop down meny boksen
master.title("Velg Figur")  # Setter titelen på meny vinduet
sider = StringVar(master)  # Datatype av meny teksten
sider.set("Trekant")  # Default meny teksten / option
# Lager drop down menyen å legger til "options" du kan trykke på
option = OptionMenu(master, sider, "Trekant", "Firkant", "Femkant", "Sekskant")
option.pack()

#lager ok funktionen
def ok():
    print("Figur: "), sider.get()
    master.quit()  # lukker menyen


button = Button(master, text="Ok",
                command=ok)  # Ok / valg knappen for menyen kjører ok funktionen når knappen blir trykket på
button.pack()

mainloop()  # Kjører tkinter

lengde = int(vindu.numinput("lengde", "Størrelse: "))
farge = vindu.textinput("farge", "Fill Colour (English):  ")  # definerer farge så brukeren kan velge farge til figuren
linje = vindu.textinput("linje",
                        "Outside Colour(English):  ")  # definerer linjefarge så brukeren kan velge farge til figuren

if sider == "Firkant":  # Hvis sider er firkant så kjører koden
    Luthien.color(linje, farge)  # Setter fargene på figuren som bruker velger
    Luthien.begin_fill()  # Begynner å fylle figuren med fargen brukeren valgte
    for i in range(4):  # Gjør det under 4 / x antal ganger.
        Luthien.forward(lengde)  # Går fremover x antall pixler som bruker har definert
        Luthien.left(360 / 4)  # Går (360 / 4) 90 grader til venstre
    Luthien.end_fill()  # fyller figuren med farge brukeren har valgt
    messagebox.showinfo("Suksess",
                        "Du har tegnet en firkant!")  # en boks kommer opp med teksten "Suksess", "Du har tegnet en firkant!"
    exit()  # Slutter programmet når du trykker ok på melding boksen
elif sider == "Trekant":  # Eller hvis sider er trekant kjør denne koden
    Luthien.color(linje, farge)
    Luthien.begin_fill()
    for i in range(3):
        Luthien.forward(lengde)
        Luthien.left(360 / 3)
    Luthien.end_fill()
    messagebox.showinfo("Suksess", "Du har tegnet en trekant!")
    exit()
elif sider == "Femkant":  # Eller hvis sider er femkant...
    Luthien.color(linje, farge)
    Luthien.begin_fill()
    for i in range(5):
        Luthien.forward(lengde)
        Luthien.left(360 / 5)
    Luthien.end_fill()
    messagebox.showinfo("Suksess", "Du har tegnet en femkant!")
    exit()
elif sider == "Sekskant":  # Hvis sider er sekskant...
    Luthien.color(linje, farge)
    Luthien.begin_fill()
    for i in range(6):
        Luthien.forward(lengde)
        Luthien.left(360 / 6)
    Luthien.end_fill()
    messagebox.showinfo("Suksess", "Du har tegnet en sekskant!")
    exit()
