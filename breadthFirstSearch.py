import queue

#just for test
def printMaze(maze, path=""):
    for index in range(len(maze)):
        for x, pos in enumerate(maze[index]):
            if pos == "P":
                start = x
                start_ = index

    i = start
    j = start_
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for index in range(len(maze)):
         for x, pos in enumerate(maze[index]):
             if pos == "P":
                 start = x
                 start_ = index

    i = start
    j = start_
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "1"):
            return False

    return True


def findEnd(maze, moves):
    for index in range(len(maze)):
        for x, pos in enumerate(maze[index]):
            if pos == "P":
                start = x
                start_ = index

    i = start
    j = start_
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "2":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


def readFILE(arr,path):
    pos = []
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

# MAIN ALGORITHM
nums = queue.Queue()
nums.put("")
add = ""
maze = []
readFILE(maze, "input.txt")
# print(maze)
while not findEnd(maze, add): #nếu chưa chạm đích thì tiếp tục
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)