import random

banner = """
 _   _                   _                 _____         _  _ 
| | | |                 | |               |_   _|       (_)| |
| |_| |  ___   __ _   __| |   ___   _ __    | |    __ _  _ | |
|  _  | / _ \ / _` | / _` |  / _ \ | '__|   | |   / _` || || |
| | | ||  __/| (_| || (_| | | (_) || |      | |  | (_| || || |
\_| |_/ \___| \__,_| \__,_|  \___/ |_|      \_/   \__,_||_||_
"""



print(banner)

head_or_tail = ["head", "tail"]

random_number = random.randint(0,1)

user_input = input("\n Enter 'head' or 'tail': ")
computer_choice = head_or_tail[random_number]

if user_input.lower() == computer_choice:
    print("You Win! 🙌")
elif user_input.lower() not in head_or_tail:
    print("Only 'head' or 'tail' are accepted as an input.")
else:
    print(f"Computer's choice is '{computer_choice}'.You Lose. Computer wins!🤖")      