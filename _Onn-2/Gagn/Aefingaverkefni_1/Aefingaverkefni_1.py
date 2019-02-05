#Guðmundur Brimir Björnsson
#16. janúar, 2019
print("Höfundur: Guðmundur Brimir Björnsson")
print("Uppsetning hafinn: 16. janúar, 2019")
val = ""
while(val != "3"):
    print("1. Rita inn í skjal.")
    print("2. Lesa skjal.")
    print("3. Hætta.")
    val = input("Hvaða dæmi viltu skoða? : ")
    print("==========")

    if(val == "1"):
        texti = input("Skrifaðu inn smá texta. : ")
        f = open("skra.txt", "a+")
        try:
            texti = texti+" "
            f.write(texti)
        finally:
            print(texti, "hefur verið skrifaður í skránna skra.txt.")
            f.close()

    elif(val == "2"):
        f = open("skra.txt", "r",)
        try:
            print(f.read())
        finally:
            f.close()
            
    elif(val == "3"):
            print("Eigðu góðan dag.")
            
    else:
            print("Þarna skrifaðirðu eitthvað vitlaus. Reyndu aftur.")

    print("==========")
            
