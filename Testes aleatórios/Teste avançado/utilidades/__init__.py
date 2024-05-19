def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b

def fat(a):
    fat = 1
    for c in range(1, 1+a):
        fat *= c
    return fat
