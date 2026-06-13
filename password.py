# Global
score = 0
uppercase = False
lowercase = False
specialchar = False
digit = False
special_chars = "!@#$%^&*"

# User input

user_input = input("Enter your password: ")

# Length Validator
 
if len(user_input) >= 8:
    score += 1
if len(user_input) >= 12:
    score += 1
if len(user_input) >=15:
    score += 1
if len(user_input) >=25:
    score += 1

# Universal

for char in user_input:
    if char.isdigit():
        digit = True
    if char in special_chars:
        specialchar = True
    if char.islower():
        lowercase = True
    if char.isupper():
        uppercase = True
    

if digit:
    score += 1
if specialchar:
    score += 1
if lowercase:
    score += 1
if uppercase:
    score += 1



# Give the score to the user

if score <= 2:
    print("Weak Password\nChange Immediately!!")
elif 3 <= score <= 5:
    print("Moderate Strength\nConsider changing.")
elif score > 5:
    print("Strong Password!\nThanks for using Garv's Password Analyser!")

print(score)