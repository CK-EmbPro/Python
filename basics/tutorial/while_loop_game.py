number=8
i=1
j=3

while i<=j:
    guess= int(input("Guess: "))
    bool_value= guess==number

    if bool_value:
        print("You win")
        break
    
    elif i==j and bool_value==False:
        print("You lose")
      
    i +=1