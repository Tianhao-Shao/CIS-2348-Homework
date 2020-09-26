# Tianhao Shao
# 1781421

''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
def fun1(x,y):
	return a*x + b*y - c
def fun2(x,y):
	return d*x + e*y - f
'''Set x y where not in range (-10,11)'''
finalx =11 
finaly =11
for x in range(-10,11):
	for y in range(-10,11):
		if fun1(x, y)== fun2(x, y) and fun1(x, y)==0:
			finalx = x
			finaly = y
'''set finalx != 11,if loop didnt go through, final still = to 11'''
if finalx != 11:
	print(finalx, finaly)
else:
	print('No solution')
