#Guðmundur Brimir Björnsson
#Uppsetning hafinn 5. febrúar, 2019
import random
import math

def greinaskil():
    print("===========")

#Föll fyrir verkefni 1 - Farenheit og Celsíus
#Celsíus í Farenheit
def Fahrenheit(cel): #Fallið tekur inn breytu og kallar hana cel. Hún á að vera hitastig í Celsíus
    return(cel*1.8+32) #Fallið skilar hve mikið Celsíus breytan cel er
#Celsíus er breytt í Farenheit
def Celsius(faren): #Fallið tekur inn breytu og kallar hana faren. Hún á að vera hitastig í Farenheit.
    return((faren-32)/1.8) #Fallið skilar hve mikið Farenheit breytan faren er

#Föll fyrir verkefni 2 - Kelvin og Celsíus
#Kelvin er breytt í Celsíus
def Kelvin(cel): #Fallið tekur inn breytu og kallar hana cel. Hún á að vera hitastig í Celsíus.
    return(cel + 273.15) #Fallið skila hve mikið Kelvin breytan cel er.
#Celsíus er breytt í Kelvin
def CelsiusKelvin(kel): #Fallið tekur inn breytu og kallar hana kel. Hún á að vera hitastig í Kelvin.
    return(kel - 273.15)#Fallið skila hve mikið Celsíus breytan kel er.

#Fall fyrir verkefni 3 - Veldareikningur
def reiknaVeldi(tala, veldi): #Þetta fall tekur inn tvær tölur, annað er veldi og hitt er tala.
    return(math.pow(tala, veldi)) #Síðan er notað fall sem veldar tölur. tala fer í sæti tölu og veldi fer í sæti veldis

#Föll fyrir verkefni 4 - Tommur og Sentimetrar
#Tommur er breytt í Sentimetra
def tm_cm(tm): #Fallið tekur inn breytu og kallar hana tm. Hún á að vera lengd í Tommum.
    return(tm*2.54) #Fallið skilar hve margir Sentimetrar breytan tm er.
#Sentimetrar eru breyttir í Tommur
def cm_tm(cm): #Fallið tekur inn breytu og kallar hana cm. Hún á að vera lengd í Sentimetrum.
    return(cm/2.54) #Fallið skilar hve margar Tommur breytan cm er.

#Föll fyrir verkefni 5 - Gallon og Lítrar
#Gallon í Lítra
def gallon_litrar(gallon): #Fallið tekur inn breytu og kallar hana gallon. Hún á að vera magn í Gallon.
    return(gallon*3.785) #Fallið skilar hve margir Lítrar breytan gallon er.
#Lítrar í Gallon
def litrar_gallon(litrar): #Fallið tekur inn breytu og kallar hana litrar. Hún á að vera magn í Lítrum.
    return(litrar/3.785)#Fallið skilar hve margar gallonur breytan litrar er.

#Fall fyrir verkefni 6 - Kveðja
def kvedja(nafn, kyn): #Fallið tekur inn nafn og kyn. Nafn breytan verður notuð fyrir nafn notanda. Kyn verður kyn notanda.
    if(kyn == "kvk"): #Gáð er hvort að notandi sé kvenkyns.
        print("Sæl og blessuð", nafn) #Kvenkyns kveðja.
    elif(kyn == "kk"): #Gáð er hvort að notandi sé karlkyns.
        print("Sæll og blessaður", nafn) #Karlkyns kveðja.

#Fall fyrir verkefni 7 - Teningakast
def kasta(): #Þetta fall tekur engar færibreytur
    print("Þú fékkst töluna", random.randint(1, 7)) #Prentað er út handahófskennd tala.

#Fall fyrir verkefni 8 - Sömu tölur í lista?
def SamaILista(list1, list2): #Þetta fall tekur inn tvo lista sem hver um sig munu heita list1, list2
    listi3 = []
    for x in list1: #Þessi for slaufa fer í gegnum lista 1 og breytan x tekur á sig það gildi.
        for y in list2: #Síðan fer þessi for slaufa í gegnum lista 2 og ber allar tölurnar þar saman við x breytuna.
            if(y == x): #Síðan ef að samsvörun er fundinn þá er bætt við lista 3 og slaufan brotinn.
                listi3.append(y)
    return(listi3) #Listi3 er loks returnað.

