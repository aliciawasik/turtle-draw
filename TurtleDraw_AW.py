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

# Calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def total_distance(points):
    total = 0
    for i in range(1, len(points)):
        total += distance(points[i-1], points[i])
    return total

# Read points from file
def read_points_from_file(file_name):
    points = []
    with open(file_name, 'r') as file:
        current_position = (0, 0)  # Start at the origin
        Franek.penup()
        Franek.goto(current_position)  # Start at (0, 0)

        for line in file:
            line = line.strip()
            if line.lower() == "stop":
                Franek.penup()  # Lift the pen
                continue  # Skip to the next line

            return_strings = line.split()

            if len(return_strings) == 3:
                color = return_strings[0]
                x = int(return_strings[1])
                y = int(return_strings[2])

                Franek.color(color)
                Franek.goto(x, y)
                Franek.pendown()

                points.append((x, y))  # Store the point

        return points

# Read points from the input file
points = read_points_from_file(file_name)

# Calculate the total distance
total = total_distance(points)
print(f"Total Distance: {total:.2f}")

# Display total distance on the screen
Franek.penup()
Franek.goto(200, -200)
Franek.pendown()
Franek.write(f"Total Distance: {total:.2f}", align="center", font=("Arial", 10, "normal"))

# Wait for user input before closing the window
input("Press Enter to exit...")
turtle.bye()
