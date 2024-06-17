def solution(bandage, health, attacks):
    
    hp= health
    start= 1
    
    for x, y in attacks: 
        hp+= (x-start)*bandage[1]
        hp+= ((x-start)//bandage[0])*bandage[2]
        start= x+1
        if hp>health: 
            hp=health
        hp-= y
        if hp<=0: 
            return -1
    return hp
            
        