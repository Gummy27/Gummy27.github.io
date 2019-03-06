#Gudmundur Brimir Bjornsson 
#Uppsetning hafinn 2019-03-05
# Föll
def greinaskil(): 
   print('==========')

# Föll sem notuð er aftur og aftur
def skrifaSkra(listi, nafntxt):
    f = open(nafntxt+".txt", "a+", encoding="utf-8")
    for x, y in enumerate(listi):
        if x != len(listi)-1:
            f.write(str(y)+" ")
        else:
            f.write(str(y))
    f.close()

def lesaSkra(nafnTxtSkra):
    listi = []
    f = open(nafnTxtSkra+".txt", "r", encoding="utf-8")
    listi = list(map(int, f.read().split(" ")))
    f.close()
    return(listi)

def prenta(listi):
    for x, y in enumerate(listi):
        if(x != len(listi)-1):
            print(y, end=", ")
        else:
            print(y)

# Föll sem eru notuð í dæmi 1
def slettarTolurListi():
    listi = []
    for x in range(1, 1001):
        if x % 2 == 0:
            listi.append(x)
    return(listi)

def medaltal(listi):
    return(round(sum(listi), 2))

def uppI8(listi):
    listi_2= []
    for x in listi:
        if x % 8 == 0:
            listi_2.append(x)
    return(listi_2)

def prenta_10(listi):
    for x, y in enumerate(listi):
        if x % 9 == 0:
            print(y, "\n")
        else:
            print(y, end=" ")
    print()

# Föll sem eru notuð í dæmi 2

def primtolur_100():
    listi =  []
    for x in range(100):
        flag = 0
        if x % 2 != 0:
            for i in range(2, x):
                if x % i == 0:
                    flag = 1
                    break
            if flag == 0:
                listi.append(x)
    return(listi)

def tolur7(listi):
    for x in listi:
        if(str(x).count("7") > 1):
            print(x)

def fjorda_hver_tala(listi):
    nyr_listi = []
    for x, y in enumerate(listi):
        if x % 4 == 0:
            nyr_listi.append(y)
    return(nyr_listi)

# Föll sem notuð er í dæmi 3
def skrifa_i_tuple(tupla):
    f = open("tuple.txt", "a+", )
    f.write("\n(")
    for x, y in enumerate(tupla):
        try:
            str(y)
            if(x != len(tupla)-1):
                f.write("'"+y+"',")
            else:
                f.write("'"+y+"')")
        except:
            if (x != len(tupla) - 1):
                f.write(y + ", ")
            else:
                f.write(y + ")")

    f.close()

def lesaTupleSkra():
    f = open("tuple.txt", "r")
    strengur = f.read().split("\n")
    for x in strengur:
        print(x)
    f.close()

def bua_til_tuple():
    listi = []
    lengd = int(input("Hve margir hlutir eiga að fara í tuple? : "))
    for x in range(lengd):
        listi.append(input("Sláðu inn hlut sem á að fara í tuple. : "))
    tupla = tuple(listi)
    return(tupla)

def summa_fyrstu_tupplunar():
    f = open("tuple.txt", "r")
    f.seek(0)
    listi = list(map(int, f.readline()[1:-2].split(",")))
    return(sum(listi))

# Föll sem eru notuð í dæmi 4

def buaTilDict():
    dict = {}
    for x in range(int(input('Hve mikið af hlutum á að vera í dictionary? : '))):
        dict[input("Lykill : ")] = int(input("Gildi : "))
    return(dict)

def skrifaDictITuple(dict):
    f = open('dict.txt', 'a+', encoding='utf-8')
    f.write("{")
    teljari = 0
    for key, value in dict.items():
        if teljari != len(dict)-1:
            f.write("'" + key + "': " + str(value) + ', ')
        else:
            f.write("'"+key+"': "+str(value)+'}\n')
        teljari += 1
    f.close()

def lesaDictSkra():
    f = open('dict.txt', 'r', encoding='utf-8')
    print(f.readline())
    f.close()

def skrifaUtItems():
    f = open('dict.txt', 'r', encoding='utf-8')
    for teljari, x in enumerate(f):
        print("  Lína", teljari+1)
        listi = x[1:-2].split(", ")
        for i in listi:
            strengur = i.replace("'", "")
            lykill, gildi = strengur.split(":")
            print(lykill+" "*(7-len(lykill)), gildi)
        greinaskil()

    f.close()
# Valmynd
verkefni = ['Sléttar tölur', 'Prímtölur', 'Tuple skrá', 'Dictionary', 'Hætta'] 
while(True): 
    for x, y in enumerate(verkefni):
        print(str(x+1)+'.', y)
    val = input('Hvaða dæmi viltu skoða? : ')
    greinaskil()

    # Dæ
    if val == '1':
        slettar_tolur = slettarTolurListi() #a
        skra = input("Hvað á skráin að heita? : ")
        skrifaSkra(slettar_tolur, skra) #b
        innihald = lesaSkra(skra) #c
        prenta(innihald) #d
        medaltal(innihald) #e
        gengurI8 = uppI8(innihald) #f
        skrifaSkra(gengurI8, "sumarslettartolur") #g
        prenta_10(innihald) #h

    elif val == '2':
        primtolur = primtolur_100() #a
        skrifaSkra(primtolur_100(), "primtolur") #b
        lesaSkra("primtolur") #c
        prenta(primtolur) #d
        tolur7(primtolur) #e
        fjordaHver = fjorda_hver_tala(primtolur) #f
        skrifaSkra(fjordaHver, "fjorda") #g
 
    elif val == '3':
        lesaTupleSkra()
        greinaskil()
        tuple_listi = bua_til_tuple() #d
        skrifa_i_tuple(tuple_listi)
        print(summa_fyrstu_tupplunar())
 
    elif val == '4':
        '''
        skrifaDictITuple(buaTilDict())
        lesaSkra("dict")
        lesaDictSkra()
        greinaskil()
        skrifaDictITuple(buaTilDict())
        greinaskil()
        skrifaDictITuple(buaTilDict())
        '''
        skrifaUtItems()


    elif(val == '5'):
        break
    greinaskil()
