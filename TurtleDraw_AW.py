import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.setup(width=450, height=450)

# Create the turtle object
Franek = turtle.Turtle()
Franek.speed(10)

# Ask the user for the input file name
file_name = input("Please enter the name of the input file: ")

TEXTFILENAME = 'turtle-draw.txt'
turtleDrawTextFile = open(TEXTFILENAME, 'r')
line = turtleDrawTextFile.readline()

# Calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def total_distance(points):
    total = 0
    for i in range(1, len(points)):
        total += distance(points[i-1], points[i])
    return total

# Read points from file
def read_points_from_file(TEXTFILENAME):
    points = []
    with open(TEXTFILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            returnStrings = line.split()
            if len(returnStrings) == 1:
                Franek.penup()
            elif len(returnStrings) == 3:
                colors = returnStrings[0]
                x = int(returnStrings[1])
                y = int(returnStrings[2])
                
                Franek.color(colors)
                Franek.goto(x, y)
                Franek.pendown()
                points.append((x, y)) 
    return points

# Read points from the text file
points = read_points_from_file(TEXTFILENAME)

# Calculate the total distance
total = total_distance(points)
print(f"Total Distance: {total:.2f}")


Franek.penup()
Franek.goto(200, -250)
Franek.pendown()
Franek.write(f"Total Distance: {total:.2f}", align="center", font=("Arial", 10, "normal"))

input("Press Enter to exit...")
turtle.bye()  
