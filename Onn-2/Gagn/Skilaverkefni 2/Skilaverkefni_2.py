#Guðmundur Brimir Björnsson
#18. janúar, 2019
print("Höfundur: Guðmundur Brimi Björnsson")
print("Uppsetning hafinn: 18. janúar 2019")
val = ""
def greinaskil(): #Fallið greinaskil er skilgreind og verður notað til að gera.... Þarf ég að segja þér hvað það á að gera það er í nafninu.
    print("==============")

while(val != "5"): #Þessi while lykkja á að tryggja það að notandi geti gert hvert dæmi nokkrum sinnum.
    for x in range(5): #Valmynd er prentuð út með for lykkju.
        if(x != 4):
            print(str(x+1)+". Dæmi", x+1)
        else:
            print(str(x+1)+". Hætta")
    val = input("Hvaða dæmi viltu skoða? : ")
    greinaskil()

    #Dæmi 1
    if(val == "1"):
        f = open("simaskra.txt", "a+") 
        #Ég kaus að geyma gögnin nákvæmlega eins og var á myndinni. Mig fannst það góð leið til að skilja að orð svo að forritið gæti verkað vel.
        f.write(input("Hvað heitir sá sem á númerið? : ")+"; ")
        f.write(input("Hver er kennitala hans. : ")+"; ")
        f.write(input("Hvað er símanúmerið hans? : ")+"\n")
        f.close()

    #Dæmi 2    
    elif(val == "2"):
        f = open("simaskra.txt", "r")
        simaskra = [] #Þessi listi mun innihalda tengiliðina sem eru í símaskrána.
        tengilidur = [] #Þessi listi mun innihalda nafn, kennitölu og símanúmer tengiliðanna.
        innsetning = "" #Innsetning er breyta sem mun vera notuð til að gefa listanum tengilidur þær upplýsingar sem hann þarf.
        teljari = 0 #Teljari mun vera notaður sem teljari
        stadsetning = 0 #Í þessari breytu mun staðsetning tengiliðarins sem á að breyta vera geymt.
        ma_koma = 0 #Einföld já eða nei breyta sem aðeins mun vera notuð einu sinni.
        
        line = f.read() 
        for x in line:
            if(x == ";"): #Gáp er hvort að x sé ;. Ef svo er þá er orðið sett inn í tengilidur listann.
                tengilidur.append(innsetning)
                innsetning = "" #Innsetning er núllstillt.
            elif(x == "\n"): #Gáð er hvort að x sé \n. Ef svo er þá er orðið sett í tengilidur listann og tengilidur listinn er settur í simaskra.
                tengilidur.append(innsetning)
                simaskra.append(tengilidur)
                tengilidur = [] #Tengiliður er núllstilltur svo að hann geti safnað upplýsingum um næsta tengilið.
                innsetning = "" #Innsetning er núllstillt.
            else:
                innsetning = innsetning + x #Innsetning fær á sig næsta stafinn í orðinu/tölunni.
            teljari += 1

        #Símaskráinn er prentuð til sýna notanda hvaða tengiliðir eru til staðar.
        for x in range(len(simaskra)):
            for x in simaskra[x]:
                print(x, end="")
            print()

        #Þessi while lykkja mun innihalda kóða sem á að finna staðsetningu tengiliðarins sem á að breyta.
        while(ma_koma != 1):
            leit = input("Hvaða tengilið viltu breyta? : ")
            for x in range(teljari):
                try: #Í fyrrum útgáfum kóðans þá myndi kóðinn ganga að eilífu. Létt er að laga þetta en ég ákvað að í staðinn setja upp error skilyrði til að segja notandann að hann hafi skrifað inn eitthvað vitlaust.
                    if(simaskra[x][0] == leit): #Þetta tjékkar hvort að nafnið þarna sé það sama og það nafn sem við erum að leita að.
                        stadsetning = x #Staðsetning er sett inní staðsetning breytuna.
                        ma_koma = 1 #ma koma er hækkað um einn svo hægt sé að komast út lykkjuna.
                        break #For slaufann er brotinn því við þurfum hana ekki lengur.
                except IndexError: #Þessi kóði gengur aðeins ef að forritið rennur í IndexError villu.
                    print("Fyrirgefðu en þetta nafn finnst ekki. Reyndu aftur.") 
                    greinaskil()
                    break

        #Þessi while lykkja mun innihalda þann kóða sem mun breyta tengiliðnum.
        while(val != "0"):
            #Valmynd er prentuð út.
            print("1. Nafn")
            print("2. Kennitala")
            print("3. Símanúmer")
            print("0. Hætta")
            val = input("Hverju viltu breyta? : ")

            #Gáð er hvort að notandi hafi valið að hætta. Kóðinn brýtur while lykkjuna.
            if(val == "0"):
                break
            #Gáð er hvort að notandi hafi valið eitthvað af þeim valmöguleikum sem var gefið upp.
            elif(val == "1" or val == "2" or val == "3"):
                simaskra[stadsetning][int(val)-1] = input(": ") #Tengiliðurinn er uppfærður.
            #Þessi kóði keyrist ef að notandi hefur valið eitthvað vitlaust.
            else:
                print("Þarna skrifaðirðu eitthvað vitlaust. Reyndu aftur.")
        
        f = open("simaskra.txt", "a+")
        f.seek(0)
        f.truncate() #Innihald upprunalega skránnar er eydd svo að nýju upplýsingarnar koma yfir.
        for x in range(len(simaskra)): #Í þessari for lykkju er tengiliðurinn skrifaður inn í skjalið.
            f.write(simaskra[x][0]+";"+simaskra[x][1]+";"+simaskra[x][2]+"\n")
        f.close()

    #Dæmi 3
    elif(val == "3"):
        teljari = 0
        listi = []
        f = open("simaskra.txt", "r")
        #í Þessari for lykkju þá eru allir tengiliðirnir í skjalinu settir á lista og í leiðinni er prentuð út valmynd fyrir notandann.
        for x in f:
            teljari += 1
            listi.append(x)
            print(str(teljari)+".", x, end="")
        
        stadsetning = int(input("Hvaða tengilið langar þig að eyða? : "))
        del listi[stadsetning-1] #Tengiliðurinn í listanum er eyddur

        f = open("simaskra.txt", "a+")
        f.seek(0)
        f.truncate() #Innihald skjalsins er eytt svo að nýju upplýsingarnar get komið í staðinn.
        #Í þessari for lykkju er listinn skrifaður inn i skjalið.
        for x in listi:
            f.write(x)
        f.close()

    elif(val == "4"):
        f = open("simaskra.txt", "r")
        #Sami kóðinn og var notaður í dæmi 2 er notaður hér til að skrifa inn í lista. Það munt þú finna meiri upplýsingar um kóðann sjálfan.
        line = f.read()
        innsetning = ""
        tengilidur = []
        simaskra = []
        for x in line:
            if(x == ";"):
                tengilidur.append(innsetning)
                innsetning = ""
            elif(x == "\n"):
                print("Yes")
                tengilidur.append(innsetning)
                simaskra.append(tengilidur)
                tengilidur = []
                innsetning = ""
            else:
                innsetning = innsetning + x
        #Þetta eru einu viðbæturnar. Í þessari lykkju er nafn, kt og símanúmer tengiliðs skrifað fallega í einni línu.
        for x in range(len(simaskra)):
            print("Nafn:", simaskra[x][0], end=", ")
            print("Kt:", simaskra[x][1], end=", ")
            print("Símanúmer:", simaskra[x][2])

    #Dæmi 5
    elif(val == "5"):
        print("Eigðu góðan dag.")

    #Eitthvað var skrifað vitlaust.
    else:
        print("Þarna skrifaðirðu eitthvað vitlaust. Reyndu aftur.")

    greinaskil()
