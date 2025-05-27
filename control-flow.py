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
    if lower_letter in 'a, e, i, o & u':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Call the function to execute it