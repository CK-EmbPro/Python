numbers=[5,2,5,2,5]

# for x_count in numbers:
#     print("x" * x_count)

for x_count in numbers:
    output=''
    for countr in range(x_count):
        output+='x'
    print(output)