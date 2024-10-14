name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age < 12:
    print(f"Hi {name}! Your ticket price is $5.")
elif age >= 12 and age < 18:
    print(f"Hi {name}! Your ticket price is $7.")
else:
    print(f"Hi {name}! Your ticket price is $12.")        
