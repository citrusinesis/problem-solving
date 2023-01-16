import sys
from functools import reduce

read = sys.stdin.readline
write = sys.stdout.write

def reducer(acc, cur):
    before = ''
    check = []

    for i in list(cur):
        if i != before and i in check:
            return acc
        before = i
        check.append(i)

    return acc + 1

words = [read().strip() for _ in range(int(read()))]
write(str(reduce(reducer, words, 0)))