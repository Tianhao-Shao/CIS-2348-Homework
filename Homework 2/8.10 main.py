user_input = input()
user_input_ignspace = user_input.replace(' ','')

i = 0
ispalindrome = True

while i < len(user_input_ignspace)//2: 
	if user_input_ignspace[i]!=user_input_ignspace[-1-i]:
		ispalindrome = False
		break
	i+=1
	
if ispalindrome:
	print(user_input,'is a palindrome')
else:
	print(user_input,'is not a palindrome')