verkefni = ["Celsíus, Farenheit", "Celsíus, Kelvin", "Veldisreikningur", "Tommur, Sentimetrar", "Lítrar, Gallon", "Kveðja", "Teningakast", "Listar", "Hætta"]

while(True):
    for x, y in enumerate(verkefni):
        print(str(x+1)+".", y)
    val = input("Hvaða verkefni viltu skoða? : ")
    greinaskil()

    #Dæmi 1 - Celsíus, Farenheit
    if(val == "1"):
        print("1. Celsíus í Fahrenheit")
        print("2. Fahrenheit í Celsíus")
        maelieining = input("Hvað aðgerð á talvan að gera? : ")
        hiti = float(input("Hvað er hitinn mikill? : "))

        if(maelieining == "1"): #Celsíus í Fahrenheit
            print(hiti, "c° er", Fahrenheit(hiti), "°f")
        elif(maelieining == "2"): #Fahrenheit í Celsíus
            print(hiti, "°f er", Celsius(hiti), "c°")

    #Dæmi 2 - Celsíus, Kelvin
    elif(val == "2"):
        print("1. Celsíus í Kelvin")
        print("2. Kelvin í Celsíus")
        maelieining = input("Hvað aðgerð á talvan að gera? : ")
        hiti = float(input("Hvað er hitinn mikill? : "))

        if(maelieining == "1"): #Celsíus í Kelvin
            print(hiti, "k er", Kelvin(hiti), "c°")
        elif(maelieining == "2"): #Kelvin í Celsíus
            print(hiti, "c° er", CelsiusKelvin(hiti), "k")

    #Dæmi 3 - Veldisreikningur
    elif(val == "3"):
        tala1 = float(input("Hvaða tala á að vera reiknuð með veldi? : "))
        tala2 = float(input("Hvert er veldið? : "))

        print(tala1, "í veldi", tala2, "er", reiknaVeldi(tala1, tala2))

    #Dæmi 4 - Tommur, Sentimetrar
    elif(val == "4"):
        print("1. Tommur í Sentimetra.")
        print("2. Sentimetrar í Tommu")
        maelieining = input("Hvað viltu gera? : ")
        lengd = float(input("Lengd: "))

        if(maelieining == "1"): #Tommur í Sentimetra
            print(lengd, "tm eru", tm_cm(lengd), "cm")
        elif(maelieining == "2"): #Sentimetrar í Tommur
            print(lengd, "cm eru", cm_tm(lengd), "tm")

    #Dæmi 5 - Gallon, Lítrar
    elif(val == "5"):
        print("1. Gallon í lítra.")
        print("2. Lítrar í Gallon")
        maelieining = input("Hvað viltu gera? : ")
        magn = float(input("Magn: "))

        if(maelieining == "1"): #Gallon í Lítra
            print(magn, "gallon eru", gallon_litrar(magn), "l")
        elif(maelieining == "2"): #Lítrar í Gallon
            print(magn, "l eru", litrar_gallon(magn), "gallon")

    #Dæmi 6 - Kveðja
    elif(val == "6"):
        gender = input("Hvort ertu kk eða kvk? : ")
        name = input("Hvað heitir þú? : ")
        kvedja(name, gender)

    #Dæmi 7 - Teningakast
    elif(val == "7"):
        kasta()

    #Dæmi 8 - Listar
    elif(val == "8"):
        listi1 = [2, 5, 8, 1, 21, 1, 25, 104, 231]
        listi2 = [3, 7, 5, 21, 12, 1, 214, 32, 321]
        print("Sömu tölur:", SamaILista(listi1, listi2))

    elif(val == "9"):
        print("Eigðu góðan dag.")
        break

    else:
        print("Þarna skrifaðir þú eitthvað vitlaust, reyndu aftur.")

    greinaskil()