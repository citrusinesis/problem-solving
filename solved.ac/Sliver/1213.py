import sys

read = sys.stdin.readline
write = sys.stdout.write

count = {}
for item in list(read().strip()):
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

odd = []
even = []
for key, value in count.items():
    if value % 2 == 0:
        even.append(key)
    else:
        odd.append(key)

if len(odd) > 1:
    write("I'm Sorry Hansoo")
    quit()

result = ""
words = odd + even

words.sort()
for item in words:
    for i in range(count[item] // 2):
        result += item

if len(odd) != 0:
    result += odd.pop()

words.reverse()
for item in words:
    for i in range(count[item] // 2):
        result += item

write(result)