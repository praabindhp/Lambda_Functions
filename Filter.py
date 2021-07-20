# Filter Items As Per The Lambda Conditions
Nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Even_Nums_Filter = filter(lambda x : x % 2 == 0, Nums)

Even_Nums = list(filter(lambda x : x % 2 == 0, Nums))

Odd_Nums = list(filter(lambda x : x % 2 != 0, Nums))

print("The Filter Output : ", Even_Nums_Filter)
print("The Even Nums : ", Even_Nums)
print("The Odd Nums : ", Odd_Nums)

Fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Cherry', 'Berry', 'Custard', 'Grapes']

Filtered_Fruits = list(filter(lambda fruit : len(fruit) < 8, Fruits))
print(Filtered_Fruits)