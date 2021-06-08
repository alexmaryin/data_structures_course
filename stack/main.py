import sys

from stack_max_supported import StackMaxSupported


def main():
    stack = StackMaxSupported()
    commands_count = next(sys.stdin)
    commands = [line.split() for line in list(sys.stdin)]
    for command in commands:
        if command[0] == 'push':
            stack.push(command[1])
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'max':
            print(stack.max())


if __name__ == '__main__':
    main()
