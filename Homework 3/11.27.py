# Tianhao Shao
# 1781421

'''(1)'''
team_dictionary={}

for i in range(1,6):
	jersey_num = int(input("Enter player {}'s jersey number:\n". format(i)))
	rating = int(input("Enter player {}'s rating:\n". format(i)))
	print()
	if jersey_num<0 and jersey_num>99 and rating<0 and rating>9:
		print('invalid entry')
		break
	else:
		team_dictionary[jersey_num]=rating

print('ROSTER')
for jersey_num,rating in sorted(team_dictionary.items()):
	print('Jersey number: {}, Rating: {}'. format(jersey_num,rating))

'''(2)'''

option = ''
while option.lower()!='q':
	print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')
	option=input('Choose an option:\n')
	
	if option.lower() == 'o':
		print('\nROSTER')
		for jersey_num,rating in sorted(team_dictionary.items()):
			print('Jersey number: {}, Rating: {}'. format(jersey_num,rating))
	
	elif option.lower() == 'a':
		jersey_num = int(input("Enter a new player's jersey number:\n"))
		rating = int(input("Enter the player's rating:\n"))
		if jersey_num<0 and jersey_num>99 and rating<0 and rating>9:
			print('invalid entry')
			break
		else:
			team_dictionary[jersey_num]=rating
			
	elif option.lower() == 'd':
		del_jersey_num=int(input('Enter a jersey number:\n'))
		if del_jersey_num in team_dictionary.keys():
			del team_dictionary[del_jersey_num]
	
	elif option.lower() == 'u':
		rerating_jersey_num = int(input('Enter a jersey number:\n'))
		if rerating_jersey_num in team_dictionary.keys():
			rerating=int(input('Enter a new rating for player:\n'))
			team_dictionary[rerating_jersey_num]=rerating
	
	elif option.lower() == 'r':
		rating_above = int(input('Enter a rating:\n'))
		print('\nABOVE {}'. format(rating_above))
		for jersey_num,rating in sorted(team_dictionary.items()):
			if rating > rating_above:
				print('Jersey number: {}, Rating: {}'. format(jersey_num,rating))