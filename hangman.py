#Gemaakt door Luuk Noverraz

import random
import time
import math

ok = []
def printTussenstand():
    pass

fout = 0 
#variabele waarin staat hoevaak je het fout geraden hebt
#5 ifs voor de galg

def printGalgje():
    pass

ggl = ""
#"goed geraden lijst" voor alle letters goed geraden door de speler

lijst = ["strijder", "humanisme", "communisme", "zimbabwe", "sinaasappel", "ananas", "dimensie", "nebula", "beeldscherm", "bilderdijkstraat", "luidspreker", "andromeda"]
#de lijst met woorden waaruit gekozen kan worden

geheimwoord = random.choice(lijst)
#het geheime woord dat uit de lijst gekozen wordt

#Als geheimwoord zelf bepaald mag worden :
#geheimwoord = input("Typ hier het geheime woord in: ")

jorg = len(geheimwoord)
#Jorg is de lengte van het geheime woord

for i in range(jorg):
  ok.append("_")

print("Welkom bij Galgje! Als je wilt stoppen, typ dan QQ.")
while True:
    if fout == 1:
        print("                  ")
        print("                  ")
        print("                  ")
        print("                  ")
        print("                  ")
        print("                  ")
        print("     ___          ")
        print("                  ")        
    if fout == 2:
        print("                  ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
    if fout == 3:
        print("     _________    ")
        print("    |/            ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
    if fout == 4:
        print("     _________    ")
        print("    |/        |   ")
        print("    |         0   ")
        print("    |         |   ")
        print("    |             ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
    if fout == 5:
        print("     _________    ")
        print("    |/        |   ")
        print("    |         0   ")
        print("    |        /|\  ")
        print("    |        / \  ")
        print("    |             ")
        print("    |___          ")
        print("                  ")
        print("")
        print("Je bent gestorven.")
        time.sleep(2)
        break
    
    for i in range(jorg):
        print (ok[i], end=" ")
    print("")
    kies = input("Kies een letter of kies ? om het geheime woord te raden. ")
    if kies.upper() not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "?"]:
        time.sleep(2)
        print("")
        print("Kies alstjeblieft een letter uit het alfabet. (Je krijgt nu een strafpunt)")
        time.sleep(2.5)
    if kies == "?":
        time.sleep(1.5)
        raad = input("Ok, typ hier in wat je denkt dat het woord is : ")
        if raad == geheimwoord:
            time.sleep(2)
            print("")
            print("Gefeliciteerd, je hebt gewonnen! Het woord was inderdaad " + raad + "!")
            time.sleep(1)
            print("")
            print("Het programma sluit af in 10 seconden.")
            time.sleep(10)
            break
        elif raad != geheimwoord:
            time.sleep(2)
            print("Helaas! Je heb het woord fout geraden, en je krijgt nu een strafpunt.")
    if kies.upper() == "QQ":
        time.sleep(0.5)
        print("Oh.")
        time.sleep(1)
        print("Ok.")
        time.sleep(1)
        print("Vaarwel. :(")
        time.sleep(1.5)
        break
    lettergoed = False
    for i in range(jorg):
        if kies == geheimwoord[i]:
            lettergoed = True
            ok[i] = kies
            print("")
            print("Goed geraden! Koop trouwens een aflaat.")
            ggl = ggl + kies
    if not lettergoed:
        fout = fout + 1
        print("")
        print("Jammer. But dont forget to enter my free gift card giveaway.")
        print("")
        time.sleep(0.5)
        print("Deze heb je al geraden: ", ggl)
    if ok == ['a', 'n', 'd', 'r', 'o', 'm', 'e', 'd', 'a'] or ok == ['h', 'u', 'm', 'a', 'n', 'i', 's', 'm', 'e'] or ok == ['c', 'o', 'm', 'm', 'u', 'n', 'i', 's', 'm', 'e'] or ok == ['l', 'u', 'i', 'd', 's', 'p', 'r', 'e', 'k', 'e', 'r'] or ok == ['a', 'n', 'a', 'n', 'a', 's'] or ok == ['d', 'i', 'm', 'e', 'n', 's', 'i', 'e'] or ok == ['b', 'i', 'l', 'd', 'e', 'r', 'd', 'i', 'j', 'k', 's', 't', 'r', 'a', 'a', 't'] or ok == ['z', 'i', 'm', 'b', 'a', 'b', 'w', 'e'] or ok == ['b', 'e', 'e', 'l', 'd', 's', 'c', 'h', 'e', 'r', 'm'] or ok == ['n', 'e', 'b', 'u', 'l', 'a'] or ok == ['s', 't', 'r', 'i', 'j', 'd', 'e', 'r'] or ok == ['s', 'i', 'n', 'a', 'a', 's', 'a', 'p', 'p', 'e', 'l']:
        time.sleep(1)
        print("")
        print("Gefeliciteerd, je hebt gewonnen! Het programma sluit af in 10 seconden.")
        time.sleep(10)
        break
 
         
         
