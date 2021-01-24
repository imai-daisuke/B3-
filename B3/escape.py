for j in range(9):
    change=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c=0
    for i in range(15):
        if random.random()>0.01:
            continue
        else:
            c=1
        change[i]=c
    print(change)