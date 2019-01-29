#Guðmundur Brimir Björnsson
#Uppsetning hafinn 29. janúar, 2019 - kláruð 29. janúar, 2019
def greinaskil():
    print("=================")
    
def skrifaUt(listi):
    for x in range(len(listi)):
        if(x != len(listi)-1):
            print(listi[x], end=", ")
        else:
            print(listi[x])

def staersta(listi):
    staerst = listi[0]
    for x in listi:
        if(x > staerst):
            staerst = x
    return(staerst)

def minnsta(listi):
    minnsta = listi[0]
    for x in listi:
        if(x < minnsta):
            minnsta = x
    return(minnsta)

def summa(listi):
    utk = 0
    for x in listi:
        utk += x
    return(utk)

def medaltal(listi):
    summa = 0
    teljari = 0
    for x in listi:
        summa += x
        teljari += 1
    return(summa/teljari)

verkefni = ["Unnið með 5 tölur", "Unnið með 4 tölur", "Meðaltal talna", "Finna orðið", "Hætta"] 
while(True):
    for x in range(len(verkefni)):
        print(str(x+1)+".", verkefni[x])
    val = input("Hvaða verkefni viltu skoða? : ")
    greinaskil()

    if(val == "1"):
        tolur = []
        for x in range(5):
            tolur.append(int(input("Skrifaðu inn tölu. : ")))
            
        skrifaUt(tolur)
        print(staersta(tolur))
        print(minnsta(tolur))
        print(summa(tolur))
        print(medaltala(tolur))
    elif(val == "2"):
        pass

    elif(val == "3"):
        pass

    elif(val == "4"):
        pass
    
    elif(val == "5"):
        print("Eigðu góðan dag.")
        break
    
    else:
        print("Þarna skrifaðir þú eitthvað vitlaust. Reyndu aftur.")

    greinaskil()
    
