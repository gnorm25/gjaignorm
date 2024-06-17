def solution(bandage, health, attacks):
    
    hp= health
    count=0
    
    for x in range(1, attacks[-1][0]+1): 
        if x==attacks[0][0]: 
            hp-= attacks[0][1]
            count= 0
            attacks.pop(0)
            if hp<=0: 
                return -1
        else: 
            hp+= bandage[1]
            count+= 1
            if count==bandage[0]: 
                hp+= bandage[2]
                count= 0
        if hp>health: 
            hp= health
    return hp
            
            
        