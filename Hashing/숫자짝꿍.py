#131128, 숫자 짝꿍

# 1. X,Y의 교집합만들기
# 2. for문 돌리면서, 교집합 원소들의 min 갯수를 answer에 저장하기(중복값이 존재할수도 있기 때문)
# 3. answer 내림차순 정렬
# 4. answer가 없으면 return -1
# 5. answer가 0이면 return 0
# 6. return answer

def solution(X, Y):
    answer = []
    # 1.
    XY = list(set(X) & set(Y))

    # 2.
    for i in XY:
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)

    # 3.
    answer.sort(reverse=True)

    4.
    if len(answer) == 0:
        return '-1'

    # 5.
    if answer[0] == '0':
        return '0'

    # 6.
    return ''.join(answer)

