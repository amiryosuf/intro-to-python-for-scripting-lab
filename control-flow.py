# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Prompt the user to enter a letter
    letter = input("Please enter a letter (a-z or A-Z): ").strip()

    # Check if the input is a single letter
    if len(letter) != 1 or not letter.isalpha():
        print("Error: Please enter a single alphabetical character.")
        return

    # Convert the letter to lowercase for uniformity
    lower_letter = letter.lower()

    # Check if the letter is a vowel or consonant
    if lower_letter in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")






# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Prompt the user to enter their age
    age_input = input("Please enter your age: ").strip()

    # Check for negative or non-numeric input
    try:
        age = int(age_input)
        if age < 0:
            print("Error: Age cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid number for your age.")
        return

    # Set the minimum voting age
    voting_age = 18

    # Check if the user is eligible to vote
    if age >= voting_age:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")






# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Prompt the user to enter the dog's age
    dog_age_input = input("Calculate a dog's age: ").strip()

    # Check for non-numeric input
    try:
        dog_age = int(dog_age_input)
        if dog_age < 0:
            print("Error: Dog's age cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid number for the dog's age.")
        return

    # Calculate the dog's age in dog years
    if dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = 20 + (dog_age - 2) * 7

    # Print the calculated age in dog years
    print(f"The dog's age in dog years is {dog_years}.")






# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Prompt the user for weather conditions
    is_cold = input("Is it cold? (yes/no): ").strip().lower()
    is_raining = input("Is it raining? (yes/no): ").strip().lower()

    # Validate inputs
    if is_cold not in ['yes', 'no'] or is_raining not in ['yes', 'no']:
        print("Error: Please answer with 'yes' or 'no'.")
        return

    # Determine clothing advice based on conditions
    if is_cold == 'yes' and is_raining == 'yes':
        print("Wear a waterproof coat.")
    elif is_cold == 'yes' and is_raining == 'no':
        print("Wear a warm coat.")
    elif is_cold == 'no' and is_raining == 'yes':
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")






# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Prompt the user for the month and day
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    day_input = input("Enter the day of the month: ").strip()
    # Validate the month input
    valid_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if month not in valid_months:
        print("Error: Please enter a valid month (Jan - Dec).")
        return
    # Validate the day input
    try:
        day = int(day_input)
        if day < 1 or day > 31:
            print("Error: Please enter a valid day (1-31).")
            return
    except ValueError:
        print("Error: Please enter a valid number for the day.")
        return
    # Determine the season based on the month and day
    if (month == 'Dec' and day >= 21) or (month in ['Jan', 'Feb']) or (month == 'Mar' and day < 20):
        season = "Winter"
    elif (month == 'Mar' and day >= 20) or (month in ['Apr', 'May']) or (month == 'Jun' and day < 21):
        season = "Spring"
    elif (month == 'Jun' and day >= 21) or (month in ['Jul', 'Aug']) or (month == 'Sep' and day < 22):
        season = "Summer"
    else:
        season = "Fall"
    # Print the result
    print(f"{month} {day:02d} is in {season}.")








    












