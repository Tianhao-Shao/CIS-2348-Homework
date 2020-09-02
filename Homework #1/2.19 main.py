#Tianhao Shao
#1781421

# FIXME (1): Finish reading other items into variables, then output the three ingredients
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
nectar_cpus = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups))
print('{:.2f} cup(s) water'.format(water_cups))
print('{:.2f} cup(s) agave nectar'.format(nectar_cpus))
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
total_useruse_amount = float(input('\nHow many servings would you like to make?\n'))
total_lemon_juice_cups = total_useruse_amount/servings*lemon_juice_cups
total_water_cups =total_useruse_amount/servings*water_cups
total_nectar_cpus =total_useruse_amount/servings*nectar_cpus

print('\nLemonade ingredients - yields {:.2f} servings'.format(total_useruse_amount))
print('{:.2f} cup(s) lemon juice'.format(total_lemon_juice_cups))
print('{:.2f} cup(s) water'.format(total_water_cups))
print('{:.2f} cup(s) agave nectar'.format(total_nectar_cpus))
# FIXME (3): Convert and output the ingredients from (2) to gallons

print('\nLemonade ingredients - yields {:.2f} servings'.format(total_useruse_amount))
lemon_juice_gallons=total_lemon_juice_cups/16
water_gallons=total_water_cups/16
nectar_gallons=total_nectar_cpus/16
print('{:.2f} gallon(s) lemon juice'.format(lemon_juice_gallons)) 
print('{:.2f} gallon(s) water'.format(water_gallons))
print('{:.2f} gallon(s) agave nectar'.format(nectar_gallons))