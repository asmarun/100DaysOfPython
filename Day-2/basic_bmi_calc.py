banner = '''
▗▄▄▖ ▗▖  ▗▖▗▄▄▄▖     ▗▄▄▖ ▗▄▖ ▗▖    ▗▄▄▖▗▖ ▗▖▗▖    ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ 
▐▌ ▐▌▐▛▚▞▜▌  █      ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌ ▐▌▐▌   ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌
▐▛▀▚▖▐▌  ▐▌  █      ▐▌   ▐▛▀▜▌▐▌   ▐▌   ▐▌ ▐▌▐▌   ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖
▐▙▄▞▘▐▌  ▐▌▗▄█▄▖    ▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▙▄▄▖▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌
'''

print(banner)

weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

bmi = round(weight / (height ** 2))

print(f"Your BMI is {bmi}")