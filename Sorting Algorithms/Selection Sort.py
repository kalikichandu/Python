
def SelectionSort (inputData):
    for value in inputData:
        for i in range(len(inputData)):
            if value > inputData[i]:
                value = inputData[i]
                # del inputData[i+1]
        output.append(value)
        inputData.remove(value)
        SelectionSort(inputData)
    return output

output = []
input = [20,10,40,3,6,122,90,23,22]
print(SelectionSort(input))

