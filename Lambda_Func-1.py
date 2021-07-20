# Normal Incremental Function
def incrementNormal(x):
    return x + 20

# Lambda Expression
incrementLamba = lambda x : x * 3

print("The Increment Normal : ", incrementNormal(50))
print("The Increment Lamba : ", incrementLamba(15))

productLamba = lambda x, y : x * y
print("The Produt Lamba : ", productLamba(15, 3))

# # Printing The Type
# print(type(incrementNormal))
# print(type(incrementLamba))