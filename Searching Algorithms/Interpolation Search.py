"""
The idea of formula is to return higher value of pos
when element to be searched is closer to arr[hi]. And
smaller value when closer to arr[lo]
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

arr[] ==> Array where elements need to be searched
x     ==> Element to be searched
lo    ==> Starting index in arr[]
hi    ==> Ending index in arr[]
"""

input = [10,11,12,13,14,16,17,18,19,20,21]
# lenOfOriginal = len(input)
valueToBeSearched = 100
lo = 0
prevPosition = None
index = 0
found = 0
while len(input)> 1:
    hi = len(input)-1
    if (input[hi] - input[lo] == 0):
        position = 0
    else:
        position = int(lo + ((valueToBeSearched - input[lo]) * (hi - lo) / (input[hi] - input[lo])))
    if (position >= len(input)):
        print("not present in list")
        break

    if (prevPosition == position == 0):
        position = position +1

    if (valueToBeSearched == input[position]):
        print("found at index " + str(index+position))
        found = 1
        break

    elif (valueToBeSearched > input[position]):
        input = input[position:].copy()
        lo = position
        index += position
        prevPosition = position

    elif (valueToBeSearched < input[position]):
        input = input[:position].copy()
        index += position
        prevPosition = position
if len(input) <= 1:
    print("not present in list")