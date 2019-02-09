#Guðmundur Brimir Björnsson
#16. janúar, 2019
print("Höfundur: Guðmundur Brimir Björnsson")
print("Uppsetning hafinn: 16. janúar, 2019")
print("==========")
val = ""
while(val != "3"):
    print("1. Rita inn í skjal.")
    print("2. Lesa skjal.")
    print("3. Hætta.")
    val = input("Hvaða dæmi viltu skoða? : ")
    print("==========")

    if(val == "1"):
        f = open("skra.txt", "a+")
        talnalisti = []
        for x in range(5):
            talnalisti.append(input("Skrifaðu inn tölu. : "))
        for x in range(5):
            f.write(str(talnalisti[x])+" ")
        f = open("skra.txt", "r")
        print(f.read())       
        f.close()

    elif(val == "2"):
        f = open("skra.txt", "r")
        tala = ""
        talnalisti = []
        strengur = f.read()
        for x in strengur:
            if(x != " "):
                tala = tala+x
            else:
                talnalisti.append(int(tala))
                tala = ""
        print(round(sum(talnalisti)/len(talnalisti),2))
                

    elif(val == "3"):
        print("Eigðu góðan dag.")

    else:
        print("Þarna skrifaðirðu eitthvað vitlaust. Reyndu aftur.")
