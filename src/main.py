import sys

max_x = 30
max_y = 30
m = [[0 for x in range(max_x)] for y in range(max_y)]

def print_maze(m):
    s = ""
    for x in range(30):
        for y in range(30):
            s = s + m[x][y]            
            if y == 29:
                s = s + "\n"
    print s

def set_pos(x, y, char):
    m[y][x] = char

def build_room(startX, startY, sizeX, sizeY):
    if (startX >=0 and startX+sizeX < max_x) == False:
        print "Error in building room."
        return
    elif (startY >=0 and startY+sizeY < max_y) == False:
        print "Error in building room."
        return
    for x in range(startX, startX+sizeX):
        for y in range(startY, startY+sizeY):
            m[x][y] = ' '


for x in range(30):
    for y in range(30):
        m[x][y] = '#'



build_room(23,23,3,3)

print_maze(m)
