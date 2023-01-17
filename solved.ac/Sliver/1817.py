import sys

read = sys.stdin.readline
write = sys.stdout.write

current = 0
count = 1

books, cap = map(int, read().split())

if books == 0:
    write(str(0))
    quit()

for book in list(map(int, read().split())):
    if current + book > cap:
        current = book
        count += 1

    else:
        current += book

write(str(count))