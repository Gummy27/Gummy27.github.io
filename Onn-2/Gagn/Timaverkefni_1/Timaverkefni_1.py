#Guðmundur Brimir Björnsson
#Uppsetning hafinn 15. febrúar 2019
def greinaskil():
    print("==========")

verkefni = ["Bæta í skrána", "Birta skrána í heild", "Birta upplýsingar um ákveðið dýr eftir nafni.", "Hætta"]
while(True):
    for x in range(len(verkefni)):
        print(str(x+1)+".", verkefni[x])
    val = input("Hvað viltu gera? : ")
    greinaskil()

    #Dæma 1 - Bæta í skrána.
    if(val == "1"):
        gaeludyra_listi = []
        f = open("gaeludyr.txt", "r")
        strengur = ""
        strengja_listi = []
        #Þessi for slaufa mun fara í gegnum f.read(), (sem er skráin), og gera lista inn í lista af upplýsingunum.
        for line in f.read(): #Line tekur á sig einn staf í einu úr skránni.
            if(line != ";" and line != "\n"): #Gáð er hvort að line sé ";" eða "\n" til að skilja að orðinn.
                strengur += line #Strengur fær á sig einn staf hverju sinni sem forritið nær í gegn. Loks mun strengur verða heilt orð.
            elif(line == ";"): #Gáð er hvort að line sé ";" til að skilja að orðunum.
                strengja_listi.append(strengur) #Hér vitum við að strengur er búinn að taka á sig heilt orð svo við bætum því við strengja listi listann.
                strengur = "" #Strengur breytan er endurræst svo það geti tekið á sig annað orð.
            elif(line == "\n"): #Gáð er hvort að line sé "\n" til að aðgreina setningar.
                strengja_listi.append(strengur) #Hér vitum við að strengur er búinn að taka á sig heilt orð svo við bætum því við strengja listi listann.
                gaeludyra_listi.append(strengja_listi) #Hér vitum við að strengja_listi listinn er búinn að taka á sig heila línu af upplýsingum svo við færum hann í lista inn í lista.
                strengur = "" #Strengur er endurræstur svo hann geti tekið á sig annað orð.
                strengja_listi = [] #Strengja listi er endurræstur svo hann geti tekið á sig aðra línu.
        strengja_listi.append(input("Hvað heitir gæludýraeigandinn? : ")) #Spurt er um nafn eiganda gæludýrs.
        strengja_listi.append(input("Hvað heitir gæludýrið? : ")) #Spurt er um nafn á gæludýri.
        strengja_listi.append(input("Hvernig tegund er gæludýrið? : ")) #Spurt er um tegund gæludýrs.
        gaeludyra_listi.append(strengja_listi) #Eftir að hann er búinn að fá input hjá öllum liðum þá bætir hann þvi loks við gæludýra listann.

        f = open("gaeludyr.txt", "a+") #F er breytt svo það geti breytt skjalinu.
        f.seek(0) #F er sett á byrjunarreit svo að hann eyðir öllu af skjalinu.
        f.truncate() #Allar upplýsingar er eyddar af skjalinu.
        #For slaufa er hafinn og mun skrifa allar upplýsingar aftur inn í listann ásamt nýju upplýsingunum.
        for x in gaeludyra_listi: #x mun keyra í gegnum allan gæludýralistann og taka á sig listann sem inni í honum er.
            for teljari, gildi in enumerate(x): #For slaufa þessi enumeratar listan x til að forðast það að nota teljara.
                if(teljari != 2): #Gáð er hvort að for slaufan hafi verið keyrðu 2 sinnum.
                    f.write(gildi+";") #Gildinu er skrifað inn ásamt ";" til að aðskilja.
                else:
                    f.write(gildi+"\n") #Hér er gildinu skrifað inn ásamt "\n" til að aðskilja línurnar.
        f.close()

    #Dæmi 2 - Birta skrána í heild.
    elif(val == "2"):
        f = open("gaeludyr.txt", "r")
        print("Nafn Eiganda:  Nafn dýrsins:  Tegund:")
        teljari = 0
        #For slaufa þessi mun skrifa út allar upplýsingar sem geymdar eru i listanum.
        for x in f.read():
            if(x != ";" and x != "\n"): #Gáð er hvort að x sé annaðhvort ";" eða "\n"
                print(x, end="") #Stafnum er prentað út með engu millibili.
                teljari += 1 #Teljari þessi verður notaður til að reikna út hve mikið bil það þarf á milli orða.
            elif(x == ";"): #Hér er gáð hvort að x sé ";" ef svo er þá er ekkert prentað nema stórt bil sem er í samræmi við lengd orðsins.
                print("", end=" "*(15-teljari))
                teljari = 0
            elif(x == "\n"): #Gáð er hvort að x sé "\n" ef svo er þá er ekkert skrifað svo að ný lína myndast.
                print("")
                teljari = 0

    #Dæmi 3 - Birta upplýsingar um ákveðið gæludýr með nafni.
    elif(val == "3"):
        dyr = input("Hvað heitir gæludýrið? : ") #Spurt er til nafns á gæludýri.
        f = open("gaeludyr.txt", "r")
        strengur = ""
        strengja_listi = []
        gaeludyra_listi = []
        #Þessi for slaufa mun gera lista inn í lista líkt og í dæmi 1. Nánari komment er þar um verklag slaufunar.
        for x in f.read():
            if(x != ";" and x != "\n"):
                strengur += x
            elif(x == ";"):
                strengja_listi.append(strengur)
                strengur = ""
            elif(x == "\n"):
                strengja_listi.append(strengur)
                gaeludyra_listi.append(strengja_listi)
                strengja_listi = []
                strengur = ""

        flag = 0
        #Í þessari for slaufu mun vera leitað að gæludýrinu.
        for x in gaeludyra_listi:
            if(x[1].lower() == dyr.lower()): #Nafn gæludýrs er í sæti 2(1) í listanum svo þar er gáð hvort að þetta sé nafnið sem notandi er að leita að.
                print("Eigandi:", x[0]) #Nafn eiganda prentað út.
                print("Nafn gæludýrs:", x[1]) #Nafn gæludýrs prentað út.
                print("Tegund:", x[2]) #Tegund gæludýrst prentað út.
                flag = 1
                break #Slaufan er brotinn þvi við erum búnir að finna gæludýrið.
            else:
                pass

        if(flag == 0):
            print("Fyrirgefðu en við finnum ekkert gæludýr undir þessu nafni.")

    elif(val == "4"):
        print("Eigðu góðan dag.")
        break

    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")

    greinaskil()