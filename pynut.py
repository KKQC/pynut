import math
import time

def render_frame(A, B):
    # Dimensions of the donut
    dim_a = 70
    dim_b = 70
    # Parameters for the rotation
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)
    # ASCII art string
    output = ""
    # Loop through each point in the donut
    for i in range(dim_a):
        for j in range(dim_b):
            # Calculate the coordinates after rotation
            x = sinA * (i - dim_a / 2) + cosA * (j - dim_b / 2)
            y = sinB * (j - dim_b / 2) + cosB * (i - dim_a / 2)
            z = 1.5 + math.sin(math.sqrt(x ** 2 + y ** 2) / 6.0)
            # Calculate the character to use based on depth
            depth = 0.5 * (z / (math.sqrt(x ** 2 + y ** 2) + 0.0001) + 1)
            c = ".,-~:;=!*#$@"[min(max(int(depth * 10), 0), 10)]
            # Append the character to the ASCII art string
            output += c
        output += "\n"
    # Return the ASCII art string
    return output

# Initialize the angles for rotation
theta = 0
phi = 0

# Loop through and render each frame
while True:
    # Clear the console
    print(chr(27) + "[2J")
    # Render the current frame
    frame = render_frame(theta, phi)
    print(frame)
    # Increment the angles for the next frame
    theta += 0.05
    phi += 0.02
    # Wait a bit before rendering the next frame
    time.sleep(0.01)
