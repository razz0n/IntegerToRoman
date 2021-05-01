
#Function to convert integer to roman
def intToRoman(num):
#Check if the number is between 0 and 3999.
    if num<0 or num>3999:
        print("Please enter number between 0 and 3999.")
        exit()

    #Creating a dictionary to map integer to roman
    my_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
             4: 'IV', 1: 'I'}

    #Answer is empty at the beginning
    answer = ''

    #val is the value of integer and key is the actual roman number
    for val, key in my_dict.items():
        #Checking if the number is greater than 0
        while (num - val >= 0):
            #Assigning key to the result
            answer += key
            #Subtracting the value from num such that the num becomes next lower place digit
            num = num - val

    return answer

#Test
print(intToRoman(4000))
