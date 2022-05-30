#!/usr/bin/env python3
import ast

equation = input("Enter an equation: ")
result = ast.literal_eval(equation)
print(f"{equation} = {result}")
