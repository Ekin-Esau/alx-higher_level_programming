#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv[1:]) != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    operators = ("+", "-", "*", "/")

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator not in operators:
        print(f"Unknown operator. Abailable operators: +, -, *, and /")
        exit(1)
    
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
    elif operator == "-":
        print(f"{a} + {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} + {b} = {mul(a, b)}")
    else:
        print(f"{a} + {b} = {div(a, b)}")
