banner = '''
▗▄▄▖ ▗▖  ▗▖▗▄▄▄▖     ▗▄▄▖ ▗▄▖ ▗▖    ▗▄▄▖▗▖ ▗▖▗▖    ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ 
▐▌ ▐▌▐▛▚▞▜▌  █      ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌ ▐▌▐▌   ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌
▐▛▀▚▖▐▌  ▐▌  █      ▐▌   ▐▛▀▜▌▐▌   ▐▌   ▐▌ ▐▌▐▌   ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖
▐▙▄▞▘▐▌  ▐▌▗▄█▄▖    ▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▙▄▄▖▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌
'''

print(banner)

name = input("Please enter your name: ")
weight = int(input(f"Hello {name}! Enter your weight in kg: "))
height = float(input(f"Hello {name}! Enter your height in metres: "))

bmi = round(weight / (height ** 2))

bmi_range = ""

if bmi < 18.5:
    bmi_range = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    bmi_range = "Normal Weight ⚖️"
elif bmi >= 25 and bmi <= 29.9:
    bmi_range = "Overweight"
elif bmi >= 30 and bmi <= 34.9:
    bmi_range = "Moderately Obese"
elif bmi >= 35 and bmi <= 39.9:
    bmi_range = "Severely Obese"
else:
    bmi_range = "Morbidly obese"

print(f"{name} your BMI index value is {bmi} and you are {bmi_range}.")