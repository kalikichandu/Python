def linearSearch(input,x):
    for i in range(len(input)):
        if input[i] == x:
            return i
    return -1
input = [1,2,3,4,5]

x = 3
print(linearSearch(input,x))