adjektiv1 = ""
adjektiv2 = ""
adjektiv3 = ""
adjektiv4 = ""
adjektiv5 = ""


def velkommen():
    print("^^^^^^Velkommen^^^^^^")
    print("^^^^^^^^^^Til^^^^^^^^^")
    print("^^Adjektivfortelling^^")


def skrivinn():
    global adjektiv1
    global adjektiv2
    global adjektiv3
    global adjektiv4
    global adjektiv5
    adjektiv1 = input("Skriv inn et adjektiv: ")
    adjektiv2 = input("Skriv inn et adjektiv: ")
    adjektiv3 = input("Skriv inn et adjektiv: ")
    adjektiv4 = input("Skriv inn et adjektiv: ")
    adjektiv5 = input("Skriv inn et adjektiv: ")


def printut():
    print("Du hoppa over en boks som var " + adjektiv1)
    print("I den boksen var det en " + adjektiv2 + " pingvin")
    print("Den pingvinen løpte mot et " + adjektiv3 + " hav")
    print("I havet er den en " + adjektiv4 + " sel")
    print("som vill spise den " + adjektiv2 + "e pingvinen men pingvinen dreper den " + adjektiv4 +
          "e selen med sit " + adjektiv5 + "e bekk")


def avslutt():
    a = input("GAME OVER. Trykk en tast for å avslutte.")
    exit()


velkommen()
skrivinn()
printut()
avslutt()
