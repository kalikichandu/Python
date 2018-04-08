#Sort even-placed elements in increasing and odd-placed in decreasing order

input = [3,1,2,4,5,9,13,14,12]

print("Input: "+str(input))

evenPlacedElements = []

oddPlacedElements = []

output = []

for x,value in zip(range(len(input)),input):
    if x == 0 or x % 2 == 0:
        evenPlacedElements.append(value)
    else:
        oddPlacedElements.append(value)

print("Even Placed Elements in Increasing Order: "+ str(sorted(evenPlacedElements)))

print("Odd Placed Elements in Decreasing Order"+str(sorted(oddPlacedElements,reverse=True)))
print("Output: "+str(sorted(evenPlacedElements) + sorted(oddPlacedElements,reverse=True)))


