def solution(id_list, report, k):
    set_rpt= set(report)
    report_spl=[]
    ban={}
    id_dic = dict.fromkeys(id_list, 0)
    
    
    for x in set_rpt: 
        pl= x.split()
        ban.setdefault(pl[1], 0)
        ban[pl[1]]+=1
        report_spl.append(pl)
        
    for a, z in report_spl: 
        if ban[z]>=k: 
            id_dic[a]+=1
    return list(id_dic.values())