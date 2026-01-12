""" In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

    Unlike Java and many other languages, Python variables do not require explicit declaration of type.
    The type of the variable is inferred based on the value assigned.
"""

""" Rules for Naming Variables
To use variables effectively, we must follow Python’s naming rules:

    Variable names can only contain letters, digits and underscores (_).
    A variable name cannot start with a digit.
    Variable names are case-sensitive like myVar and myvar are different.
    Avoid using Python keywords like if, else, for as variable names.
"""

x = 10
"""
stack: 
    |x->@ref_A| 
heap: 
    ref_A:
        - object: int
        - value: 10
"""
y = str(x)
"""
stack:  
    |y->@ref_B|
    |x->@ref_A|
heap: 
    ref_A:
        - object: int
        - value: 10
    ref_B:
        - object: str
        - value: '10'
"""

z = int(y)
"""
stack:  
    |z->@ref_C|
    |y->@ref_B|
    |x->@ref_A|
heap: 
    ref_A:
        - object: int
        - value: 10
    ref_B:
        - object: str
        - value: '10'
    ref_C:
        - object: int
        - value: 10
"""

k = float(z)
"""
stack:  
    |k->@ref_D|
    |z->@ref_C|
    |y->@ref_B|
    |x->@ref_A|
heap: 
    ref_A:
        - object: int
        - value: 10
    ref_B:
        - object: str
        - value: '10'
    ref_C:
        - object: int
        - value: 10
    ref_D:
        - object: float
        - value: 10.0
"""

print("Value of x:", x, ", Type of x:", type(x))
print("Value of y:", y, ", Type of y:", type(y))
print("Value of z:", z, ", Type of z:", type(z))
print("Value of k:", k, ", Type of k:", type(k))