# Lambda Functions Are Anonymous Functions
# Declared By Checking The Traceback

def customFunc(x):
    return x / 0

lambdaFunc = lambda x : x / 0

print("Custom Function : ",customFunc(20)) # Show Error - customFunc
print("Lambda Function : ",lambdaFunc(10)) # Show Error - lambdaFunc