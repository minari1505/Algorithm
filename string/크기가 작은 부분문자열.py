#크기가 작은 부분문자열, 147355

#for문 사용
def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1

    return answer

#while문 사용
def solution(t, p):
    answer = 0
    i = 0
    while i+len(p)-1 < len(t):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
        i += 1
    return answer