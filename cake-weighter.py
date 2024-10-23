import tkinter

# Define and initialize constants

PROGRAM_NAME = "Cake Weighter 🍰"
PROGRAM_DESCRIPTION = "Input the weights of your cakes, and see statistics!"
NUMBER_OF_CAKES = 3
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1000

# Define and initialize variables with default values

weight_input = -1 # Variable to store whatever weight the user typed in, as a float
weight_input_is_ongoing = True # Variable to store whether or not the app is in input mode
weight_input_current_cake_type = "" # Variable to store the selected cake type when in input mode

cake_a_weight = 0 # Weight of Cake A (Chocolate)
cake_b_weight = 0 # Weight of Cake B (Vanilla)
cake_c_weight = 0 # Weight of Cake C (Orange)
cake_total_weight = 0 # Total weight of all cakes

cake_a_percent = 0 # Precise percentage of total weight that is Cake A (Chocolate)
cake_b_percent = 0 # Precise percentage of total weight that is Cake B (Vanilla)
cake_c_percent = 0 # Precise percentage of total weight that is Cake C (Orange)

num_of_grid_items_cake_a = 0 # Number of grid cells that Cake A uses
num_of_grid_items_cake_b = 0 # Number of grid cells that Cake B uses
num_of_grid_items_cake_c = 0 # Number of grid cells that Cake C uses
num_of_grid_items_last_row = 0 # Number of grid cells in last row

cell_color = "" # Current color being used to color cells

'''
S T A R T U P  A N D  I N P U T  F L O W
'''

# Startup UI

print ()
print ("|=======================================================|")
print ("| ", PROGRAM_NAME, "                                    |")
print ("| ", PROGRAM_DESCRIPTION, "|")
print ("|=======================================================|")
print ()

# Input flow: get and and process user input

while (weight_input_is_ongoing == True) :
    # Prompts the user for which predefined cake type
    # This can go as many times as they want, with the user being able to add as many amounts as they like

    print (
        "Select the type of cake you would like to add a weight for,",
        "by typing the letter:"
    )
    print ("🍫 [A] Chocolate")
    print ("🍦 [B] Vanilla")
    print ("🍊 [C] Orange")
    print ("")
    print ("🛑 Type [D] to exit input, and see statistics. 🛑")
    print ("")

    weight_input_current_cake_type = input ("         Letter: ")

    # Signify they are done by entering D
    if (weight_input_current_cake_type == "D") :
        weight_input_is_ongoing = False
    else:
        # Prompts user for weight of each type
        weight_input = float (
            input ("Weight in grams: ")
        )

        # Add weight to running total for cake type
        if (weight_input_current_cake_type == "A") :
            cake_a_weight = cake_a_weight + weight_input
        elif (weight_input_current_cake_type == "B") :
            cake_b_weight = cake_b_weight + weight_input
        else :
            cake_c_weight = cake_c_weight + weight_input

        # Display running total of each type
        print ()
        print ("|—————————————————|")
        print ("| STATS SO FAR    |")
        print ("|—————————————————|")
        print ("| [A] Chocolate   | ", round (cake_a_weight, 1) , "grams")
        print ("| [B] Vanilla     | ", round (cake_b_weight, 1) , "grams")
        print ("| [C] Orange      | ", round (cake_c_weight, 1) , "grams")
        print ("|—————————————————|")
        print ()
        print ()
        print ()
        print ()
        print ()

# Calculate total weight of all the cakes
cake_total_weight = cake_a_weight + cake_b_weight + cake_c_weight

# If user typed invalid inputs, warn them
if (cake_total_weight == 0) :
	print ("You haven't entered any weights, so the app is about to break.")

# Calculate percentage of the total weight that each cake type makes up
cake_a_percent = (cake_a_weight / cake_total_weight) * 100
cake_b_percent = (cake_b_weight / cake_total_weight) * 100
cake_c_percent = (cake_c_weight / cake_total_weight) * 100

# Print table
print ()
print ("|—————————————————|")
print ("| TOTAL           | ", round (cake_total_weight, 1) , "grams")
print ("|—————————————————|")
print ("| [A] Chocolate   | ", round (cake_a_weight, 1) , "grams", "---", round (cake_a_percent) , "percent of total")
print ("| [B] Vanilla     | ", round (cake_b_weight, 1) , "grams", "---", round (cake_b_percent) , "percent of total")
print ("| [C] Orange      | ", round (cake_c_weight, 1) , "grams", "---", round (cake_c_percent) , "percent of total")
print ("|—————————————————|")
print ()

'''
S E T  U P  T K I N T E R
'''

# GUI setup boilerplate

