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

# Call the function to execute it
check_letter()