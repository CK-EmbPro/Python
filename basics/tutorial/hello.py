weight= int(input("Weight: "))
metric_system = input("input k or l ")

if (metric_system.upper()== "L"): 
    print("Weight in bs: ", str(weight*2.5))
elif metric_system.upper() =="K":
    print("Weight in kg:", str(weight*1.8))