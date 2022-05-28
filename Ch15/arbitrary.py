from multiprocessing.sharedctypes import Value
from typing import Type


with open('input.dat', 'r') as file:
    nums = [value.strip() for value in file if value]

for num in nums:
    expression = f"{num} // 2 + 2"
    try:
        answer = eval(expression)
    except (NameError, ValueError, TypeError, SyntaxError) as e:
        print(e)
    finally:
        code = "print('The answer is', answer)"
        obj = compile(code, '<string>', mode='exec')
        exec(obj)
