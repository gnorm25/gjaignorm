N= int(input())
xxx= []
for x in range(N): 
    xxx.append(str(input()))
xxx= list(set(xxx))
xxx.sort()
dam= []
N = len(xxx)
for x in range(N): 
    for y in range(x+1, N): 
        if xxx[x]== xxx[y][:len(xxx[x])]:
            dam.append(xxx[x])
            break
xxx= set(xxx)
dam= set(dam)
k= len(xxx-dam)
if k<= 0: 
    k= 1
print(k)