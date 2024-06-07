import sys
inp= sys.stdin.readline
a = []
for i in range(5):
    a.append(int(inp()))
a.sort()

print(sum(a)//len(a), a[len(a)//2])

