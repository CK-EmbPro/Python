number=9

for item in range(1,4):
    guess=int(input("Guess: "))
    bool_value= guess==number
    
    if guess==number:
        print("You win")
        break
    
    elif item==3 and bool_value==False:
        print("You lose")
        break