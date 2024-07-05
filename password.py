def check_password_strength(password):
    # Initialize flags to check different criteria
    passlen = len(password) > 8
    passupper = any(x.isupper() for x in password)
    passlower = any(x.islower() for x in password)
    passdigit = any(x.isdigit() for x in password)
    passspecialchar = any(x in "!@#$%&*~" for x in password)
    
    # Determine if the password is valid based on the criteria
    validorNot = passlen and passupper and passlower and passdigit and passspecialchar

    # Determine the strength of the password
    strength = passlen + passdigit + passupper + passlower + passspecialchar
    if strength == 5:
        strength_label = "Very Strong"
    elif strength == 4:
        strength_label = "Strong"
    elif strength == 3:
        strength_label = "Moderate"
    elif strength == 2:
        strength_label = "Weak"
    else:
        strength_label = "Very Weak"
    
    return validorNot, strength_label

# Input password
password = input("Please Choose Your Password:\t")
valid, strength = check_password_strength(password)
print(f"Password is {'Valid' if valid else 'Invalid'} and its strength is {strength}")
