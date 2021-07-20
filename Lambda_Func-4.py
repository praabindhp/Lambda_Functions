# Lambda Functions Are Anonymous Functions
# Normal / Standard Functions Can Not Be Called Immediately
# Lambda Expressions Are Immediately Invoked Functional Expressions (IIFEs)
 
def customFunc(x): # Standard Functions
    print("Standard Functions : ", x + 10)

customFunc(20)

print("Lambda - IIFE : ",(lambda x : x + 10)(20)) # Lambda Expressions