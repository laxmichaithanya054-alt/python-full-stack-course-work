# Product list with price per unit
products = {
    "milk": 50,
    "sugar": 40,
    "butter": 60,
    "bread": 30
}

cart = {}

while True:
    print("\nAvailable products:", list(products.keys()))
    print("1. Buy Now")
    print("2. Add to Cart")
    print("3. Show Cart & Calculate Bill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  # Buy Now
        name = input("Enter product name: ").lower()
        if name in products:
            qty = int(input("Enter quantity: "))
            total = products[name] * qty
            print(f"Total amount for {name}: ₹{total}")
        else:
            print("Product not available!")

    elif choice == "2":  # Add to Cart
        name = input("Enter product name: ").lower()
        if name in products:
            qty = int(input("Enter quantity: "))
            if name in cart:
                cart[name] += qty
            else:
                cart[name] = qty
            print(f"{name} added to cart!")
        else:
            print("Product not available!")

    elif choice == "3":  # Show Cart & Bill
        total_bill = 0
        print("\nYour Cart:")
        for item, qty in cart.items():
            price = products[item] * qty
            total_bill += price
            print(f"{item} x {qty} = ₹{price}")
        print("Total Bill = ₹", total_bill)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
