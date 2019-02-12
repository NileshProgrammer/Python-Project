import math 
def CalculatePi(roundVal):
    somepi = round(math.pi,roundVal)
    pi = str(somepi)
    someList = list(pi)
    return somepi
roundTo = input('Enter the number of digits you want after the decimal for Pi: ')
if int(roundTo) < 10:
    try:
        roundint = int(roundTo)
        print(CalculatePi(roundint))
    except:
        print("You did not enter an integer")
else:
    print("Value should be less than 10")