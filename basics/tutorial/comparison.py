name= (input("Enter the name "))

if len(name)<3:
    print("The name must be at least 3 characters")
elif len(name)>50:
    print("The name must be at not more than 50 characters")

elif len(name)>=3 and len(name)<=50:
    print("Ok with the name")