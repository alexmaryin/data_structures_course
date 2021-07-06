if __name__ == '__main__':
    count = int(input())
    book = {}
    log = []
    for _ in range(count):
        command = input().split()
        if command[0] == 'add':
            book[command[1]] = command[2]
        if command[0] == 'del':
            book.pop(command[1], None)
        if command[0] == 'find':
            log.append(book.get(command[1]) or 'not found')
    for l in log: print(l)
