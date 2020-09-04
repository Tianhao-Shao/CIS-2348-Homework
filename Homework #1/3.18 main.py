#Tianhao Shao
# 1781421

import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
	'red': 35,
	'blue': 25,
	'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height*wall_width
print('Wall area:', wall_area, 'square feet')
	
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
paint_need = round(wall_area/350,2)
print('Paint needed:', paint_need, 'gallons' )
# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
cans_need =int(round(paint_need,0))
print('Cans needed:',cans_need,'can(s)')
# FIXME (4): Calculate and output the total cost of paint can needed depending on color
color_wall = input('\nChoose a color to paint the wall:\n')
cost = paint_colors[color_wall]*cans_need
print('Cost of purchasing',color_wall,'paint: $'+str(cost))
