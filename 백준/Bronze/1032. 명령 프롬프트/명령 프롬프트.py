N= int(input()) 
xxx= []
for x in range(N): 
    xxx.append(input())
result = []
for i in range(len(xxx[0])):
    set = {s[i] for s in xxx}
    if len(set) == 1:
        result.append(xxx[0][i])  # 모든 문자가 동일하면 그 문자를 추가
    else:
        result.append('?')  # 그렇지 않으면 '?'를 추가

print(''.join(result))