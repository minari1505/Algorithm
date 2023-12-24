#n : 전체 학생 수, lost : 체육복을 도난당한 학생들, reserve : 여분의 체육복이 있는 학생 번호
#0. reserve, lost 오름차순 정렬
#1. reserve - lost : 찐 reserve
#2. reserve에 있는 숫자의 앞뒤가 lost에 있다면 reserve, lost 지우고, 없다면 answer-1
def solution(n, lost, reserve):
    answer = n #시작을 모두 수업을 들을 수 있는 경우로 가정
    losts = lost.copy()
    
    #0. lost, reserve 오름차순 정렬
    lost.sort()
    reserve.sort()
    #1.
    for i in losts:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    #2.
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            answer -= 1
            
    return answer
