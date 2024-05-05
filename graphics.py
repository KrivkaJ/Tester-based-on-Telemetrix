import matplotlib.pyplot as plt
from PIL import Image

# Load the image of the board
board_image = Image.open('esp-s3.png')

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Display the board image
ax.imshow(board_image)

# Dictionary to store tested pins and their positions
tested_pins = {}

# Callback function for mouse click event
def onclick(event):
    # Get the x and y coordinates of the mouse click
    x, y = event.xdata, event.ydata
    
    # Prompt user to enter the pin label
    pin_label = 'x'
    
    # Store the pin label and its position
    tested_pins[pin_label] = (x, y)
    
    # Plot the pin label on the image
    ax.text(x, y, ('this pins is', pin_label), color='lime', fontsize=12, ha='center', va='center')
    print(x, y)
    # Update the plot
    plt.draw()

# Connect the mouse click event to the callback function
fig.canvas.mpl_connect('button_press_event', onclick)

# Hide the axis
ax.axis('off')

# Show the plot
plt.show()

# Print the final positions of tested pins
print("Tested pins and their positions:")
for pin, pos in tested_pins.items():
    print(f"{pin}: {pos}")
