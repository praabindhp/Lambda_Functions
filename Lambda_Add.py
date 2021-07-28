a = int(input("Enter A : "))
b = int(input("Enter B : "))

sum = lambda x, y : x + y

print("Sum ({} + {}) : ".format(a, b), sum(a, b))