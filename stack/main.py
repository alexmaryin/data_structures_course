from stack_min_supported import StackMinSupported


def main():
    stack = StackMinSupported()
    is_exit = False
    while not is_exit:
        raw = input("Enter command (u(push) #value / p(pop) / size / r(print) / e(xit): ").split()
        if raw:
            command = raw[0]
            if command == 'e':
                is_exit = True
            elif command == 'u':
                stack.push(raw[1])
                print(f"Value {raw[1]} append to stack")
            elif command == 'p':
                n = stack.pop()
                print(f"Pop value {n} from stack" if n else "Stack is empty!")
            elif command == 'size':
                print(f'Stack size is {stack.size()} items')
            elif command == "r":
                print(stack)


if __name__ == '__main__':
    main()
