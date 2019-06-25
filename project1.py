from turtle import *
import turtle
import math
images=["pacman-r 1.gif","bg.gif","ghost 1.gif"]
for image in images:
    turtle.register_shape(image)
wm =turtle.Screen()
wm.bgpic("bg.gif")
wm.title("PACMAN")
wm.setup(750,550)

class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.shapesize(1)
        self.penup()
        self.speed(0)
class Coin(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5)
        self.penup()
        self.speed(0)
class Player(turtle.Turtle):
    def __init__(self):
        #turtle.addshape("pacman2.gif")
        turtle.Turtle.__init__(self)
        self.shape("pacman-r 1.gif")
        self.color("white")
        self.shapesize(0.7)
        self.penup()
        self.speed(0)
class Ghost(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("ghost 1.gif")
        self.penup()
        self.speed(0)

levels=[]

def setup_level(level,height,width):
    for y in range(len(level)):
        for x in range(len(level[y])):

            char = level[y][x]
            screen_x =-130+(x*24)
            screen_y =70-(y*24)

            if char == "1":
                wall.goto(screen_x,screen_y)
                wall.stamp()
                walls.append((screen_x,screen_y))
            elif char =="2":
                coin.goto(screen_x,screen_y)
                coin.stamp()
                coins.append((screen_x,screen_y))
            elif char == "P":
                player.goto(screen_x,screen_y)


def readFILE(arr,path):
    global height, width
    file = open(path, "r")
    hw = []
    hw.append(file.readline().split())
    height = int(hw[0][0])
    width = int(hw[0][1])
    l = 1
    for line in file:
        if l <= width:
            arr.append(line.split())
            l = l + 1
        else:
            pos.append(line.split())

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if int(pos[0][0]) == y and int(pos[0][1]) == x:
                arr[y][x] = "P"

    file.close()
    return


if __name__=="__main__":
    map = int(Screen().numinput("Choose map","Enter map(from 1 to 5)",1,1,5))
    lev = int(Screen().numinput("Choose level", "Enter level(from 1 to 4)", 1, 1, 4))
    levels = []
    level1 = []
    walls = []
    coins = []
    height = 0
    width = 0
    pos=[]
    wall = Wall()
    coin = Coin()
    player = Player()
    if map == 1 and lev == 1:
        readFILE(level1,"input.txt")
        setup_level(level1, height, width)
    elif map == 2 and lev == 1:
        readFILE(level1,"input2.txt")
        setup_level(level1,height,width)

turtle.done()