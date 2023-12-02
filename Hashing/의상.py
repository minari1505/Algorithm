#42578, 의상
# 1.clothes를 dict로 변환
# 2.answer 값을 1로 두고, 가능한 경우의 수를 곱하기

import collections

def solution(clothes):
    # 1.
    cody = collections.defaultdict(list)
    for i in clothes:
        cody[i[1]].append(i[0])

    # 2.
    answer = 1

    for i in cody:
        answer *= (len(cody[i]) + 1) #+1 의 이유 : 아무것도 입지 않는 선택지가 있음

    return answer - 1 #-1의 이유 : 모두 '아무것도 입지 않음'을 선택했을 경우를 제외함