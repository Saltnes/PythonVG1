# Importerer bibliotek / moduler
import turtle
from random import randint
from tkinter import *
from tkinter import messagebox

Luthien = turtle.Turtle()  # legger til en skilpade med navn Luthien
Luthien.shape("arrow")  # Gjør så Luthien er en "arrow"
Luthien.speed(5)  # Endre farten til Luthien
Luthien.pensize(3)  # Setter strørrelsen på linjen rundt figuren
vindu = turtle.Screen()  # Navngir vinduet som popper op med grafisk informasjon

master = Tk()  # Lager meny objektet
master.geometry("250x100")  # setter størrelsen på drop down meny boksen
master.title("Velg Figur")  # Setter titelen på meny vinduet
var = StringVar(master)  # Datatype av meny teksten
var.set("Trekant")  # Default meny teksten / option
# Lager drop down menyen å legger til "options" du kan trykke på
option = OptionMenu(master, var, "Trekant", "Firkant", "Femkant", "Sekskant", "Kunst")
option.pack()


# lager ok funktionen
def ok():
    global var  # Gjør var en global variabel
    var = var.get()  # Setter var variablen til det brukeren velger i menyen
    master.quit()  # lukker menyen


button = Button(master, text="Ok",
                command=ok)  # Ok / valg knappen for menyen kjører ok funktionen når knappen blir trykket på
button.pack()
mainloop()  # Kjører tkinter

lengde = int(vindu.numinput("lengde", "Størrelse(px): "))
farge = vindu.textinput("farge", "Fill Colour (English):  ")  # definerer farge så brukeren kan velge farge til figuren
linje = vindu.textinput("linje",
                        "Outside Colour(English):  ")  # definerer linjefarge så brukeren kan velge farge til figuren
Luthien.color(linje, farge)  # setter fargen på linjen rundt figuren å fyll fargen

if var == "Firkant":  # Hvis var = firkant så kjører koden
    Luthien.begin_fill()  # Begynner å fylle figuren med fargen brukeren valgte
    for i in range(4):  # Gjør det under 4 / x antal ganger.
        Luthien.forward(lengde)  # Går fremover x antall pixler som bruker har definert
        Luthien.left(360 / 4)  # Går (360 / 4) 90 grader til venstre
    Luthien.end_fill()  # fyller figuren med farge brukeren har valgt
    messagebox.showinfo("Success!",
                        "Du har tegnet en firkant!")  # en boks kommer opp med teksten "Success!", "Du har tegnet en firkant!"
    exit()  # Slutter programmet når du trykker ok på melding boksen
elif var == "Trekant":  # Eller hvis var er trekant kjør denne koden
    Luthien.begin_fill()
    for i in range(3):
        Luthien.forward(lengde)
        Luthien.left(360 / 3)
    Luthien.end_fill()
    messagebox.showinfo("Success!", "Du har tegnet en trekant!")
    exit()
elif var == "Femkant":  # Eller hvis var er femkant...
    Luthien.begin_fill()
    for i in range(5):
        Luthien.forward(lengde)
        Luthien.left(360 / 5)
    Luthien.end_fill()
    messagebox.showinfo("Success!", "Du har tegnet en femkant!")
    exit()
elif var == "Sekskant":  # Hvis var er sekskant...
    Luthien.begin_fill()
    for i in range(6):
        Luthien.forward(lengde)
        Luthien.left(360 / 6)
    Luthien.end_fill()
    messagebox.showinfo("Success!", "Du har tegnet en sekskant!")
    exit()
elif var == "Kunst":
    for loop in range(4):
        Luthien.pensize(10)
        Luthien.begin_fill()
        for i in range(4):
            Luthien.forward(lengde)
            Luthien.left(90)
        Luthien.end_fill()
        Luthien.left(90)
        Luthien.penup()
        Luthien.forward(100)
        Luthien.pendown()
    messagebox.showinfo("Success!", "Du har tegnet noe kunst!")
    exit()