window = tkinter.Tk () # Set window to be a new Tk
window.geometry ("1000x500") # Make window width 1000px, height 500px
window.title ("Cake Weighter")
canvas = tkinter.Canvas (window, bg = "white", width = WINDOW_WIDTH, height = WINDOW_HEIGHT)

'''
S H O W  B A R  C H A R T
'''

# Show icons above bars
# In case a bar is tiny, we'd still like the user to know it's there
# Makes things less confusing that way

canvas.create_oval (125, 25, 175, 75, fill = "red", outline = "red")
canvas.create_rectangle (225, 25, 275, 75, fill = "green", outline = "green")
canvas.create_polygon (325, 50, 350, 25, 375, 50, 350, 75, fill = "blue", outline = "blue")

# Create bars in chart

canvas.create_rectangle (100, WINDOW_HEIGHT, 200, WINDOW_HEIGHT - cake_a_percent * 4, fill = "red", outline = "red")
canvas.create_rectangle (200, WINDOW_HEIGHT, 300, WINDOW_HEIGHT - cake_b_percent * 4, fill = "green", outline = "green")
canvas.create_rectangle (300, WINDOW_HEIGHT, 400, WINDOW_HEIGHT - cake_c_percent * 4, fill = "blue", outline = "blue")

'''
S H O W  G R I D
Uses a grid to represent proportions
'''

# Create a rectangle that takes up the whole right half of space

canvas.create_rectangle ((WINDOW_WIDTH / 2), WINDOW_HEIGHT, WINDOW_WIDTH, 0)

# Round them all
# If it's below/above 100 (unlikely) it won't be by much
# So, just adjust the number of grid cells
# Sorry, I couldn't figure out a viable algorithm that would adjust it to 100 that only uses functions taught in class

num_of_grid_items_cake_a = round (cake_a_percent)
num_of_grid_items_cake_b = round (cake_b_percent)
num_of_grid_items_cake_c = round (cake_c_percent)

num_of_grid_items_last_row = (num_of_grid_items_cake_a + num_of_grid_items_cake_b + num_of_grid_items_cake_c) - 90

# Create all the rectangles

for i in range (90 + num_of_grid_items_last_row) :
	# Set colour
	
	if (i < num_of_grid_items_cake_a):
		cell_color = "red"
	
	elif (i < (num_of_grid_items_cake_b + num_of_grid_items_cake_a)):
		cell_color = "green"

	elif (i < (num_of_grid_items_cake_c + num_of_grid_items_cake_b + num_of_grid_items_cake_a)):
		cell_color = "blue"

	# Create cell

	if (i < 90) :
		canvas.create_rectangle (
			# For left x-border, use middle of screen + a certain column distance
			(WINDOW_WIDTH / 2) + ( (i % 10) * (WINDOW_WIDTH / 20) ),

			# For top y-border, use row number * row height
			(i // 10) * (WINDOW_HEIGHT / 10),

			# For right x-border,
			# use middle of screen + the next column's left border
			# (which is screen edge for last column)
			(WINDOW_WIDTH / 2) + ( ( (i % 10) + 1) * (WINDOW_WIDTH / 20) ),

			# For bottom y-border,
			# use next row number * row height
			( (i // 10) + 1) * (WINDOW_HEIGHT / 10),

			# Set fill to current cell color
			fill = cell_color,

			# Set outline to white
			outline = "white"
		)

	else:
		canvas.create_rectangle (
			# For left x-border,
			# use middle of screen + the column's left border
			# (which is screen edge for last column)
			# Note: this time, we're determining based on a factor of the row length
			# rather than the standard row length, 10
			(WINDOW_WIDTH / 2) + ( (i % num_of_grid_items_last_row) * (WINDOW_WIDTH / (2 * num_of_grid_items_last_row) ) ),
			
			# For top y-border, use row number * row height
			(i // 10) * (WINDOW_HEIGHT / 10),                            

			# For right x-border,
			# use middle of screen + the next column's left border
			# (which is screen edge for last column)
			# Note: this time, we're determining based on a factor of the row length
			# rather than the standard row length, 10
			(WINDOW_WIDTH / 2) + ( ( (i % num_of_grid_items_last_row) + 1) * (WINDOW_WIDTH / (2 * num_of_grid_items_last_row) ) ),
			
			# For bottom y-border,
			# use next row number * row height
			( (i // 10) + 1) * (WINDOW_HEIGHT / 10),

			# Set fill to current cell color
			fill = cell_color,

			# Set outline to white
			outline = "white"
		)

'''
SHOW GUI
'''

print ("Launching GUI...")

# Add content to canvas and launch the GUI
canvas.pack ()
window.mainloop ()