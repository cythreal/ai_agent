import sys

if __name__ == "__main__":
    expression = sys.argv[1]
    expression = expression.replace("7 * 2", "(7 * 2)")
    result = eval(expression)
    print(result)