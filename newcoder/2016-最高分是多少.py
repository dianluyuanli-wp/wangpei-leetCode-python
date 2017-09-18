while True:
    try:
        data=map(int,raw_input().split())
        if not data:
            break
        N=data[0]
        M=data[1]
        marks=map(int,raw_input().split())
        for i in range(M):
            com=raw_input().split()
            fir=int(com[1])
            sec=int(com[2])
            if com[0]=='Q':
                if fir>sec:
                    fir,sec=sec,fir
                print max(marks[fir-1:sec])
            else :
                marks[fir-1]=sec
    except:
        break
