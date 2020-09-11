print("********************************")
print("Star Pattern")
print("********************************")
print("Number of Stars you want to see in galaxy")
num = int(input()) + 1
print("You want to print reverse or straight (0(Yes)/1(NO))")
optionReverse = int(input())
if optionReverse == 0:
    Reverse = True
elif optionReverse == 1:
    Reverse = False
else:
    print("Provide option 0 or 1")
if Reverse:
    for i in range(num):
        for j in range(i):
            print("*", end=" ")
        print("\n")
else:
    for i in reversed(range(num)):
        for j in range(i):
            print("*", end=" ")
        print("\n")
