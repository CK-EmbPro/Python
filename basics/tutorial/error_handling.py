try: 
    age =40 
    divident =input("Input what to divide by: ")

    print(age/int(divident))

except ZeroDivisionError:
    print("Can't divide by zero")

except ValueError:
    print("Can't convert to integer from string")