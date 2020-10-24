def addition():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 1
    t += 1
    b = float(input("Enter another number (0 to calculate): "))
    ans = b + n
    return [ans, t]


def subtraction():
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 1
    t += 1
    b = float(input("Enter another number (0 to calculate): "))
    ans = n - b
    return [ans, t]


def multiplication():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 1
    t += 1
    b = float(input("Enter another number (0 to calculate): "))
    ans = b * n
    return [ans, t]


def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans, t]


while True:
    lists = []
    print("Welcome to one of my wonderful python program!")
    print("This is a simple calculator in python by Moi")
    print("Enter 'a' for addition")
    print("Enter 's' for subtraction")
    print("Enter 'm' for multiplication")
    print("Enter 'v' for average")
    print("Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            lists = addition()
            print("Ans = ", lists[0], " total inputs ", lists[1])
        elif c == 's':
            lists = subtraction()
            print("Ans = ", lists[0], " total inputs ", lists[1])
        elif c == 'm':
            lists = multiplication()
            print("Ans = ", lists[0], " total inputs ", lists[1])
        elif c == 'v':
            lists = average()
            print("Ans = ", lists[0], " total inputs ", lists[1])
        else:
            print("Sorry, invalid character")
    else:
        break
