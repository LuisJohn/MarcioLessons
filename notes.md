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