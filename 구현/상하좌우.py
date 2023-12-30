#상하좌우
def udlr(n):
    r, c = 1, 1
    plans = input().split()

    #U,D,L,R에 따른 방향이동 설정하기
    nr = [1,0,-1,0]
    nc = [0,1,0,-1]
    move_types = ["R","D","L","U"]

    #이동 계획을 확인하기
    for plan in plans:
        #이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nnr = r + nr[i]
                nnc = c + nc[i]

        #공간을 벗어나는 경우 무시
        if nr < 1 or nr > n or nc < 1 or nc > n :
            continue
        #이동 수행
        r,c = nr, nc

    print(r, c)


udlr(5)

pass
