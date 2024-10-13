banner = '''
▗▄▄▄▖▗▄▄▄▖▗▄▄▖      ▗▄▄▖ ▗▄▖ ▗▖    ▗▄▄▖▗▖ ▗▖▗▖    ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ 
  █    █  ▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌ ▐▌▐▌   ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌
  █    █  ▐▛▀▘     ▐▌   ▐▛▀▜▌▐▌   ▐▌   ▐▌ ▐▌▐▌   ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖
  █  ▗▄█▄▖▐▌       ▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▙▄▄▖▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌
'''
print(banner)

bill_amount = float(input("Enter the bill amount: $"))
print("\n")
people_visited_restaurant = int(input("Enter the number of person to share the bill: "))
print("\n")
tip_percentage = int(input("Enter your tip preference %, 10/12/15:  "))
print("\n")

tip_amount = bill_amount * (tip_percentage / 100)
print(f"The Total Tip Amount is ${round(tip_amount,2)}\n")

total_amount = bill_amount + tip_amount

individual_share = total_amount / people_visited_restaurant

print(f"The Total Bill including the tip amount is ${round(total_amount,2)}\n")

print(f"Individuals should pay ${round(individual_share,2)}")