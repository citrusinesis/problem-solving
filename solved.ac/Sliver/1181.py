import sys
from functools import cmp_to_key

read = sys.stdin.readline

words = [read().strip() for _ in range(int(read()))]
words = list(set(words))
words.sort(key = lambda x: (len(x), x))

for word in words:
    sys.stdout.write(word + '\n')