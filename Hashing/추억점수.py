#176963, 추억점수

# 1. name:key, yearning:value인 dict생성
# 2. photo 돌면서 추억점수 계산 -> answer에 저장
import collections


def solution(name, yearning, photo):
    answer = []

    # 1.
    score_dict = collections.defaultdict(int)
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]

    # 2.
    for i in photo:
        cnt = 0  # 추억점수 저장할 변수
        for j in i:
            cnt += score_dict[j]
        answer.append(cnt)
    return answer


