# Tianhao Shao
# 1781421

class ItemToPurchase:

    def __init__(self, it_name="none", it_price=0, it_quant=0, it_desc="none"):
        self.item_name = it_name;
        self.item_price = it_price;
        self.item_quantity = it_quant;
        self.item_description = it_desc;

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
            self.item_quantity * self.item_price));

    def print_item_description(self):
        print(self.item_name + ": " + self.item_description);


class ShoppingCart:

    def __init__(self, cust_name="none", curr_date="January 1, 2016", cartList=[]):
        self.customer_name = cust_name
        self.current_date = curr_date
        self.cart_items = cartList

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, it_name):
        for obj in self.cart_items:
            if (obj.item_name == it_name):
                self.cart_items.remove(obj)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        item_found = False
        for obj in range(0, len(self.cart_items)):
            if self.cart_items[obj].item_name == ItemToPurchase.item_name:
                item_found = True
                self.cart_items[obj].item_quantity = ItemToPurchase.item_quantity
                break

        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for obj in self.cart_items:
            total_quantity = total_quantity + obj.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for obj in self.cart_items:
            total_cost = total_cost + (obj.item_price * obj.item_quantity)
        return total_cost

    def print_total(self):
        if (len(self.cart_items) != 0):
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: " + str(self.get_num_items_in_cart()) + "\n")
            for obj in self.cart_items:
                obj.print_item_cost()
            print("\nTotal: $" + str(self.get_cost_of_cart()))
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: 0")
            print("\nSHOPPING CART IS EMPTY\n")
            print('Total: $0')

    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("\nItem Descriptions")
        for obj in self.cart_items:
            obj.print_item_description()


def print_menu(self):
    menu = '\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items\' descriptions\no - Output shopping cart\nq - Quit\n'
    choice = ''

    while (choice != 'q'):
        print(menu)
        choice = input('Choose an option:\n')
        while choice != 'a' and choice != 'o' and choice != 'i' and choice != 'r' and choice != 'c' and choice != 'q':
            choice = input('Choose an option:\n')

        if choice == 'a':
            print("ADD ITEM TO CART")
            it_name = input("Enter the item name:\n")
            it_desc = input("Enter the item description:\n")
            it_price = int(input("Enter the item price:\n"))
            it_quant = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(it_name, it_price, it_quant, it_desc)
            self.add_item(item)

        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            it_name = input("Enter name of item to remove:\n")
            self.remove_item(it_name)

        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            it_name = input("Enter the item name:\n")
            it_quant = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(it_name, 0, it_quant, None)
            self.modify_item(item)

        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            self.print_descriptions()

        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            self.print_total()

if __name__=='__main__':
    print("Enter customer's name:")
    cust_name = input()
    print("Enter today's date:")
    cur_date = input()
    shCart = ShoppingCart(cust_name, cur_date)
    print("\nCustomer name: " + shCart.customer_name)
    print("Today's date: " + shCart.current_date)

    print_menu(shCart)

