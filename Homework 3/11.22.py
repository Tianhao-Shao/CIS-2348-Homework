# Tianhao Shao
# 1781421

list = input().split()

dic = {}

for i in list:
	if i in dic:
		dic[i] = dic[i] + 1
	else:
		dic[i] = 1

for i in list:
	print(i, dic[i])