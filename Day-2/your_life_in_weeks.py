# TODO Consider lifetime as 90 years, so total weeks is 90 * 52 weeks

lifetime = 90
total_lifetime_weeks = 90 * 52

age = int(input("Enter your age: "))
user_age_in_weeks = age * 52

remaining_weeks = total_lifetime_weeks - user_age_in_weeks


print(f"Your remaining weeks in this mortal world are/is {remaining_weeks} weeks.👻")
