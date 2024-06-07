import sys

inp= sys.stdin.readline

N = int(inp())

a = []

for i in range(N):
    a.append(int(inp()))


# # 버블 정렬
# for i in range(N):
#     for j in range(N-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
a.sort()


for i in range(N):
    print(a[i])