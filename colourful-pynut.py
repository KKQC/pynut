#Autor: von Mehlem

#Created on: 25.02.2023
#Last update: 25.02.2023

import math
import time
import os

def clamp(x, a, b):
    return max(min(x, b), a)

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
            depth = clamp(depth, 0, 1)  # clamp the depth value between 0 and 1
            c = ".,-~:;=!*#$@"[min(int(depth * 10), 10)]
            # Add color to the character
            r = clamp(int(depth * 6), 0, 5) # red component
            g = clamp(int(depth * 12) - 6, 0, 5) # green component
            b = clamp(int(depth * 18) - 12, 0, 5) # blue component
            color_code = 16 + 36 * r + 6 * g + b # calculate the color code
            c = "\x1b[48;5;{}m{}\x1b[0m".format(color_code, c) # add color to the character
            # Append the character to the ASCII art string
            output += c
        output += "\n"
    # Return the ASCII art string
    return output



# Initialize the angles for rotation
theta = 0
phi = 0

# Set the terminal background color to black
os.system("printf '\033[48;5;0m'")

# Loop through and render each frame
while True:
    # Clear the console
    print(chr(27) + "[2J")
    # Render the current frame
    frame = render_frame(theta, phi)
    print(frame)
    # Increment the angles for the next frame
    theta += 0.01
    phi += 0.005
    # Wait a bit before rendering the next frame
    #time.sleep(0.01)
