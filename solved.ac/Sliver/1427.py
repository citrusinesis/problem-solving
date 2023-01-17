import sys

read = sys.stdin.readline
write = sys.stdout.write

numbers = list(map(int, list(read().strip())))
for number in sorted(numbers, reverse = True):
    write(str(number))