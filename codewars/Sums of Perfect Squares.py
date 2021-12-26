import math
def isSquare(x):
    sqRoot = int(math.sqrt(x));
    return (sqRoot * sqRoot == x);
def sum_of_squares(n):
    if (isSquare(n)):
        return 1;
    for i in range(1, int(math.sqrt(n))):
        if (isSquare(n - (i * i))):
            return 2;
    while (n % 4 == 0):
        n >>= 2;
    if (n % 8 == 7):
        return 4;
    return 3;