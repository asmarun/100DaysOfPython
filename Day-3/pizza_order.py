"""
TODO
Based on a user's order, work out their final bill.
1. Pizza Size
    a. Small pizza (S): $15
    b. Medium pizza (M): $20
    c. Large pizza (L): $25
2. Add pepperoni for small pizza (Y or N): +$2
3. Add pepperoni for medium or large pizza (Y or N): +$3
4. Add extra cheese for any size pizza (Y or N): +$1
"""
banner = """
██████╗ ██╗███████╗███████╗ █████╗     ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗     
██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗    ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗    
██████╔╝██║  ███╔╝   ███╔╝ ███████║    ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║    
██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║    ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║    
██║     ██║███████╗███████╗██║  ██║    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝    
╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ 
"""
print(banner)

print("Welcome to Pizza World🍕!")
print("""
Pizza World Menu:
    a. Small pizza (S): $15
    b. Medium pizza (M): $20
    c. Large pizza (L): $25  
""")
pizza_size = input("Please choose your pizza size, S or M or L: ")
add_pepperoni = input("Do you want us to add pepperoni (costs additional $2-$3) to your pizza? Yes or No: ")
add_cheese = input("Do you want us to add extra cheese (costs additional $3) to your pizza? ")
pizza_price = 0

if pizza_size.lower() == "s":
    pizza_price = 15
elif pizza_size.lower () == "m":
    pizza_price = 20
elif pizza_size.lower () == "l":
    pizza_price = 25
else:
    print("Please enter valid input. The allowed values are S, M or L. Please try again!")

if add_pepperoni.lower() == "yes":
    if pizza_size.lower == "s":
        pizza_price += 2
    else:
        pizza_price += 3

if add_cheese.lower() == "yes":
    pizza_price += 3

print(f"\nPlease pay ${pizza_price} and enjoy your delicious 🍕.")