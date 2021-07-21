# Map Functions Handling Numbers
Nums = [1, 2, 3, 4, 5, 6, 7]

incremented_Nums = list(map(lambda num : num * num, Nums))

print("Map Functions Handling Numbers")
print(incremented_Nums)

# Map Functions Handling Strings
Fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']

transformed_Fruits = list(map(lambda fruits : str.upper(fruits), Fruits))

print("\nMap Functions Handling Strings")
print(transformed_Fruits)