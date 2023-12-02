#138476, 귤 고르기

# k : 한 상자에 담으려는 귤의 개수
# tangerine : 귤의 크기를 담은 배열

# 귤 크기별 분류 시 다른 종류의 수를 최소화
# 1. key: 귤의 크기  value : 귤의 크기 별 개수 담기
# 2. dict 내림차순 정렬
# return : 귤의 다른 크기 수

import collections


def solution(k, tangerine):
    answer = 0
    # 1.
    tan_dic = collections.defaultdict(int)  # 귤의 크기 별 개수 담을 dict
    for i in tangerine:
        tan_dic[i] += 1

    # 2.
    tan_dic = sorted(tan_dic.items(), key=lambda x: x[1], reverse=True)

    # 3.cnt로 k개가 넘었는지 확인하면서 answer 찾기
    cnt = 0
    for i in tan_dic:
        cnt += i[1]
        answer += 1
        if cnt >= k:
            break

    return answer