import math
list = [ ]
n = int(input("Please enter the number to find the prime factor:"))
def prime_factor(n):
    while n % 2 == 0:
        n = n / 2
        list.append(2)

    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            list.append(i)
            n = n /i 

    if n > 2 :
        list.append(n)
prime_factor(n)
print(list)
n = len(list)
i = 0
while  i in range(0,n):
    
    if ( i > n):
        break
    else:
        print(list[i])
        if input('Do you want to continue Y or N ?') == 'Y':
            i = i + 1
            continue
        else:
            break