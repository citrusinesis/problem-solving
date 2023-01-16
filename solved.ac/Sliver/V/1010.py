import sys

factorial = lambda x: x * factorial(x-1) if x > 0 else 1
combination = lambda m, n: factorial(n) // (factorial(n-m) * factorial(m))

testCase = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
for case in testCase:
    sys.stdout.write(str(combination(case[0], case[1])) + '\n')