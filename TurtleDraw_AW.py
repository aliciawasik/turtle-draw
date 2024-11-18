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

# Initialize variables
total_distance = 0  # To accumulate the total distance traveled

# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Read file
line = turtleDrawTextfile.readline()

# Open the input file and process its content
try:
    with open(file_name, 'r') as file:
        # Initialize start position (origin)
        current_x, current_y = 0, 0
        Franek.penup()
        Franek.goto(current_x, current_y)  # Move Franek to the origin
        Franek.pendown()

        for line in file:
            line = line.strip()  # Strip whitespace from the line
            if line:  # Only process non-empty lines
                parts = line.split()
                
                if parts[0].lower() == "stop":
                    Franek.penup()  # Lift the pen
                    print("Pen lifted, no drawing.")
                else:
                    try:
                        x, y = int(parts[0]), int(parts[1])  # Extract x and y coordinates
                        color = parts[2] if len(parts) > 2 else "black"  # Default to black if no color is specified
                        
                        Franek.color(color)  # Change the pen color
                        distance = calculate_distance(current_x, current_y, x, y)  # Calculate the distance
                        total_distance += distance  # Add to the total distance
                        
                        Franek.goto(x, y)  # Move Franek to the new position
                        Franek.pendown()  # Start drawing again
                        current_x, current_y = x, y  # Update current position
                    except (ValueError, IndexError):
                        print(f"Invalid line format: {line}")
        
        # Display total distance at the bottom right of the screen
        Franek.penup()
        Franek.goto(150, -150)
        Franek.write(f"Total distance: {total_distance:.2f} units", font=("Arial", 14, "normal"))

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Todo: Wait for the user to press the Enter key before closing.
turtleDrawTextfile.close()
input("/Press Enter to exit...")
turtle.bye()

print('\nEnd')
