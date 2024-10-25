"""
TODO: RollerCoaster Ticket Payment System:

Create a program, where a user is trying to buy a ticket for a rollercoaster ride.

1. Allow user only if the user’s height is above 120 cm.

2. Ticket price varies depending on their age:

    a. Age < 12 = $5

    b. Age between 12 - 18 = $7

    c. Age > 18 = $12 

3. Add $3 to the total bill if they want a photo taken
"""

name = input("Please enter your name: ")
height = int(input("Please enter your height in cm: "))
age = int(input("Please enter your age: "))
photo = input(f"Hello {name}, do you want to take a photo of you riding Roller Coaster: Yes or No?: ")

if photo.lower() == "yes" or photo.lower() == "y":
    ticket_price = 3
else:
    ticket_price = 0

if height > 120:
    if age < 12:
        ticket_price += 5
    elif age >= 12 and age < 18:
        ticket_price += 7
    else:
        ticket_price += 12
    print(f"\nHi {name}! Your ticket price is ${ticket_price}.")  
    print(f"Here you Go 🎟️")
else:
     print(f"Sorry {name}! 🚫 Minimum height required to get the ticket should be more than 120cm.")       



  