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

# Map Functions Returning Length Of Strings
len_of_Fruits = list(map(lambda fruits : len(fruits), Fruits))

print("\nMap Functions Returning Length Of Strings")
print(len_of_Fruits)

# Map Functions With Multiple Data Structures
Nums_01 = [1, 2, 3, 4]
Nums_02 = [5, 6, 7, 8, 9] # Evaluates The Lower Size While Merging

print("\nMap Functions Multiple Data Structures")
merged_Nums = list(map(lambda x, y : x + y, Nums_01, Nums_02))
print(merged_Nums)