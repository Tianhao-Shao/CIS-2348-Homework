# Tianhao Shao
# 1781421

def get_age():
	age = int(input())
	if age<18 or age>75:
		raise ValueError('Invalid age.')
	return age

def fat_burning_heart_rate(age):
	heart_rate= (220-age)*0.7
	return heart_rate

if __name__ == "__main__":
	try:
		age = get_age()
		rate = fat_burning_heart_rate(age)
		
		print('Fat burning heart rate for a {} year-old: {} bpm'. format(age,rate))
		
	except ValueError as excpt:
		print(excpt)
		print('Could not calculate heart rate info.\n')