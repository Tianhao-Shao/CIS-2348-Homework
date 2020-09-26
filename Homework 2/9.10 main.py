# Tianhao Shao
# 1781421

import csv

#Enter the file name:
file = input()
#make dic for frequency
frequency = {}

with open(file, 'r') as csvfile:
	csvfile = csv.reader(csvfile)
	
	for row in csvfile:
		for word in row:
			if word not in frequency.keys():
				frequency[word] = 1
			else:
				frequency[word] =frequency[word]+ 1
for key in frequency.keys():

	print(key + " " + str(frequency[key])) 
