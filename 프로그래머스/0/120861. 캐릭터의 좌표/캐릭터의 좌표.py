def solution(keyinput, board):
    now= [0, 0]
    
    for x in keyinput: 
        if x=='right': 
            if now[0]==board[0]//2:
                pass
            else: 
                now[0]+=1
        elif x=='left': 
            if now[0]==-1*(board[0]//2):
                pass
            else: 
                now[0]-=1
        elif x=='up': 
            if now[1]==board[1]//2:
                pass
            else: 
                now[1]+=1
        elif x=='down': 
            if now[1]==-1*(board[1]//2):
                pass
            else: 
                now[1]-=1
    return now
            