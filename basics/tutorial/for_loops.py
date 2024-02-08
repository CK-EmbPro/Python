# Nested loops
# Coordinates
# for x in range(3):
#     for y in range(3):
#         print((x,y))

# numbers= [3,2,4,1]

# for item in range(len(numbers)):
#     for j_item in range(1, len(numbers)):
#         if(numbers[j_item]<numbers[item]):
#             temp= numbers[item]
#             numbers[item] = numbers[j_item]
#             numbers[j_item] = temp

# print(numbers)


numbers = [3, 2, 4, 1]

for i in range(len(numbers)):
    for j in range(1, len(numbers)):
        if numbers[j] < numbers[j-1]:
            temp = numbers[j]
            numbers[j] = numbers[j-1]
            numbers[j-1] = temp

print(numbers)

