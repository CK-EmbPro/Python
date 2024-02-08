# digits_mapping= {0:"Zero",1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

food_dict ={"R": "rice", "G": "Goffrey", "S": "sweet_potatoes","I": "Irish potatoes"}
inputt = input("what is your favorite food? ")
split_input = inputt.split(" ")

del food_dict['R']
output= ""
for food in split_input:
    output = output + food_dict.get(food,food) + " "

print(output)