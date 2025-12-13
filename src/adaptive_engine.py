def adaptive_engine(curr_lvl,attempts): # shows in format (Medium,2),basically giving the level,number of attempts
    if len(attempts)<3:  #if number of attemots is less than 3,level remains same
        return curr_lvl
    accuracy=sum(1 for c,_ in attempts[-3:] if c)/3 #accuracy and avg time is calculated
    avg_time=sum(t for _,t in attempts[-3:])/3
    levels=["Easy","Medium","Hard"]
    index=levels.index(curr_lvl)

    if accuracy==1 and avg_time<5:
        index=min(index+1,2) #level increases
    elif accuracy<0.5 or avg_time>8:
        index=max(index-1,0) #level decreased
        
    return levels[index]
