# MATH OPERATORS
# -----------------------------------------------------------------------------

# value1 = 20
# value2 = 25

# sum =  value1 + value2
# print(sum)

# difference = value2 - value1
# print(difference)


# product = value1 * 3
# print(product) 


# divisible = value2 / 5
# print(divisible)

# COMPARATIVE OPERATORS
# _________________________________________________________________


# value1 = 25
# value2 = value1 + 5

# compare = value2 > 100
# print(compare)

# NOTES
# Comparative Operators return back a boolean

# username = input("Enter your name: ")
# password = input("Enter your password: ")

# if username == "Marcio" and password == "pass1234":
#     print("Welcome, Marcio!")
# else: 
#     print("Sorry, your name or password is incorrect.")


guess = input("Enter your age: ")

if guess.isdigit():
    guess = int(guess)
    if guess <= 18:
        print("You are too young")
    if guess > 18:
        print("You are over age")
else: 
    print("Please enter a number as age")



