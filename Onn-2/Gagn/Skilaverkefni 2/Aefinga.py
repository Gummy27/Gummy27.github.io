f = open("simaskra.txt", "r")
for x in f.read():
    if(x == "\n"):
        print(x, "+")
    else:
        print(x)
