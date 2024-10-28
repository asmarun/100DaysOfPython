banner = """
.-.-.  .-.-.  .-.-.  .-.-.        .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  
'. L ) '. O ) '. V ) '. E ) .-.-. '. C ) '. A ) '. L ) '. C ) '. U ) '. L ) '. A ) '. T ) '. O ) '. R ) 
  ).'    ).'    ).'    ).'  '._.'   ).'    ).'    ).'    ).'    ).'    ).'    ).'    ).'    ).'    ).'
"""
print(banner)

name1 = input("What is your name?").lower() 
name2 = input("What is their name?").lower()
print("The Love Calculator is calculating your score...")

combined_name = f"{name1}{name2}"

key_word1 = "true"
key_word2 = "love"
count_of_keyword1_in_combined_name = 0
count_of_keyword2_in_combined_name = 0

for i in key_word1:
    count_of_keyword1_in_combined_name += combined_name.count(i)

for i in key_word2:
    count_of_keyword2_in_combined_name += combined_name.count(i)

love_score = int(str(count_of_keyword1_in_combined_name) + str(count_of_keyword2_in_combined_name))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score <= 50 and love_score >= 40:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

