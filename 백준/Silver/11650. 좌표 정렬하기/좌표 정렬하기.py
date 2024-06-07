count= int(input())

setlist=[]
for x in range(count): 
    setlist.append(tuple(map(int, input().split())))

setlist.sort()
for x in setlist: 
    print(f'{x[0]} {x[1]}')
