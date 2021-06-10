from typing import Tuple

from stack.stack import Stack

BRACKETS_SYMBOLS = ('{', '}', '(', ')', '[', ']')
BRACKETS_PAIRS = {'{': '}', '(': ')', '[': ']'}


def check_expected_bracket(brackets, closed):
    if brackets.size() > 0:
        opened = brackets.last()[0]
        if BRACKETS_PAIRS[opened] == closed:
            brackets.pop()
            return True
    else:
        return False


def main():
    brackets = Stack[Tuple[str, int]]()
    s = input('Pass string with brackets to parse: ')
    for index in range(len(s)):
        if s[index] in BRACKETS_PAIRS.keys():
            brackets.push((s[index], index))
        elif s[index] in BRACKETS_SYMBOLS and not check_expected_bracket(brackets, s[index]):
            print(f'Unexpected bracket in {index + 1} position!')
            break
    if brackets.size() > 0:
        unclosed = brackets.pop()
        print(f'Unclosed bracket {unclosed[0]} in {unclosed[1] + 1} position!')


if __name__ == '__main__':
    main()
