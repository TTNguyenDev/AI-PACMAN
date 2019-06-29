from turtle import *
import turtle
import time
import queue
import math

def _Screen():
    wm =turtle.Screen()
    wm.bgpic("bg.gif")
    wm.bgcolor("black")
    wm.title("PACMAN")
    wm.setup(750,550)

class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape("square")
        self.color("blue")
        self.shapesize(1)
        self.penup()
        self.speed(0)
class Coin(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5)
        self.penup()
        self.speed(0)
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape("pacman-r 1.gif")
        self.shapesize(0.7)
        self.penup()
        self.speed(0)
class Ghost(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape("ghost 1.gif")
        self.penup()
        self.speed(0)
class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.goto(-240, -260)
        self.color("yellow")
        self.write("Score:", move=False, align="center", font=("Arial", 36, "normal"))
        self.speed(0)

def setup_level(level,height,width,pos1):
    for y in range(len(level)):
        for x in range(len(level[y])):
            char = level[y][x]
            screen_x = -130+(x*24)
            screen_y = 70-(y*24)
            if char == "1":
                wall.showturtle()
                wall.goto(screen_x,screen_y)
                wall.stamp()
                walls.append((screen_x,screen_y))
            elif char == "2":
                coin.showturtle()
                coin.goto(screen_x,screen_y)
                coin.stamp()
                coins.append((screen_x,screen_y))
            elif char == "3":
                ghost.showturtle()
                ghost.goto(screen_x,screen_y)
                ghost.stamp()
                ghosts.append((screen_x,screen_y))
            elif char == "P":
                player.showturtle()
                player.goto(screen_x,screen_y)
                pos1.append((screen_x,screen_y))

class White(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.shapesize(1)
        self.penup()
        self.speed(0)

def Move(maze,x,y,add):
    white=White()
    for i in range(len(add)):
        if(add[i]=="L"):
            player.goto(x-24,y)
            white.goto(x,y)
            white.stamp()
            time.sleep(0.5)
            x=x-24
        if (add[i] == "R"):
            player.goto(x + 24, y)
            white.goto(x, y)
            white.stamp()
            time.sleep(0.5)
            x = x + 24
        if (add[i] == "U"):
            player.goto(x, y+24)
            white.goto(x, y)
            white.stamp()
            time.sleep(0.5)
            y = y + 24
        if (add[i] == "D"):
            player.goto(x , y - 24)
            white.goto(x, y)
            white.stamp()
            time.sleep(0.5)
            y = y - 24

def readFILE(arr,path,pos,coins1):
    global height, width
    file = open(path, "r")
    hw = []
    hw.append(file.readline().split())
    width = int(hw[0][0])
    height = int(hw[0][1])
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
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == "2":
                coins1.append((y,x))
    file.close()
    return

def updateScore():
    global scores
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    s.goto(-110,-260)
    while True:
        score =Score()
        s.write(str(scores), move=False, align="center", font=("Arial", 36, "normal"))
        s.color("yellow")
        scores +=1
        time.sleep(0.5)
        s.clear()

def valid(map, moves):
    column, row = updatePacmanPosition(map, moves)

    #out of range
    if not (0 <= column < len(map[0]) and 0 <= row < len(map)):
        return False
    elif (map[row][column] == "1"): #1 represent wall
        return False
    elif (map[row][column] == "3"): #3 represent enemy
        return False

    return True

def updatePacmanPosition(map, moves):
    global column, row
    for index in range(len(map)):
        for x, pos in enumerate(map[index]):
            if pos == "P":
                column = x
                row = index

    for move in moves:
        if move == "L":
            column -= 1

        elif move == "R":
            column += 1

        elif move == "U":
            row -= 1

        elif move == "D":
            row += 1

    return column, row

def findEnd(map, moves):
    column, row = updatePacmanPosition(map, moves)

    # 2 represent food
    if map[row][column] == "2":
        return True

    return False

def level1_map1(level,pos,coin1):
    global add
    readFILE(level, "input1.txt",pos,coins1)
    setup_level(level, height, width,pos1)
    while not findEnd(level, add):  # nếu chưa chạm đích thì tiếp tục
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(level, put):
                nums.put(put)
    Move(level, int(pos1[0][0]), int(pos1[0][1]),add)

def level2_map1(level1,pos,coins1):
    global add2
    readFILE(level1, "input1_2.txt",pos,coins1)
    setup_level(level1, height, width,pos1_2)
    while not findEnd(level1, add2):  # nếu chưa chạm đích thì tiếp tục
        add2 = nums2.get()
        for j in ["L", "R", "U", "D"]:
            put = add2 + j
            if valid(level1, put):
                nums2.put(put)
    Move(level1, int(pos1_2[0][0]), int(pos1_2[0][1]),add2)

def level1_map2(level1,pos,coins1):
    global add
    readFILE(level1, "input2.txt",pos,coins1)
    setup_level(level1, height, width,pos1)
    while not findEnd(level1, add):  # nếu chưa chạm đích thì tiếp tục
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(level1, put):
                nums.put(put)
    Move(level1, int(pos1[0][0]), int(pos1[0][1]),add)

def level2_map2(level1,pos,coins1):
    global add2
    readFILE(level1, "input2_2.txt",pos,coins1)
    setup_level(level1, height, width,pos1_2)
    while not findEnd(level1, add2):  # nếu chưa chạm đích thì tiếp tục
        add2 = nums2.get()
        for j in ["L", "R", "U", "D"]:
            put = add2 + j
            if valid(level1, put):
                nums2.put(put)
    Move(level1, int(pos1_2[0][0]), int(pos1_2[0][1]),add2)

def level1_map3(level1,pos,coins1):
    global add
    readFILE(level1, "input3.txt",pos,coins1)
    setup_level(level1, height, width,pos1)
    while not findEnd(level1, add):  # nếu chưa chạm đích thì tiếp tục
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(level1, put):
                nums.put(put)
    Move(level1, int(pos1[0][0]), int(pos1[0][1]),add)

def level2_map3(level1,pos,coins1):
    global add2
    readFILE(level1, "input3_2.txt",pos,coins1)
    setup_level(level1, height, width,pos1_2)
    while not findEnd(level1, add2):  # nếu chưa chạm đích thì tiếp tục
        add2 = nums2.get()
        for j in ["L", "R", "U", "D"]:
            put = add2 + j
            if valid(level1, put):
                nums2.put(put)
    Move(level1, int(pos1_2[0][0]), int(pos1_2[0][1]),add2)
def level1_map4(level1,pos,coins1):
    global add
    readFILE(level1, "input4.txt",pos,coins1)
    setup_level(level1, height, width,pos1)
    while not findEnd(level1, add):  # nếu chưa chạm đích thì tiếp tục
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(level1, put):
                nums.put(put)
    Move(level1, int(pos1[0][0]), int(pos1[0][1]),add)

def level2_map4(level1,pos,coins1):
    global add2
    readFILE(level1, "input4_2.txt",pos,coins1)
    setup_level(level1, height, width,pos1_2)
    while not findEnd(level1, add2):  # nếu chưa chạm đích thì tiếp tục
        add2 = nums2.get()
        for j in ["L", "R", "U", "D"]:
            put = add2 + j
            if valid(level1, put):
                nums2.put(put)
    Move(level1, int(pos1_2[0][0]), int(pos1_2[0][1]),add2)

def level1_map5(level1,pos,coins1):
    global add
    readFILE(level1, "input5.txt",pos,coins1)
    setup_level(level1, height, width,pos1)
    while not findEnd(level1, add):  # nếu chưa chạm đích thì tiếp tục
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(level1, put):
                nums.put(put)
    Move(level1, int(pos1[0][0]), int(pos1[0][1]),add)

def level2_map5(level1,pos,coins1):
    global add2
    readFILE(level1, "input5_2.txt",pos,coins1)
    setup_level(level1, height, width,pos1_2)
    while not findEnd(level1, add2):  # nếu chưa chạm đích thì tiếp tục
        add2 = nums2.get()
        for j in ["L", "R", "U", "D"]:
            put = add2 + j
            if valid(level1, put):
                nums2.put(put)
    Move(level1, int(pos1_2[0][0]), int(pos1_2[0][1]),add2)

if __name__=="__main__":
    _Screen()
    images = ["pacman-r 1.gif", "bg.gif", "ghost 1.gif"]
    for image in images:
        turtle.register_shape(image)
    map = int(Screen().numinput("Choose map","Enter map(from 1 to 5)",1,1,5))
    level1 = []
    level2 = []
    walls = [] #vector cua wall
    coins = [] #vector cua coin
    ghosts =[]  #vector cua ghost
    coins1 = [] #vi tri cua coin level1
    coins2= [] #vi tri cua coin level2

    pos = [] # vi tri vector cua player level1
    pos_2 = [] #vi tri vector cua player level2

    pos1 = []  # vi tri cua player level1 trong mang
    pos1_2 =[]  # vi tri cua player level2 trong mang
    scores = 0
    height = 0
    width = 0
    start = 0
    start_ = 0
    wall = Wall()
    coin = Coin()
    player = Player()
    ghost=Ghost()
    nums = queue.Queue()#cua level1
    nums.put("")
    nums2 = queue.Queue() #cua level2
    nums2.put("")
    add = "" #duong di cua level 1
    add2 ="" #duong di cua level 2
    if map == 1:
        level1_map1(level1,pos,coins1)
        time.sleep(1)
        Screen().clear()
        _Screen()
        coin = Coin()
        wall = Wall()
        player = Player()
        ghost = Ghost()
        level2_map1(level2,pos_2,coins2)
    elif map == 2:
        level1_map2(level1,pos,coins1)
        time.sleep(1)
        Screen().clear()
        _Screen()
        coin = Coin()
        wall = Wall()
        player = Player()
        ghost = Ghost()
        level2_map2(level2, pos_2, coins2)
    elif map == 3:
        level1_map3(level1,pos,coins1)
        time.sleep(1)
        Screen().clear()
        _Screen()
        coin = Coin()
        wall = Wall()
        player = Player()
        ghost = Ghost()
        level2_map3(level2, pos_2, coins2)
    elif map == 4:
        level1_map4(level1,pos,coins1)
        time.sleep(1)
        Screen().clear()
        _Screen()
        coin = Coin()
        wall = Wall()
        player = Player()
        ghost = Ghost()
        level2_map4(level2, pos_2, coins2)
    elif map == 5:
        level1_map5(level1,pos,coins1)
        time.sleep(1)
        Screen().clear()
        _Screen()
        coin = Coin()
        wall = Wall()
        player = Player()
        ghost = Ghost()
        level2_map5(level2, pos_2, coins2)
turtle.done()