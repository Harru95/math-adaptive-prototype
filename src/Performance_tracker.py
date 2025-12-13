def Performance_Tracker(attempts,correct,time_taken):
    attempts.append((correct,time_taken))

def progress_summarize(name,total_q,attempts,path,final_lvl):
    t_correct=sum(1 for c,_ in attempts if c)
    accuracy=(t_correct/total_q)*100
    avg_time=sum(t for _,t in attempts)/len(attempts)

    summary={
        "name":name,
        "total_questions":total_q,
        "correct":t_correct,
        "accuracy":accuracy,
        "avg_time":avg_time,
        "path":path,
        "next_level":final_lvl
    }
    
    return summary