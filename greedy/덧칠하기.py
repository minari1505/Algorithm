#그리디, 161989
# section 가장 작은 부분에 페인트칠 시작, m까지 숫자 안에 다음 숫자가 있다면 pass 없다면 +1, 다시 m까지 숫자 정의

def solution(n, m, section):
    answer = 1
    first = section[0]  # 롤러가 처음 닿을 부분
    f_m = section[0] + (m - 1)  # 페인트칠 한 번에 칠해질 수 있는 거리

    for i in range(1, len(section)):
        if section[i] <= f_m:
            pass
        else:
            answer += 1
            first = section[i]
            f_m = section[i] + (m - 1)
    return answer

n = 8
m = 4
section = [2,3,6]
solution(n,m,section)