N= int(input()) 
score= [] 
for _ in range(N): 
    score.append(input().split()) 

while [x for x in score if x[0]=='undo']:
    for x in score[::-1]: 
        if x[0]=='undo': 
            t= int(x[2])
            count_= t-int(x[1]) 
            score= [x for x in score if int(x[2])<count_ or int(x[2])>t] 
            break
answer= ''
for x in score: 
    answer+= x[1] 

print(answer) 