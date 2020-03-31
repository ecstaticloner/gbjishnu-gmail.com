command= input('''
welcome to the car  game'
enter the command
or enter Help for help''')

started = False

while True:
    command = input(">>  ").lower()
    if command == "help":
        print('''
        START to start the car
        STOP to stop the car
        QUIT to exit the gameFa
        ''')
    elif command == "start":
        if started :
            print("Already started ")
        else:
            started = True
            print("The car is started , Ready to go")
    elif command == "stop":
        if not started :
            print(" Already stopped ")
        else:
            started = False
            print("The car is stopped ")
    elif command== "quit":
        break
    else:
        print(" unknown command , enter a correct one")
