
cardPin = "1234"

chances = 3

while chances > 0:
    pin = input("Enter your pin code: ")

    if pin == cardPin:
        print("Withdraw Money")
        quit()
    elif pin != cardPin:
        print("Wrong pin code")
        continue
    chances = chances - 1

print("Card Blocked")


# INFINITE LOOP IS A LOOP THAT NEVER STOPS

# number = 0
# while True:
#     print("Marcio: ", number)
#     number = number + 1