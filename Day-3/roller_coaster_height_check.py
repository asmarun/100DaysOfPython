name = input("Please enter your name: ")
height = int(input("Please enter your height in cm: "))

if height <= 120:
    print(f"Sorry {name}! 🚫 Minimum height required to get the ticket should be more than 120cm.")
else:
    print(f"Hello {name}! Here you Go 🎟️")
