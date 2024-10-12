#TODO Swap two variable values(integers) without creating a third variable

x = int(input("Enter the value for x, x should be an integer : "))
print(f"The value of x is {x}\n")

y = int(input("Enter the value for y, y should be an integer : "))
print(f"The value of y is {y}\n")

print("The Program is swapping your values...\n")

x = x + y
y = x - y

x = x - y

print(f"Displaying the values after swap. Now: \n x: {x} \n y: {y}")