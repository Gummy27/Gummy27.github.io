import turtle
import time

flag = False
flag_1 = False

bord = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

global spilari
spilari = 1

# Skjár
wn = turtle.Screen()
wn.title("Tic Tac Toe by Gummy27")
wn.bgcolor("white")
wn.setup(width=700, height=700)

grid = turtle.Turtle()
grid.speed(0)
grid.pencolor("black")
grid.right(90)

for x in range(2):
    grid.penup()
    grid.goto(-100+(200*x), 300)
    grid.pendown()
    grid.forward(600)
grid.right(90)
for x in range(2):
    grid.penup()
    grid.goto(300, -100+(200*x))
    grid.pendown()
    grid.forward(600)
grid.hideturtle()

wn.tracer(0)

#Teiknari
teiknari = turtle.Turtle()
teiknari.speed(0)
teiknari.pencolor("black")

# Functions
# Innsláttur
#  1 Röð
def grid_1():
    if(bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(-290, 290)
        teiknari.pendown()
        teikna()

def grid_2():
    if (bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(-90, 290)
        teiknari.pendown()
        teikna()

def grid_3():
    if (bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(110, 290)
        teiknari.pendown()
        teikna()

#2 Röð
def grid_4():
    if (bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(-290, 90)
        teiknari.pendown()
        teikna()

def grid_5():
    if (bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(-90, 90)
        teiknari.pendown()
        teikna()

def grid_6():
    if (bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(110, 90)
        teiknari.pendown()
        teikna()

#3 Röð
def grid_7():
    if (bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(-290, -110)
        teiknari.pendown()
        teikna()

def grid_8():
    if (bord[1] == "-"):
        teiknari.penup()
        teiknari.goto(-90, -110)
        teiknari.pendown()
        teikna()

def grid_9():
    teiknari.penup()
    teiknari.goto(110, -110)
    teiknari.pendown()
    teikna()

# Teikna
def teikna():
    global spilari
    if(spilari % 2 == 0):
        # Kross
        x = teiknari.xcor()
        y = teiknari.ycor()
        teiknari.right(45)
        teiknari.forward(260)
        teiknari.right(90)
        teiknari.penup()
        teiknari.goto(x+180, y)
        teiknari.pendown()
        teiknari.forward(260)
        teiknari.left(135)

    else:
        teiknari.penup()
        teiknari.goto(teiknari.xcor()+90, teiknari.ycor()-180)
        teiknari.pendown()
        teiknari.circle(90)

    spilari += 1

# Lyklaborð
wn.listen()

wn.onkeypress(grid_1, "7")
wn.onkeypress(grid_2, "8")
wn.onkeypress(grid_3, "9")
wn.onkeypress(grid_4, "4")
wn.onkeypress(grid_5, "5")
wn.onkeypress(grid_6, "6")
wn.onkeypress(grid_7, "1")
wn.onkeypress(grid_8, "2")
wn.onkeypress(grid_9, "3")

while(True):
    wn.update()

wn.mainloop()
