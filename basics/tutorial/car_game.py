started =False
while True: 
    commands = input("> ").lower()
    
    if(commands =="help"):
        print('''
        start: to start the car
        stop: to stop the car
        quit: to quit the car
        ''')

    elif commands == "start":
        if started:
            print("The car is already started")
        else:
            print("Started the car")
            started = True 
        

    elif commands == "stop":
        if not started: 
            print("The car is already stopped")

        else:
            print("The car stoppeed")
            started = False


    elif commands=="quit":
        break
    
    else: 
        print("Sorry I don't understand this command")