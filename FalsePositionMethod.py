#Pranta__Kumar_Biswas_Code
def f(x):
    return x*x*x-2*x*x-4
def falsePosition(x0,x1,e):
    step = 1
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > e

    print('Root is: %0.8f' % x2)
x0 = input('Enter First Value: ')
x1 = input('Enter Second Value: ')
e = input('Enter Tolerable Error: ')
x0 = float(x0)
x1 = float(x1)
e = float(e)
if f(x0) * f(x1) > 0.0:
    print('Given values do not in the root.')
    print('Try with different  values.')
else:
    falsePosition(x0,x1,e)