"""
Simple Python Calculator (v1.0)
- Supports +, -, *, / operations
- Saves calculation history in history.txt
- Preserves calculation numbering across runs
"""
def calculate(expr):
    """
    Takes a string expression
    Returns the result of the calculation or an error message
    Handles +, -, *, / and invalid input safely
    """
    #splits the expression into parts: number1, operator, number2
    parts = expr.split() 
    if len(parts)!=3:
        return "Invalid input. Use format: num1 operator num2"
    num1, op, num2 = parts
    #converts string to float, catch invalid numbers
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid Number format."
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    elif op=="/":
        return "Cannot divide by 0" if num2==0 else num1/num2
    else:
        return "Unknow Operator"
try:
    with open("history.txt", "r") as history:
        lines = history.readlines()
        last_calc = 0
        for line in reversed(lines):
            if "Calculation" in line:
                last_calc = int(line.strip().split()[2])
                break
# Reads history.txt to find the last calculation number
# This ensures numbering continues across program runs
except FileNotFoundError:
    last_calc = 0
with open("history.txt", "a") as history:
    c = last_calc+1
    while True:
        history.write(f"--- Calculation {c} ---\n")
        expr = input("Enter an expression with spaces(eg.- 4 + 5): ")
        result = calculate(expr)
        print("Result:", result)
        history.write(f"{expr} = {result}\n")
        history.write("----------------------\n")
        cont = input("Do you wish to continue (Y/N): ").strip().lower()
        c = c+1
        if cont!="y":
            print("Thank you")
            break
# TODO: Handle multi-operator expressions in future version
