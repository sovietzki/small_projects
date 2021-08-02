print("Welcome to your shopping cart!")
shopping_cart = []
new_item = ""
while new_item != "q":
    new_item = input("Add something to your basket. Type q to quit: ")
    shopping_cart.append(new_item)

if new_item == "q":
    shopping_cart.remove("q")
    print("Your shopping list is:")
    shopping_cart.sort()
    for item in shopping_cart:
        print(" -" + item)
