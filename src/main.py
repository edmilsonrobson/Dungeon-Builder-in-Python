import random

max_x = 50
max_y = 50
m = [[0 for x in range(max_x)] for y in range(max_y)]
number_rooms = random.randint(10,15)

random_points = []

def print_maze(m):
    s = ""
    for x in range(max_x):
        for y in range(max_y):
            s = s + m[x][y]            
            if y == max_y-1:
                s = s + "\n"
    print s

def set_pos(x, y, char):
    m[y][x] = char

def break_block(x, y):
    m[x][y] = ' '

def build_room(startX, startY, sizeX, sizeY):
    if (startX >0 and startX+sizeX < max_x-1) == False:
        print "Error in building room."
        return False
    elif (startY >0 and startY+sizeY < max_y-1) == False:
        print "Error in building room."
        return False
    for x in range(startX, startX+sizeX):
        for y in range(startY, startY+sizeY):
            break_block(x,y)
            random_points.append([random.randint(startX,startX+sizeX), random.randint(startY,startY+sizeY)])
    return True





def build_maze():

    #Initializes all positions with blocks (#)
    for x in range(max_x):
        for y in range(max_y):
            m[x][y] = '#'
            
    #Builds a "central" room first, with variable size.
    build_room(max_x/3+random.randint(0,6), max_y/3 + random.randint(0,6), 3+random.randint(3,6), 3+random.randint(3,6))

    #Builds a few random other rooms in random places. Can overlap!
    for i in range(number_rooms):
        build_room(random.randint(1,max_x-7), random.randint(1,max_y-7), random.randint(3,7), random.randint(3,7))

    #Tries to connect all the rooms!
        
    for index, value in enumerate(random_points):
        if (index < len(random_points)-1):            
            p1 = value
            p2 = random_points[index+1]
            for x in range(p1[0], p2[0]):
                break_block(x,p1[1])
            for y in range(p1[1], p2[1]):
                break_block(p1[1],y)
    
        


build_maze()

print_maze(m)

print "A total of %d rooms were built." % number_rooms
