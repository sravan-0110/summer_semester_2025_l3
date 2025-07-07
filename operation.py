print("a = sum")
print("b = difference")
print("c = product")
print("o = division")

m = input("Enter your operator: ")

if m == "a":
    z = int(input("Enter num 1: "))
    j = int(input("Enter num 2: "))
    y = z + j
    print(y, "is the sum")
elif m == "b":
    z = int(input("Enter num 1: "))
    j = int(input("Enter num 2: "))
    y = z - j
    print(y, "is the difference")

elif m == "c":
    z = int(input("Enter num 1: "))
    j = int(input("Enter num 2: "))
    y = z * j
    print(y, "is the product")

elif m == "o":
    z = int(input("Enter num 1: "))
    j = int(input("Enter num 2: "))
    if j != 0:
        y = z / j
        print(y, "is the division")
    else:
        print("Error: Division by zero")

else:
    print("Error: Invalid operator")
