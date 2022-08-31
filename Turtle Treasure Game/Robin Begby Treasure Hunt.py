import turtle
import random
from tkinter import messagebox
from playsound import playsound

# importerer forskjellige biblioteker så vi kan bruke dem i programmet våres.

vindu = turtle.Screen()
vindu.bgpic("kart.gif") # setter bakgrunn bildet
vindu.setup(1000, 669) # setter størrelsen på vinduet
vindu.title("Desolation of The Shire") # setter en titel på vinduet

turtle.register_shape("freddy.gif")  # registrerer bilde filen jeg laget i photoshop så vi kan bruke den til  skilpadden
turtle.register_shape("fire.gif")
turtle.register_shape("enemy.gif")

freddy = turtle.Turtle()  # lager skillpaden som er spilleren.
freddy.shape("freddy.gif")  # endrer åssen skilpadden ser ut
freddy.hideturtle()
freddy.penup()
freddy.setposition(200, -100)  # setter skilpadden på kordinatene git
freddy.pendown()
freddy.showturtle()

skatt = turtle.Turtle()  # lager skillpaden som fungerer som "skatten"
skatt.shape("fire.gif")
skatt.hideturtle()  # hider "skatten" så du ikke ser den teleporterer seg
skatt.penup()  # gjør så skatten ikke lager en tegne strek.
skatt.setpos(-200, 130)
skatt.showturtle()  # viser den igjen etter den har tp'a

enemy = turtle.Turtle()  # lager skillpaden som er fienden
enemy.shape("enemy.gif")
enemy.hideturtle()
enemy.penup()
enemy.speed(1)
enemy.setpos(-300, 100)
enemy.showturtle()

enemy2 = turtle.Turtle()  # lager skillpaden som er fienden
enemy2.shape("enemy.gif")
enemy2.hideturtle()
enemy2.penup()
enemy2.speed(1)
enemy2.setpos(-100, -50)
enemy2.showturtle()

freddy.speed(1)
speed = 1
fortsette = 1  # setter variablen fortsette til 1, som gjør at koden i while løken kjøres.


def travel():  # Gjør så skillpdaden går fremover automatisk og hvor fort / mye
    freddy.forward(speed)
    vindu.ontimer(travel, 10)


def collide():  # Gjør så du "dør" når du kommer nærme fiendene
    avstand_til_enemy = freddy.distance(enemy)
    second_enemy = freddy.distance(enemy2)

    if second_enemy <= 50:  # når enemy er nærmere eller er 50 pixels unna spilleren så kjører koden nedenfor
        playsound("death.mp3")  # Spiller en lydfil jeg har laget når spilleren "dør"
        messagebox.showinfo("The Light Prevails", "You've been slain")  # en melding kommer opp når du "dør"
        exit()

    if avstand_til_enemy <= 50:
        playsound("winnn.mp3")
        messagebox.showinfo("The Light Prevails", "You've been slain")

        global fortsette
        fortsette = 0
        exit()


def search():  # Når du kommer nærme "skatten" så vinner du
    avstand_til_skatt = freddy.distance(skatt)

    if avstand_til_skatt <= 50:  # når spilleren er 50 pixels eller nærmere spill koden under.
        playsound("winnn.mp3")  # spiller en lydfil når du vinner
        messagebox.showinfo("Victory", "You burnt The Shire")  # Viser en melding når du vinner.

        global fortsette
        fortsette = 0
        exit()

    # Setter åssen du beveger spilleren gjorde det lit anderledes en det som var på oppgaven, den går fremover automatisk.


vindu.onkey(lambda: freddy.setheading(90), 'Up')
vindu.onkey(lambda: freddy.setheading(180), 'Left')
vindu.onkey(lambda: freddy.setheading(0), 'Right')
vindu.onkey(lambda: freddy.setheading(270), 'Down')

vindu.listen()  # Gjør så vindu lytter etter inputs
travel()

# føler nesten ut som det er noen problemer med åssen løkken kjører eller hvor ofte den kjører siden noen ganger
# fungerer det helt fint men andre ganger beveger fiendene seg veldig sent og det registrerer seg ikke helt når du er nærme dem
# er det fordi det er for mye i løken? men spillet føles lit "laggy" ut pga dette.
# pga dette tror jeg det hade vært meget iriterende med et poeng system siden du måte ha gåt over skaten flere ganger hvis spillet
# lagger som det gjør noen ganger. er ikke sikker om dette er noe med turtle eller hva det er.

while (fortsette == 1):  # når fortsetter er 1 kjører et noen functions, gjør også at fiendene beveger seg.
    collide()  # kjører collide function når fortestte = 1
    search()  # kjører search funtion når fortestte = 1
    lengde = random.randint(10, 40)  # gjør så fienden går 10 - 40 pixels når løkken kjøres.
    enemy.forward(lengde)  # fienden går fremover når løken kjøres
    enemy2.forward(
        lengde * 1.25)  # fienden går fremover nå løken kjøres, men valgte å endre hvor langt han gikk så det ikke bled helt likt

    vinkel = random.randint(0, 360)  # gjør så vinkel er noe "random" melom 0 og 360 grader
    enemy.left(vinkel)  # enemy
    enemy2.left(vinkel * 1.25)

vindu.mainloop()
vindu.exitonclick()
