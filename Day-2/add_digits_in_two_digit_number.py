# TODO Add the numbers in a given two digit number

num = input("Enter a two digit number: ")
entered_num = num

sum = 0

for n in num:
    sum += int(n)

print(f"The sum of entered two digit {entered_num} num is {sum}")