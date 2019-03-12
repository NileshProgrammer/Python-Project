# Change Return Program

moneyTaken = int(input('Please enter the total  money taken: '))
productPrice = int(input('Please input the price od product :'))


def parse_change(change):
    resultName = []
    resultCount = []
    pennies = int(change * 100)
    for name, value in (('Quarters', 25), ('Dimes', 10), ('Nickels', 5), ('Pennies', 1)):
        count = int(pennies / value)
        pennies -= count * value
        resultName.append(name)
        resultCount.append(count)
    result = dict(zip(resultName,resultCount))
    return result


if moneyTaken > productPrice:
    change = moneyTaken - productPrice
    totalChange = parse_change(change)
    print(f'Money given {moneyTaken}')
    print(f'Product Cost{productPrice}')
    print()
    print('-------------')
    print('Remaining Change should be return in')
    print('-------------')
    print(f"Quarters : {totalChange['Quarters']}")
    print(f"Dimes : {totalChange['Dimes']}")
    print(f"Nickels : {totalChange['Nickels']}")
    print(f"Pennies : {totalChange['Pennies']}")




