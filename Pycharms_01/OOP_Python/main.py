
# write methods in class, these will be accessible from instances
# methods are nothing but functions inside classes
# python passes object itself as first argument, hence the self
class Item:
    def calculate_total_price(self, x, y):
        return x*y


# create instance of this class
item1 = Item()
# attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
# attributes
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))


# create methods and execute them on instances

random_str = "aaa"
print(random_str.upper())