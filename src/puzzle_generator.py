import random
def puzzle_generator(level):
    if level=="Easy":
        a=random.randint(0,10)
        b=random.randint(0,10)
        op=random.choice(["+","-"])
        if op=="-" and b>a:
            a,b=b,a
        res=a+b if op=="+" else a-b

    elif level=="Medium":
        a=random.randint(10,50)
        b=random.randint(10,50)
        op=random.choice(["+","-"])
        if op=="-" and b>a:
            a,b=b,a
        res=a+b if op=="+" else a-b

    else:
        a=random.randint(20,200)
        b=random.randint(2,20)
        op=random.choice(["+","-","/","*"])
        if op=="-" and b>a:
            a,b=b,a
        if op=="+":
            res=a+b
        elif op=="-":
            res=a-b
        elif op=="*":
            res=a*b
        else:
            res= a/b
    question=f"{a} {op} {b}"
    return question,res