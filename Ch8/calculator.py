import logging
from operator import add, sub, mul, truediv
import sys

logging.basicConfig(filename='log.txt', level=logging.INFO)


def calculator(a, b, op):
    a = float(a)
    b = float(b)
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return truediv(a, b)
    else:
        raise NotImplementedError(f"No operator {op}")


print("""CALCULATOR
Use postfix notation.
Ctrl+C or Ctrl+D to quit.
""")

while True:
    try:
        equation = input(" ").split()
        result = calculator(*equation)
        print(result)
    except NotImplementedError as e:
        print("<!> Invalid operator.")
        logging.info(e)
    except ValueError as e:
        print("<!> Expected format: <A> <B> <OP>")
        logging.info(e)
    except TypeError as e:
        print("<!> Wrong number of arguments. Use: <A> <B> <OP>")
        logging.info(e)
    except ZeroDivisionError as e:
        print("<!> Cannot divide by zero.")
        logging.info(e)
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")
        sys.exit(0)
    except Exception as e:
        logging.exception(e)
        raise
