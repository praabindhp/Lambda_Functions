from functools import reduce

ori_Values = [1, 2, 3, 4, 5]

# Reduce Functions To Sum Up The Values

result = reduce(lambda x, y : x + y, range(1, 100, 2))
ori_Result = reduce(lambda x, y : x + y, ori_Values)

print("The Range Generated Result :", result)
print("The Original Result :", ori_Result)

# Generating Initials
Names = ['Bindhu', 'Pradeep', 'Praabindh', 'Prathyush']

name_Result = reduce(lambda name1, name2 : name1[0] + name2[0], Names)
print("The Name Initial Gen Result : ", name_Result)

# Generating The Min & Max Values
int_Values = [1, -5, 15, 36, -84, 45]

Min_Val = reduce(lambda x, y : x if x < y else y, int_Values)
Max_Val = reduce(lambda x, y : y if x < y else x, int_Values)

print("The Minimum Value : ", Min_Val)
print("The Maximum Value : ", Max_Val)