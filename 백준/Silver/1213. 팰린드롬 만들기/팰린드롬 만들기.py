name= input()
name= sorted(name)

from collections import Counter
count_= Counter(name)

odd= 0
mid= []
for k, x in count_.items(): 
    if x%2==1: 
        odd+= 1
        mid.append(k)
    if odd>=2: 
        print("I'm Sorry Hansoo")
        break

if odd<=1: 
    n_name= name[1::2]
    answer= n_name+mid+sorted(n_name, reverse= True)
    print(''.join(answer))