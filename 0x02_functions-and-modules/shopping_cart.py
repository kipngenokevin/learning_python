#!/usr/bin/python3

class ProductNode:
    """This class holds the content of a product added to the cart"""
    def __init__(self, product_id, name, size, color, quantity, price):
        self.product_id = product_id
        self.name = name
        self.size = size
        self.color = color
        self.quantity = quantity
        self.price = price
        self.next = None

class ShoppingCart:
    """This is a class that initializes the shopping cart"""
    def __init__(self):
        """Here is an initialization of some variables used for total quantity and price"""
        self.head = None
        self.total_items = 0
        self.total_price = 0

    def add_product(self, product_id, name, size, color, quantity, price):
        """This function creates a new instance of the class ProductNode"""
        new_product = ProductNode(product_id, name, size, color, quantity, price)
        new_product.next = self.head
        self.head = new_product
        self.total_items += quantity
        self.total_price += quantity * price

    def display_cart(self):
        """This function displays the items in the cart"""
        current = self.head
        item_number = 1
        while current:
            print("Item_number {}".format(item_number))
            print("Product Name: {}".format(current.name))
            print("Product Quantity: {}".format(current.quantity))
            print("Product price: {}".format(current.price * current.quantity))
            current = current.next
            item_number += 1

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(1, 'Versece', 'large', 'blue', 2, 4500)
    cart.add_product(2, 'Balenciaga', '23x45', 'blue', 2, 9000)
    print("Total items {}".format(cart.total_items))
    print("Total price {}".format(cart.total_price))
    cart.display_cart()

