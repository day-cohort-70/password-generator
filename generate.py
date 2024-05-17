import random
import string

def validate_password(password, char_type_dict):
    is_valid = True

    if 'lower' in char_type_dict and not any(ch.islower() for ch in password):
        is_valid = False

    if 'upper' in char_type_dict and not any(ch.isupper() for ch in password):
        is_valid = False

    if 'digit' in char_type_dict and not any(ch.isdigit() for ch in password):
        is_valid = False

    if 'special' in char_type_dict and not any(not ch.isalnum() for ch in password):
        is_valid = False

    return is_valid


def generate_password(length, char_type_dict):
    """Generate a password of the specified length using the provided character types

    Args:
        length (int): Number of characters to generate
        char_type_dict (dict): Dictionary of user-chosen character types and their corresponding character sets

    Returns:
        str: The generated password string
    """

    # Start with an empty password string
    password_string = ""

    # Use the range() function to iterate over the desired password length
    max_range = range(length)

    for _ in max_range:
        # Repeat the process until the desired password length is reached

        # Randomly select a character type
        random_type = random.choice(list(char_type_dict.keys())) # this will be 'lower', 'digit', etc

        # Randomly select a character from that type
        key_value_we_need = char_type_dict[random_type]
        random_character = random.choice(key_value_we_need)

        # Append the selected character to the password string
        password_string += random_character

    # Return the generated password
    return password_string

def evaluate_password_strength(password):
    """Evaluate the strength of the provided password

    Args:
        password (str): A password string to evaluate

    Returns:
        tuple: Contains the strength score and strength category of the password
    """
    # Calculate the length score by multiplying the password length by 4
    score = len(password) * 4

    # Calculate the character type score by checking the presence of lowercase, uppercase, digits, and special characters
    # Add 10 to the character type score for each type present in the password
    if any(ch.islower() for ch in password):
        score += 10

    if any(ch.isupper() for ch in password):
        score += 10

    if any(ch.isdigit() for ch in password):
        score += 10

    if any(not ch.isalnum() for ch in password):
        score += 10


    # Determine the password strength category based on the strength score
    # Less than 50 is Weak, 50-79 is Moderate, 80-99 is Strong, 100 or more is Very Strong
    category = ""
    if score < 50:
        category = "Weak"
    elif score >= 50 and score <=79:
        category = "Moderate"
    elif score >= 80 and score <=99:
        category = "Strong"
    else:
        category = "Very Strong"

    # Return a tuple containing the strength score and strength category
    return ( score, category )

# Prompt the user for the desired password length
# password_length = int(input("Enter the desired password length: "))
password_length = 8

# Prompt the user to select character types (lowercase, uppercase, digits, special characters)
char_types = ['lower', 'digit', 'special', 'upper']
# if input("Include lowercase letters? (y/n): ").lower() == 'y':
#     char_types.append('lower')

# if input("Include uppercase letters? (y/n): ").lower() == 'y':
#     char_types.append('upper')

# if input("Include numbers? (y/n): ").lower() == 'y':
#     char_types.append('digit')

# if input("Include special characters? (y/n): ").lower() == 'y':
#     char_types.append('special')


# Create a dictionary mapping character types to their corresponding character sets
char_type_dict = {
    'lower': list(string.ascii_lowercase),
    'upper': list(string.ascii_uppercase),
    'digit': list(string.digits),
    'special': list(string.punctuation)
}

# Filter the character type dictionary based on user-selected types. Generate a new dictionary with only the selected types.
user_char_choices = {}
for choice in char_types:
    user_char_choices[choice] = char_type_dict[choice]

# Create a data structure to store generated passwords. This data structure should only store unique passwords.
unique_passwords = set()


# Generate and evaluate passwords in a loop until 5 unique passwords is reached.
while len(unique_passwords) < 5:

    is_valid = False
    while not is_valid:
        final_password = generate_password(password_length, user_char_choices)
        is_valid = validate_password(final_password, char_type_dict)

    unique_passwords.add(final_password)

    score, category = evaluate_password_strength(final_password)
    print(f'Score of password is {score} and its category is {category}')

print(unique_passwords)

# Display each generated password along with its strength score and category
# Example:
#    Generated password: d6Gh%Fk8Lm1Q
#    Password strength score: 88
#    Password strength category: Strong


# Print all the generated passwords stored in the set


