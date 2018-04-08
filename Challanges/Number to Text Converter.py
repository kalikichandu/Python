dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve"
        ,13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
        30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"
        }

digitToBeConverted = 99345678917510
i = 1
digitList = str(digitToBeConverted)

output = ""
j = len(digitList)-1
while (i <= len(digitList) and j >= 0):
    for key in dict:
        if j == 1 or j == 4 or j == 6 or j == 8 or j == 11 or j == 13:
            if digitList[len(digitList) - j-1] == "1":
                if key == int(digitList[len(digitList) - j-1] + digitList[len(digitList)-j]):
                    if j == 4 or j == 11:
                        output = output + dict[key] + " thousand "
                    elif j == 6 or j == 13:
                        output = output + dict[key] + " lakh "
                    elif j == 8:
                        output = output + dict[key] + " crore "
                    else:
                        output = output + dict[key] + " "
                    j -=1
                    break

            elif key == int(digitList[len(digitList)-j-1]+'0'):
                output = output + dict[key] + " "
                break


        elif str(key) == digitList[len(digitList)-j-1]:
            if j == 2 or j == 9:
                output = output + dict[key]+" hundred "
                break
            elif j == 0:
                output = output + dict[key] +" "
            elif j == 3 or j == 10:
                output = output + dict[key] + " thousand "
            elif j == 5 or j == 12:
                output = output + dict[key] + " lakh "
            elif j == 7:
                output = output + dict[key] + " crore "
    j -= 1
    i +=1

print(output)