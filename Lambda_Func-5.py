# Lambda Functions Acts Implicitly According To The Input Parameters

def int_Multiply(x):
    return lambda c : c * x

int_Double = int_Multiply(2)
int_Triple = int_Multiply(3)
int_Tenfold = int_Multiply(10)

print("Integer Doubled Value : ", int_Double(10))
print("Integer Tripled Value : ", int_Triple(10))
print("Integer Ten Folded Value : ", int_Tenfold(10))