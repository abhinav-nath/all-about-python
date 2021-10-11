def print_factors(num):
    print("The factors of ", num, " are:")

    # // is int division operator
    # range() only supports integers
    # / always returns a flot
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            print(i)
    print(num)


number = int(input("Enter a number: "))
print_factors(number)
