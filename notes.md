username = 'Marcio'
password = 'pass12345'

if username == username && password == password:
    return login accepted
else:
    return login failed


    AND - All values must be true

    OR - One of the values must be true

    NOT - The value must be false


! = NOT

START
    is it raining?
        case: yes
                take umbrella
        case: no
                !take umbrella



Hot => Wear Vests
Cold => Wear Gloves
Raining => Wear rain coats
Sunny => Stay indoors


HOW AN ATM WORKS

ATM SYSTEM:
    Enter Pin Code
        Chances 3
        if pin is wrong
            another chance
        if pin is wrong
            another chance
        if pin is wrong
            another chance
        

        case 1:
            if pin isCorrect 
                withdraw()
        case 2:
            if pin is wrong:
                another chance
        case 3: 
            if chances >= 3
                cardBlocked()


Write a program that allows the user to enter a number or a letter then
it tells you if the user entered a number or a letter

Built-in Functions:
    These are functions that are already built in python like:
        print()
        int()
        isdigit()
        isalpha()
        len()

User-defined Funtions:
    These are functions that are not built in python but can be created
    by the programmer
        withdraw()
        cardBlocked()


Create a calculator that takes in 2 values and returns an answer.
    1. Calculator should end only after the user closes it
    2. Calculator should take user data
    3. User can enter a number or a letter
    4. If user places a wrong value eg. #, system should tell to enter 
    a number(calid data)

        