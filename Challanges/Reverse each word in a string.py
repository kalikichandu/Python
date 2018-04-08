# Challange from GreekforGreeks

input = "string to be reversed"

split = input.split(" ")
# split.reverse()  using python string function

output = []

for word in split:
    output.insert(0,word)
print(output)

