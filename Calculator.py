def add(a,b):
    return(a + b)


def subtract(a,b):
    return(a - b)


def multpily(a,b):
    return(a * b)


def divide(a,b):
    return(a / b)




while True:
    first_num = int(input("First number: "))


    print("operations: 1.add  2.Subtract 3.Multiply  4.Divide")


    operation = input("operation: ")
    second_num = int(input("second number: "))

    if operation == "1" :
        print(add(first_num , second_num))

    if operation == "2":
        print(subtract(first_num , second_num))

    if operation == "3":
        print(multpily(first_num, second_num))

    if operation == "4":
        print(divide(first_num, second_num))


    else:
        print("Invalid Operation Input")

        break







