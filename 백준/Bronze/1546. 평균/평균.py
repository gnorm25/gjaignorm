N= int(input())
score= list(map(int, input().split()))
M= max(score)
print(sum(score)/N/M*100)