print("Davy's auto shop services")
print('Oil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')

user_service = {'-':0,'Oil change':35, 'Tire rotation':19, 'Car wash':7, 'Car wax':12}

user_service1 = input('Select first service:\n')
user_service2 = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")

if user_service1 == 'Oil change':
	print('Service 1: Oil change, $35')
elif user_service1 == 'Tire rotation':
	print('Service 1: Tire rotation, $19')
elif user_service1 == 'Car wash':
	print('Service 1: Car wash, $7')
elif user_service1 == 'Car wax':
	print('Service 1: Car wax, $12')
elif user_service1 == '-':
	print('Service 1: No service')

if user_service2 == 'Oil change':
	print('Service 2: Oil change, $35')
elif user_service2 == 'Tire rotation':
	print('Service 2: Tire rotation, $19')
elif user_service2 == 'Car wash':
	print('Service 2: Car wash, $7')
elif user_service2 == 'Car wax':
	print('Service 2: Car wax, $12')
elif user_service2 == '-':
	print('Service 2: No service')

invoice_total = user_service[user_service1] + user_service[user_service2]

print('\nTotal: ${}'. format(invoice_total))