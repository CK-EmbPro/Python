def food_determiner():
    food_dict = {
        "S": "Sweet potatoes","J": "Juice", "K": "Kawunga"
    }
    word_input= input("Input your favorite food ")
    split_input= word_input.split(" ")

    output = ""

    for food in split_input:
        output += food_dict.get(food, food)+ " "
    
    return output

print(food_determiner())