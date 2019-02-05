#Guðmundur Brimir Björnsson
#Uppsetning hafinn 30. janúar, 2019
import csv
import random
stig = 0

skra = open("spurningar.txt", encoding="utf-8-SIG")
lesari = csv.reader(skra, delimiter=";")
spurningar=list(lesari)
print(spurningar)
random.shuffle(spurningar)

print(spurningar)
for x in spurningar:
    for i in range(2):
        svar = input(x[0]+" : ")
        if(svar.lower() == x[1].lower()):
            print("Já þetta var hárrétt!")
            stig += 1
            break
        else:
            if(i == 0):
                print("Þetta var vitlaust. Reyndu aftur.")
            elif(i == 1):
                print("Ahh, rétta svarið var", x[1])
    print('==========')

print("Þú náðir", stig, "af 10 stigum.")

