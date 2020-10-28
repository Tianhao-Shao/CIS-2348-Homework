# Tianhao Shao
# 1781421

def selection_sort_descend_trace(numbers):
	for i in range(len(numbers)-1):
		index_max = i
		for j in range(i + 1, len(numbers)):
			if numbers[index_max] < numbers[j]:
				index_max = j
		
		temp = numbers[i]
		numbers[i] = numbers[index_max]
		numbers[index_max] = temp
		
		for num in numbers:
			print(str(num), end=' ')
		print()

		

if __name__ == '__main__':
	numbers = []
	data = input()
	numbers = [int(x) for x in data.split()]
	selection_sort_descend_trace(numbers)
	