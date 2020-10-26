# Tianhao Shao
# 1781421

user_input=input().split()

result=[]

for num in user_input:
	num=int(num)
	if num>=0:
		result.append(num)
result.sort()
for num in result:
	print(num,end=' ')