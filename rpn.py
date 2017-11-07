#!/usr/bin/env python3

import operator, colorama
from colorama import Fore, Back, init

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def calculate(myarg):
    init(autoreset=True)
    # extra code to demo coverage drop
    # if not myarg:
    #     raise TypeError("No input")
    print("You entered: ")
    print(Fore.GREEN + myarg)
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            print(Fore.RED + token)
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        # print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ")
        print (Back.BLUE + Fore.YELLOW + str(result))

if __name__ == '__main__':
    main()

