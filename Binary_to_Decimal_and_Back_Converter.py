# Decimal to Binary and Binary to Decimal


def decimal_to_binary(n):
    if n > 1:
        # divide with integral result
        # (discard remainder)
        decimal_to_binary(n // 2)
    print(n % 2, end=' ')


def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)

# Driver code


if __name__ == '__main__':
    decimal_to_binary(8)

    print("\n")

    decimal_to_binary(18)

    print("\n")

    decimal_to_binary(7)

    print("\n")


if __name__ == '__main__':
    binary_to_decimal(1000)

    binary_to_decimal(10010)

    binary_to_decimal(111)

