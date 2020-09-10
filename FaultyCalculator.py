# Design a calulator which will correctly solve all the problem except the following ones:
# 45 * 3 = 555 , 56 + 9  = 77 , 56 /4 = 4
print("***********************************************************")
print("Program to take 2 number and apply operation +,-,/,*")
print("***********************************************************")
print("Enter your number1")
num1 = int(input())
print("Enter your number2")
num2 = int(input())
print("Provide operator from this option : (+,-,*,/) to perform operation ")
operators = ["+", "-", "/", "*"]
operator = input()
print("***********************************************************")
invalidData = [3, 45, "*"]
invalidData2 = [56, 9, "+"]
invalidData3 = [56, 6, "/"]

if operator in operators:
    if operator == "+":
        if num1 not in invalidData2 and num2 not in invalidData2:
            result = num1 + num2
        else:
            result = 77
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        if num1 not in invalidData and num2 not in invalidData:
            result = num1 * num2
        else:
            result = 555
    elif operator == "/":
        if num1 not in invalidData3 and num2 not in invalidData3:
            result = num1 / num2
        else:
            result = 4
    else:
        result = 0
else:
    result = 0
    print("Provide Proper operator")
print(result)
