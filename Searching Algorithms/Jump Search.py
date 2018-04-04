from math import sqrt
# Finding optimal size
"""
n is size of array Let n = 10
m jump size Minimum Jump size can be 1
array = [0,1,2,3,4,5,6,7,8,9]
In worst case scenario of finding 9 with minimum jump size i.e 1
we need to do 9 comparisions
In the worst case, we have to do n/m jumps
and if the last checked value is greater than the element to be searched for,
we perform m-1 comparisons more for linear search.
Therefore the total number of comparisons in the worst case will be ((n/m) + m-1).
The value of the function ((n/m) + m-1) will be minimum when m = √n.
Therefore, the best step size is m = √n.
"""
input = [10,11,12,13,14,16,17,18,19,20,21]
# lenOfInput = len(input)
jumpSize = int(sqrt(len(input)))
valueToBeSearched = 21
# print (jumpSize)
# y = jumpSize
i = 1
found =0
while(jumpSize <= len(input)):
    if (valueToBeSearched < input[jumpSize-1]):
        while (i <= int(sqrt(len(input)))):
            if input[jumpSize - 1 - i] == valueToBeSearched:
                print("found at " + str(jumpSize-i-1))
                found = 1
                break
            i += 1
        if found == 0:
            print("value is not present in the list")
            break

    elif (valueToBeSearched == input[jumpSize-1]):
        print("found at " + str(jumpSize - 1))
        found = 1
        break
    elif (valueToBeSearched > input[len(input)-1]):
        print("value is not present in the list")
        break
    if found == 1:
        break
    else:
        # y += int(sqrt(lenOfInput))
        jumpSize += int(sqrt(len(input)))
        if jumpSize >= len(input):
            # jumpSize, y = lenOfInput,lenOfInput
            jumpSize = len(input)

