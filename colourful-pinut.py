#Autor: von Mehlem

#Created on: 25.02.2023
#Last update: 25.02.2023

import math
import time

def render_frame(A, B):
    # Dimensions of the donut
    dim_a = 70
    dim_b = 120
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
            denom = math.sqrt(x ** 2 + y ** 2)
            if denom > 0.0001:
                depth = 0.5 * (z / denom + 1)
            else:
                depth = 0.5 * (z / max(math.sqrt(x ** 2 + y ** 2), 0.01) + 1)
            depth = min(max(depth, 0), 1)  # clamp the depth value between 0 and 1
            # Set the color based on the depth
            if depth < 0.25:
                color = "\033[38;2;255;0;0m"  # red
            elif depth < 0.5:
                color = "\033[38;2;255;165;0m"  # orange
            elif depth < 0.75:
                color = "\033[38;2;255;255;0m"  # yellow
            else:
                color = "\033[38;2;0;255;0m"  # green
            # Assign the character to use based on depth
            c = ".,-~:;=!*#$@"[min(int(depth * 14), 13)]
            # Add the colored character to the output string
            output += color + c + "\033[0m"
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
