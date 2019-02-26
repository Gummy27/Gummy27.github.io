#Guðmundur Brimir Björnsson
#Uppsetning hafinn 21. febrúar 2019
import random

def greinaskil():
    print("==========")

# Þetta fall mun prenta út tuple á fallegan hátt.
def prentaTuple(tupl1, tupl2):  # Fallið tekur inn 2 tuple lista og skýrir þá tupl1 og tupl2
    for x in tupl1:  # Fyrst er farið í gegnum tupl1. Þar mun x taka á sig gildi í tuple1
        print(x, end=" ")  # Prentað er út x en ekki með newline heldur bara autt bil þar sem næsta x kemur.
    print() # Prentað er ekkert út svo að næsta for slaufa prenti ekki í sömu línu og hin.
    for x in tupl2: # Farið er í gegnum tupl2 þar sem x tekur á sig gildi úr tupl2
        print(x, end=" ") # X er prentað út með ekkert endline.
    print() # Hér er ekkert prentað út svo að ný lína verðu búin til.

# Þetta fall parar saman tvo einstaklinga úr báðum listunum.
def paraRod(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    for x in range(len(tupl1)): #Þessi slaufa mun loopa jafn mörgum sinnum og það eru hlutir í tupl1.
        print(tupl1[x], "og", tupl2[x]) #Hér eru sérstök stök úr listunum prentuð út og þau pöruð saman: Einar og Jósefína

# Þetta fall velur einstaklinga af handahófi og parar þeim saman.
def paraRandom(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    for x in range(len(tupl1)): #Þessi slaufa mun loopa jafn mörgum sinnum og það eru hlutir í tupl1.
        y = random.randint(0, 4) #y fær á sig handahófskennda tölu sem mun vera notuð til að velja einhvern úr hópnum.
        i = random.randint(0, 4) #i fær á sig handahófskennda tölu sem mun vera notuð til að velja einhvern úr hópnum.
        print(tupl1[i], "og", tupl2[y]) #Hér eru sérstök stök úr listunum prentuð út og þau pöruð saman: Einar og Jósefína

# Þetta fall velur einstakling af handahófi og parar þeim saman. Hérna þá getur aðeins einn einstaklingur verið paraður í einu.
def paraRandomStakur(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    #Tuple listarnir eru breyttir í venjulega lista og síðan settir í tupl_random svo hægt sé að breyta röðinni í þeim.
    tupl1_random = list(tupl1) #List er notað til að breyta tuple í lista.
    tupl2_random = list(tupl2)
    #Listarnir eru síðan shufflaðir með .shuffle fallið sem breytir röðinni þeirra í einhverja handahófskennda röð.
    random.shuffle(tupl1_random)
    random.shuffle(tupl2_random)
    for x in range(len(tupl1)): #Þessi slaufa mun loopa jafn mörgum sinnum og það eru hlutir í tupl1.
        print(tupl1_random[x], "og", tupl2_random[x]) #Hér eru sérstök stök úr listunum prentuð út og þau pöruð saman: Einar og Jósefína

# Þetta fall reynir að finna nafn eftir aðeins einum staf.
def finnaNafn(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    stafur = input("Skrifaðu inn staf sem á að leita að í nöfnunum. : ") #Notandi er spurður um þann staf sem á að leita að.
    # Þessar for slaufur munu fara í gegnum báða tuple listana og taka á sig gildi úr þeim.
    for x in tupl1:
        # Í þessari for slaufu fer i í gegnum alla stafina í x til að gá hvort að stafurinn sé í orðinu.
        for i in x:
            # Gáð er hvort að i sé sá stafur sem leitað er að.
            if(i.lower() == stafur.lower()): # Stafirnir eru settir í lágstafi svo að hann finni stafinn þó að hann sé í hástöfum.
                print(x) #Orðið sem er með stafnum er prentað út.
                break #Ekki er þörf á að leita meira því við fundum stafinn í orðinu svo for slaufan er brotinn. 
    for x in tupl2:
        for i in x:
            if(i.lower() == stafur.lower()):
                print(x)
                break

# Gáð er hvort að orð hefur fleiri en eitt n
def morgN(tupl1, tupl2): #Fallið tekur inn tvo tuple lista sem munu heita tupl1 og tupl2
    # Þessi for slaufa mun fara í gegnum listann tupl1.
    for x in tupl1: 
        # Flag er bráðabirgðarbreyta sem verður notuð til að sýna fram á það að fleiri en 1 n sé orðinu.
        flag = 0
        #for slaufa fer gegnum x til að skoða alla stafina í orðinu í leit að n.
        for i in x:
            if(i.lower() == 'n'): #Gáð er hvort að i í lágstöfum sé n
                flag += 1 #Flag er plúsað við einn.
                continue #Continue er notað til að fara í gegnum hina if setninguna.
            elif(flag == 2): #Gáð er hvort að flag sé 2 sem bendir til þess að orðið hafi meiri eða nákvæmlega 2 n.
                print(x)
                break
    for x in tupl2:
        flag = 0
        for i in x:
            if(i.lower() == 'n'):
                flag += 1
                continue
            elif(flag == 2):
                print(x)
                break

def finnaFyrstaStaf(tupl1, tupl2):
    stafur = input("Skrifaðu inn staf sem tilheyrir fyrsta staf nafns. : ")
    for x in tupl1:
        if(x[0].lower() == stafur.lower()):
            print(x)
    for x in tupl2:
        if(x[0].lower() == stafur.lower()):
            print(x)

def finnaSimanumer(nafn, simskra):
    for key, value in simaskra.items():
        if(key.lower() == nafn.lower()):
            return(value)
            break

def prentaDict(dict):
    for key, value in dict.items():
        print(key, "-"*(10-len(key))+">", " "*(2-len(str(value))) + str(value), "ára")

def yfir18(dict):
    teljari = 0
    for key, value in dict.items():
        if(value <= 18):
            teljari += 1
            print(key)
    print("Þarna voru", teljari, "sem voru 18 ára eða eldri")

def medalaldur(dict):
    samanlagt = 0
    for key, value in dict.items():
        samanlagt += value
    print("Meðalaldur bekkjarins er", round((samanlagt/15), 2))

def heildaraldur(dict):
    samanlagt = 0
    for key, value in dict.items():
        samanlagt += value
    print("Samanlagður aldur bekkjarins er", samanlagt)

def finnaStafDict(dict):
    listi = []
    stafur = input("Skrifaðu inn staf. : ")
    for key, value in dict.items():
        if(stafur.lower() == key[0].lower()):
            print(key, "-" * (10 - len(key)) + ">", " " * (2 - len(str(value))) + str(value), "ára")
            listi.append(key)
    return(listi)

def medalaldurDict_2(listi, dict):
    samanlagt = 0
    for x in listi:
        for key, value in dict.items():
            if(x == key):
                samanlagt += value
                break
    print("Meðalaldur þeirra er", round((samanlagt/len(listi)),2))

verkefni = ["Danspörin", "Símaskrá", "Skráning í bekk", "Hætta"]
while(True):
    for x, y in enumerate(verkefni):
        print(str(x+1)+".", y)
    val = input("Hvaða dæmi viltu skoða? : ")
    greinaskil()

    if(val == "1"):
        strakar = ("Einar", "Geir", "Angantínus", "Halldór", "Heimir", "Kristófer")
        stelpur = ("Rósa", "Kristín", "Guðmunda", "Halldóra", "Gerður", "Anna")

        daemi_1 = ["Nafnalisti prentaður út", "Parað er saman eftir röð", "Pör valin af handahófi",
                   "Pör valin af handahófi en aðeins 1 getur komið í einu", "Finna nafn eftir einum staf",
                   "Finna fyrsta staf", "Fleiri en 1 n", "Hætta"]
        while(True):
            for x, y in enumerate(daemi_1):
                print(str(x+1)+".", y)
            val = input("Hvaða fall viltu skoða? : ")
            greinaskil()

            if(val == "1"):
                prentaTuple(strakar, stelpur)

            elif(val == "2"):
                paraRod(strakar, stelpur)

            elif(val == "3"):
                paraRandom(strakar, stelpur)

            elif(val == "4"):
                paraRandomStakur(strakar, stelpur)

            elif(val == "5"):
                finnaNafn(strakar, stelpur)

            elif (val == "6"):
                finnaFyrstaStaf(strakar, stelpur)

            elif(val == "7"):
                morgN(strakar, stelpur)

            elif(val == "8"):
                break

            greinaskil()
    elif(val == "2"):
        simanumer = ""
        simaskra = {"Einar":8121234, "Þórgerður":9202138, "Heimir":2302317, "Ragnar":2312309, "Halldór":9218321,
                    "Kristófer":6723214, "Anna":5622364, "Sigurður":2782387, "Pedró":7682347, "Dagný":2312787}
        nafn = input("Hvern viltu finna? : ")
        simanumer = finnaSimanumer(nafn, simaskra)
        simanumer = str(simanumer)
        if(simanumer == ""):
            print("Þetta nafn er ekki til í skránni")
        else:
            print(nafn, "er með símanúmerið:", simanumer[0:3]+"-"+simanumer[4:])

    elif(val == "3"):
        bekkur = {"Einar":16, "Guðmundur":17, "Árni":4, "Gabríel":20, "Halldór":22, "Heimir":30, "Kristófer":42,
                  "Magnús":15, "Hreiðar":14, "Guðmunda":18, "Þógerður":21, "Sólveig":13, "Guðrún":19, "Geir":6,
                  "Kormákur":78}
        daemi_2 = ["Bekkurinn er prentaður út", "18 ára eða eldri", "Meðalaldur bekkjarins", "Heildaraldur bekkjarins",
                   "Fyrsti stafur og meðalaldur þeirra", "Hætta"]
        while (True):
            for x, y in enumerate(daemi_2):
                print(str(x + 1) + ".", y)
            val = input("Hvaða fall viltu skoða? : ")
            greinaskil()
            if(val == "1"):
                prentaDict(bekkur)

            elif(val == "2"):
                yfir18(bekkur)

            elif(val == "3"):
                medalaldur(bekkur)

            elif(val == "4"):
                heildaraldur(bekkur)

            elif(val == "5"):
                nafnalisti = finnaStafDict(bekkur)
                medalaldurDict_2(nafnalisti, bekkur)

            elif(val == "6"):
                break

            greinaskil()


    elif(val == "4"):
        print("Eigðu góðan dag.")
        break
    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")

    greinaskil()
