def power(x, n):
    if not isinstance(x, (int,float)):
        raise TypeError('Bad opearand type')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
