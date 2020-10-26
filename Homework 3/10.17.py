# Tianhao Shao
# 1781421

class ItemToPurchase:
	def __init__(self, it_name="none", it_price=0, it_quant=0):
		self.item_name = it_name;
		self.item_price = it_price;
		self.item_quantity = it_quant;

	def print_item_cost(self):
		print(self.it_name + " " + str(self.it_quant) + " @ $"+str(int(self.it_price)) +" = $"+str(int(self.it_price*self.it_quant )))
			
if __name__=='__main__':
	item1 = ItemToPurchase()
	item2 = ItemToPurchase()
		
	print('Item 1')
	item1.it_name = input('Enter the item name:\n')
	item1.it_price = float(input('Enter the item price:\n'))
	item1.it_quant = int(input('Enter the item quantity:\n'))
	print('\nItem 2')
	item2.it_name = input('Enter the item name:\n')
	item2.it_price = float(input('Enter the item price:\n'))
	item2.it_quant = int(input('Enter the item quantity:\n'))
		
	print('\nTOTAL COST')
	item1.print_item_cost()
	item2.print_item_cost()
	total = (item1.it_price*item1.it_quant)+(item2.it_price*item2.it_quant)
	print('\nTotal: $'+str(int(total)))