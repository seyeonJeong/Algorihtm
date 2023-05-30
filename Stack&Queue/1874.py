import sys

n = int(sys.stdin.readline())

nums = []
for i in range(n):
    a = int(sys.stdin.readline())
    nums.append(a)

stack = []

# ing..
for j in range(n):
    if j == nums[j]:
        stack.pop()
        print('-')
    else:
        stack.append(j)
        print('+')

k = 0
while True:
    k += 1
    stack.append(k)
    print('+')
    if k == nums[j]:
        stack.pop()
        print('-')

