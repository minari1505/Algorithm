#예산, Lv1
def solution(d, budget):
    answer = 0  # 예산 배정 가능한 부서의 개수 저장
    cnt = 0  # 지금까지 배정한 예산 저장할 변수
    # 1.필요예산이 적은 부서부터 정렬
    d.sort()

    for i in d:
        cnt += i
        if cnt <= budget:
            answer += 1
        else:
            break

    return answer