import turtle 
import math 

print('Turtle Draw Python :)') 

# Todo: Ask user for file name.
file_name = input("Please enter the name of the input file: ")
# Print file name.
print(f"The file name you entered is: {file_name}")

TEXTFILENAME = 'turtle-draw.txt'
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()

# Set up the screen.
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=450, height=450)

# Create turtle.
Franek = turtle.Turtle()
Franek.speed(10)
Franek.penup()

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

# Todo: Wait for the user to press the Enter key before closing.
turtleDrawTextfile.close()
input("Press Enter to exit...")
turtle.bye()

print('\nEnd')
