price=1000000
good_credit= bool(input("Input true or leave it for false "))
# print(good_credit)
if good_credit :
    down_payment= 0.1*price
else: 
    down_payment=0.2*price

print(f"Down payment is {down_payment}")