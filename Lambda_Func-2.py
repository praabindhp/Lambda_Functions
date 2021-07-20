# Normal Lambda Expression
lambda_Func = lambda x, y : x + y

print("Normal Lambda : ",lambda_Func(x = 15, y =20))

# Argumental Lambda Expression
lambda_Args = lambda *args : sum(args)

print("Args Lambda : ",lambda_Args(10,20,30,40,50))

# Key Value Argumental Lambda Expression
lambda_KeyArgs = lambda **args : sum(args.values())

print("Key Value Args Lambda : ",lambda_KeyArgs(one = 1, three = 3, five = 5, seven = 7))