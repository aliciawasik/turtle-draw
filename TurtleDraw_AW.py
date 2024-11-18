import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.setup(width=450, height=450)

# Create the turtle object.
Franek = turtle.Turtle()
Franek.speed(0)  # Maximum speed
Franek.width(2)

# Default color
Franek.color("black")

# Ask the user for the input file name
file_name = input("Please enter the name of the input file: ")

# Initialize variables
total_distance = 0  # To accumulate the total distance traveled

# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Open the input file and process its content
try:
    with open(file_name, 'r') as file:
        # Initialize start position (origin)
        current_x, current_y = 0, 0
        Franek.penup()
        Franek.goto(current_x, current_y)  # Move Franek to the origin
        Franek.pendown()

        # Process each line in the input file
        for line in file:
            line = line.strip()  # Strip whitespace from the line
            if line:  # Only process non-empty lines
                parts = line.split()

                # Check for 'stop' keyword
                if parts[0].lower() == "stop":
                    print("Stop command encountered. Skipping drawing segment.")
                    continue  # Skip the drawing of this segment

                if len(parts) < 3:
                    print(f"Invalid line format (too few values): {line}")
                    continue  # Skip this line if there are not enough values

                try:
                    # Parse the color (first part), and coordinates (second and third parts)
                    color = parts[0]
                    x, y = int(parts[1]), int(parts[2])

                    # Move the turtle to the new position and draw
                    Franek.color(color)  # Set the color
                    distance = calculate_distance(current_x, current_y, x, y)  # Calculate distance
                    total_distance += distance  # Add to the total distance

                    Franek.goto(x, y)  # Move Franek to the new position
                    Franek.pendown()  # Start drawing again
                    current_x, current_y = x, y  # Update current position

                except ValueError as ve:
                    print(f"Error processing line (invalid value): {line} - {ve}")
                except IndexError as ie:
                    print(f"Error processing line (missing data): {line} - {ie}")

        # Display total distance at the bottom right of the screen
        Franek.penup()
        Franek.goto(150, -150)
        Franek.write(f"Total distance: {total_distance:.2f} units", font=("Arial", 14, "normal"))

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for user to press enter before closing
input("Press Enter to exit...")
turtle.bye()  # Close the turtle graphics window
