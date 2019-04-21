def collatz(number):
    operation = 0
    if (number % 2) == 0:
        operation = number // 2
        print(operation)
    elif number % 2 == 1:
        operation = 3 * number + 1
        print(operation)

    if operation != 1:
        collatz(operation)


print('Enter number: ')
num1 = int(input())
collatz(num1)