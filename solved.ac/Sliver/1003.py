import sys

read = sys.stdin.readline
write = sys.stdout.write

for _ in range(int(read())):
    zero, one = 1, 0
    for i in range(int(read())):
        zero, one = one, zero + one
    write(str(zero) + ' ' + str(one) + '\n')