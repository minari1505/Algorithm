#단속카메라, Lv3

def solution(routes):
    answer = 1  # 카메라 대수 카운트
    # 1. 나간지점이 빠른 차부터 정렬하기
    routes.sort(key=lambda x: (x[1], x[0]))

    # 2. for문 돌면서 answer 횟수늘리기
    et = routes[0][1]

    for i in range(1, len(routes)):
        if et < routes[i][0]:
            answer += 1
            et = routes[i][1]

    return answer