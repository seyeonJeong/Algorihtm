import sys

n = int(sys.stdin.readline())
score = list(map(float, sys.stdin.readline().strip().split()))


max = max(score)
for i in range(n):
    score[i] = score[i] / max * 100

print(sum(score) / n)




