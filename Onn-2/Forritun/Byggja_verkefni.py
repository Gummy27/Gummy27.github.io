import datetime
print(datetime.date.today())

nafn = input("Hvað viltu að verkefnið heiti?: ")
daemi = []
for x in range(int(input("Hve mikið af dæmum? : "))):
    daemi.append(input("Hvað heitir dæmið? : "))
daemi.append("Hætta")

f = open(str(nafn)+".py", 'a+', encoding='windows-1252')
f.write("#Gudmundur Brimir Bjornsson \n")
f.write("#"+str(datetime.date.today())+"\n")
f.write("verkefni = [")
for x, gildi in enumerate(daemi):
    if(x != len(daemi)-1):
        f.write("'"+gildi+"', ")
    else:
        f.write("'"+gildi+"'")
f.write("] \n")
f.close()