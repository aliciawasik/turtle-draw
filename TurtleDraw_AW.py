import turtle 

TEXTFILENAME = 'turtle-draw.txt'

# Todo: Ask user for the file name.

print('Turtle Draw Python :)')

Franek = turtle.Turtle()
Franek.speed(10)
Franek.penup()

print('Reading a text file line by line.')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

    
        Franek.color(color)
        Franek.goto(x,y)
        # Todo: Calculate the distance and add it to the total distance.
        Franek.pendown()

    if (len(parts) == 1): # Assumes that a single word on a line is "stop"
        Franek.penup()

    line = turtleDrawTextfile.readline()

# Todo: Print the total near the bottom.
turtle.done()
turtleDrawTextfile.close()

# Todo: Wait for the user to press the Enter key before closing.
print('\nEnd')
