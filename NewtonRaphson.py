#Pranta__Kumar_Biswas_Code
import math
def func(x):
    return 3 * x + math.sin(x) - math.exp(x)
def derivfun(x):
    return 3  + math.cos(x) - math.exp(x)
def newton(a,b) :
    if (func(a) * func(b) < 0):
        m = (a + b) / 2
    else:
        print("Root is not here.")
    while (derivfun(m) > 0):
        h=func(m)/derivfun(m)
        if(h==0.0):
            break
        m=m-h
    print("The value of root is : ", "%.8f" % m)
a = float(input('Enter First Value: '))
b = float(input('Enter Second Value: '))
newton(a,b)