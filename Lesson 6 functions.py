data = input("Marcio, please enter anything: ")

if data.isdigit():
    print("You entered a number")
elif data.isdclsecimal():
    print("You entered a decimal")
else:
    print("You entered a letter")