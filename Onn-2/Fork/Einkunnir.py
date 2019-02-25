spurningar, nemendur = input().split(" ")
spurningar = int(spurningar)
nemendur = int(nemendur)
stig = 10/spurningar
n = input().split(" ")
dict = {}

def fall():
    teljari = 0
    nafn = input()
    svar = input().split(" ")
    for x, y in enumerate(svar):
        if(y == n[x]):
            teljari += stig

    teljari = round(teljari, 2)
    y = ""
    i = teljari
    for x in str(i):
        if(x != "."):
            y += x
        else:
            break
    i = y
    i = int(i)
    if(teljari < float(i+0.25)):
        teljari = str(i)+".0"
    elif(teljari < float(i+0.75)):
        teljari = i+0.50
    elif(teljari >= float(i+0.75)):
        teljari = str(round(teljari, 0))+".0"
    
    return(str(nafn)+": "+str(teljari))

listi = []
for x in range(nemendur):
    listi.append(fall())
for x in listi:
    print(x)
