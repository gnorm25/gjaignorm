def solution(n, computers):
    
    
    
    def conn_idx(idx): 
        result= []
        for jdx, conn in enumerate(computers[idx]): 
            if idx!=jdx and conn==1: 
                result.append(jdx)
        return result
    

    visited= [1]*n
    
    def dfs(idx): 
        visited[idx]=0
        for n_idx in conn_idx(idx): 
            if visited[n_idx]==1: 
                dfs(n_idx)
        
    answer= 0
    
    for idx in range(n): 
        if visited[idx]==1: 
            dfs(idx)
            answer+=1
            
    return answer