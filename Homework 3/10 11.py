# Tianhao Shao
# 1781421

class Triangle:   
	def __init__(self):
		self.base = 0
		self.height = 0

	def set_base(self, user_base):
		self.base = user_base

	def set_height(self, user_height):
		self.height = user_height
   
	def get_area(self):
		area = 0.5 * self.base * self.height
		return area
   
	def print_info(self):
		print('Base: {:.2f}'.format(self.base))
		print('Height: {:.2f}'.format(self.height))
		print('Area: {:.2f}'.format(self.get_area()))

if __name__ == "__main__":
	triangle1 = Triangle()
	triangle2 = Triangle()
	
	triangle1.set_base(float(input()))
	triangle1.set_height(float(input()))  

	triangle2.set_base(float(input()))
	triangle2.set_height(float(input())) 	  

	print('Triangle with larger area:')
	if triangle1.get_area() > triangle2.get_area():
		print(triangle1.print_info())
	else:
		print(triangle2.print_info())

