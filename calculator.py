# Python program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
    
def dec2bi(dec):
    if dec > 1:
        dec2bi(dec//2)
    print (dec % 2, end="")
    
    
