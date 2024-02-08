high_income= bool(input("Input sth for truthy or leave it for falsy "))
has_good_credit= bool(input("Input sth for truthy or leave it for falsy "))

if high_income and has_good_credit:
    print("Eligible for loan")

elif has_good_credit or high_income: 
    if has_good_credit==False:
        print("partially eligible for loan due to bad credit")
    
    if high_income==False:
        print("partially eligible for loan due to low income")

else: 
    print("Not eligible just")
    