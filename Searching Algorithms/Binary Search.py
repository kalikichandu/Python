def BinarySearch(input,x,factor):
    if x == input[int(len(input)/2)]:
        factor = factor+int(len(input)/2)
        return "found at index "+str(factor)
    elif x > input[int(len(input)/2)]:
        temp = input[int(len(input)/2):]
        factor= factor + int(len(input)/2)
        return BinarySearch(temp, x,factor)
    else:
        temp = input[:int(len(input) / 2)]
        return BinarySearch(temp, x,factor)

input = [10,11,12,13,14,15,16,17,18,19,20,21]
x = 11 # value to be searched

print(BinarySearch(input,x,factor=0))

