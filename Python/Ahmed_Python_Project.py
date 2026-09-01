print("Welcome to Tokyo Shop, Travel & Luggage Store")
print("Your journey starts here")

name = "Tokyo Shop"
shop_type = "Travel & Luggage Store"
brand = "Sakura"


sakura_backpack = {
    "name": "Sakura Backpack",
    "price": 99,
    "stock": 30,
    "colours": ("Pink", "Red", "Blue", "Black", "White", "Purple", "Green"),
    "description": "A practical backpack suitable for everyday travel and carrying personal items. It has multiple pockets for organising different types of items"
}


sakura_handbag = {
    "name": "Sakura Handbag",
    "price": 50,
    "stock": 50,
    "colours": ("Pink", "Red", "Blue", "Black", "White", "Purple", "Green"),
    "description": "A stylish and practical handbag suitable for travel and everyday use. It has multiple compartments for keeping personal items organised and easy to access"
}


sakura_suitcase_s = {
    "name": "Sakura Suitcase",
    "size": "S",
    "price": 60,
    "stock": 300,
    "colours": ("Pink", "Red", "Blue", "Black", "White", "Purple", "Green"),
    "description": "A strong and durable suitcase with plenty of storage space and multiple pockets for organising travel items. It is water-resistant and suitable for different types of travel"
}


sakura_suitcase_m = {
    "name": "Sakura Suitcase",
    "size": "M",
    "price": 90,
    "stock": 200,
    "colours": ("Pink", "Red", "Blue", "Black", "White", "Purple", "Green"),
    "description": "A strong and durable suitcase with plenty of storage space and multiple pockets for organising travel items. It is water-resistant and suitable for different types of travel"
}


sakura_suitcase_l = {
    "name": "Sakura Suitcase",
    "size": "L",
    "price": 120,
    "stock": 100,
    "colours": ("Pink", "Red", "Blue", "Black", "White", "Purple", "Green"),
    "description": "A strong and durable suitcase with plenty of storage space and multiple pockets for organising travel items. It is water-resistant and suitable for different types of travel"
}


sakura_suitcase_xl = {
    "name": "Sakura Suitcase",
    "size": "XL",
    "price": 150,
    "stock": 30,
    "colours": ("Pink", "Red", "Blue", "Black", "White", "Purple", "Green"),
    "description": "A strong and durable suitcase with plenty of storage space and multiple pockets for organising travel items. It is water-resistant and suitable for different types of travel"
}


products = [
    sakura_backpack,
    sakura_handbag,
    sakura_suitcase_s,
    sakura_suitcase_m,
    sakura_suitcase_l,
    sakura_suitcase_xl
]


for number, p in enumerate(products, 1):

    display_name = p["name"]

    if "size" in p:
        display_name = display_name + " — " + p["size"]

    print(number, display_name)
    print("$", p["price"])
    print(" Available colours:", ", ".join(p["colours"]))
    print(p["stock"])
    print(p["description"])


choice = input("Please choose a product (1-6): ")

product_index = int(choice) - 1

selected_product = products[product_index]
selected_display_name = selected_product["name"]
if "size" in selected_product:
    selected_display_name = selected_display_name + " — " + selected_product["size"]
print(selected_display_name)


quantity = input("How many would you like? ")

quantity_number = int(quantity)


if quantity_number <= selected_product["stock"]:

    print("Your order is available.")

    selected_product["stock"] -= quantity_number

    total = selected_product["price"] * quantity_number

    print("Your order total is: $", total)
 
    print("Order Review")
    print("Product:", selected_display_name)
    print("Quantity:", quantity_number)
    print("Remaining stock:", selected_product["stock"])


    add_more = input("Would you like to add another product? (yes/no): ")
    if add_more == "no":
        print("Thank you for visiting Tokyo Shop! ")
    if add_more == "yes":
        print("Please choose another product:")
        second_choice = input("Please choose another product (1-6): ")
        second_product_index = int(second_choice) - 1
        second_product = products[second_product_index]
        second_display_name = second_product["name"]
        if "size" in second_product:
            second_display_name = second_display_name + " — " + second_product["size"]
        print(second_display_name)
        second_quantity = input("How many would you like? ")
        second_quantity_number = int(second_quantity)
        if second_quantity_number <= second_product["stock"]:
            second_product["stock"] -= second_quantity_number
            second_total = second_product["price"] * second_quantity_number
            order_total = total + second_total
            print("Second Product:", second_display_name)
            print("Second Quantity:", second_quantity_number)
            total_quantity = quantity_number + second_quantity_number
            if total_quantity >= 2:
                discount = order_total * 0.05
                final_total = order_total - discount
                print("Discount: $", discount)
                print("Final total: $", final_total)
                print("Thank you for your order! ")
            else:
                final_total = order_total
                print("Final total: $", final_total)
                print("Thank you for your order! ")
        else:

            print("Sorry, not enough stock available for this product.")

else:

    print("Sorry, not enough stock available.")