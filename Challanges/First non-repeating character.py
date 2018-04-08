input = 'chandrasekhar'

for b in range(len(input)):
    if input.count(input[b]) == 1:
        # print(input[b])
        print("First Non-Repeating Character in {} is  {} ".format(input,input[b]))
        break