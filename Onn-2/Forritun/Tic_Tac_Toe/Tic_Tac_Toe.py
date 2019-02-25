import turtle
import time

flag = False
flag_1 = False
spilari = 0

# Skjár
wn = turtle.Screen()
wn.title("Tic Tac Toe by Gummy27")
wn.bgcolor("white")
wn.setup(width=600, height=600)

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
    teiknari.penup()
    teiknari.goto(-290, 290)
    teiknari.pendown()
    teikna()

def grid_2():
    teiknari.penup()
    teiknari.goto(-90, 290)
    teiknari.pendown()
    teikna()

def grid_3():
    teiknari.penup()
    teiknari.goto(110, 290)
    teiknari.pendown()
    teikna()

#2 Röð
def grid_4():
    teiknari.penup()
    teiknari.goto(-290, 90)
    teiknari.pendown()
    teikna()

def grid_5():
    teiknari.penup()
    teiknari.goto(-90, 90)
    teiknari.pendown()
    teikna()

def grid_6():
    teiknari.penup()
    teiknari.goto(110, 90)
    teiknari.pendown()
    teikna()

#3 Röð
def grid_7():
    teiknari.penup()
    teiknari.goto(-290, -110)
    teiknari.pendown()
    teikna()

def grid_8():
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

    # Hringur
    teiknari.penup()
    teiknari.goto(teiknari.xcor()+95, teiknari.ycor())
    teiknari.pendown()
    teiknari.circle(90)

# Lyklaborð
wn.listen()

wn.onkeypress(grid_1, "1")
wn.onkeypress(grid_2, "2")
wn.onkeypress(grid_3, "3")
wn.onkeypress(grid_4, "4")
wn.onkeypress(grid_5, "5")
wn.onkeypress(grid_6, "6")
wn.onkeypress(grid_7, "7")
wn.onkeypress(grid_8, "8")
wn.onkeypress(grid_9, "9")

while(True):
    wn.update()

wn.mainloop()





wn.tracer(0)  # Turns off the screen updates.