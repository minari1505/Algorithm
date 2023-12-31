#왕실의 나이트
#이동방법 : +-(2,1), +-(1,2)
#나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수 출력

#현재 위치
data = input()
r = int(data[1])
c = int(ord(data[0])) - int(ord('a')) + 1

#이동가능한 방향 8개
step  = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

#각 방향으로 이동이 가능하면 +1, 불가능하면 pass
cnt = 0
for i in step:
    nr = r + step[0]
    nc = c + step[1]
    #해당 위치로 이동가능하면 cnt+=1
    if nr >= 1 and nr <= 8 and nc>=1 and nc<=8:
        cnt +=1

print(cnt)


