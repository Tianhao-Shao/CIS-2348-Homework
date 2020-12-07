import csv
import datetime

products = []
today = datetime.datetime.now()
with open('FullInventory.csv', 'r') as f:
    products_list = csv.reader(f)
    for row in products_list:
        d = row[4]
        d = datetime.datetime.strptime(d, "%m/%d/%Y")
        if d > today:  # ensure only the service date has not been reached
            for x in range(len(row)):
                r = row[x]  # remove white spaces
                r = r.strip()
                row[x] = r
            products.append(row)
        # print(row)

# clean the products to remove the damaged ones
products = [products[x] for x in range(len(products)) if products[x][5] == '']

# sort products by most expensive
products = sorted(products, key=lambda product: product[3])
products = products[::-1]
# print(products)

items = {}
for x in range(len(products)):
    product = products[x]
    if product == []:
        continue
    pid = product[0]
    supplier = product[1]
    itemtype = product[2]
    price = product[3]
    time = product[4]
    state = product[5]

    if itemtype not in items:
        items[itemtype] = {supplier: [pid, price, time, state]}
    else:
        if supplier in items[itemtype]:  # many items with same supplier
            if type(items[itemtype][supplier][0]) == list:  # more then one items was added
                items[itemtype][supplier].append(
                    [[pid, price, time, state]])  # if already 2 or more products add another
            else:
                items[itemtype][supplier] = [items[itemtype][supplier], [pid, price, time, state]]
        else:
            items[itemtype][supplier] = [pid, price, time, state]
# print(items)

def menu():
    global items
    print("-------------------------------------------------------------")

    supplier = input("Please enter the supplier name: ")
    item_type = input("Enter the item type: ")
    # strip spaces
    supplier = supplier.lower().strip()
    item_type = item_type.lower().strip()

    itype = None

    # i
    if item_type not in items:
        for x in items:
            if x in item_type:  # eliminate unnecessary user inputs
                itype = x
        if itype == None:
            print('No such item in inventory')
            return
    # ii
    if itype == None:
        itype = item_type
    selected = None  # the selected item
    if itype != None:
        # get for the right manufacturer
        item_type = itype
        suppliers = items[item_type]
        found = False
        supplier = supplier[0:1].upper() + supplier[1:]

        if supplier in suppliers:
            item = suppliers[supplier]
            selected = item
            print(f'Your item is: {item[0][0]} {supplier} {item_type} {item[0][1]}')
            found = True
        if not found:
            supplier = supplier[0].upper() + supplier[1:]
            if supplier in suppliers:
                item = suppliers[supplier]
                # check if the items are more than one
                if type(item[0]) == list:
                    topitem = item[0]
                    for it in item:
                        if it[1] > topitem[1]:
                            topitem = it
                    print(f'Your item is: {topitem[0][0]} {supplier} {item_type} {topitem[0][1]}')
                else:
                    print(f'Your item is: {item[0][0]} {supplier} {item_type} {item[0][1]}')
        # iii
        print('You may also consider: ')
        oit=[]
        for x in suppliers:
            # check if the items are more than one
            if type(suppliers[x][0]) == list:
                for s in suppliers[x]:
                    sup = s
                    if selected != sup:
                        # print(f'{sup[0]} {x} {item_type} {sup[1]}')
                        oit.append(sup)
            else:
                if selected != suppliers[x]:
                    # print(f'{suppliers[x][0]} {x} {item_type} {suppliers[x][1]}')
                    oit.append(suppliers[x])
        # print(oit)
        # print(suppliers)
        print(f'{oit[0][0]} {list(suppliers.keys())[0]} {item_type} {oit[0][1]}')


def main():
    while True:
        print("\n......................Menu...................................")
        print("q -- exits the application")
        print("any other key searches for products")
        print("-------------------------------------------------------------")
        choice = input("Enter command: ")
        choice = choice.lower().strip()
        if choice == 'q':
            break
        else:
            menu()


if __name__ == "__main__":
    main()
