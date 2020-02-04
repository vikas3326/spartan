x1 =  int(input('enter coefficient of x of first equation: '))
y1 = int(input('enter coeffucient of y of equation 1: '))
x2 = int(input('enter coefficient of x of equation 2: '))
y2 = int(input('enter coefficient of equation 2: '))
c1 = int(input('enter constant 1: '))
c2 = int(input('enter constant 2: '))
k = x2
j = x1
x1 = x1 * k
x2 = x2 * j
if x1 == x2:
    print('y value is is:' )
    y = float((((c1 * k)-(c2 * j))//((y1 * k)-(y2 * j))))
    print(y)
    print('x value is: ')
    x = float(((c1-(y1 * y))/j))
    print(x)
else:
    print('not possible')
