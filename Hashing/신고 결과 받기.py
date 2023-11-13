#신고결과받기,Lv1

import collections

def solution(id_list, report, k):
    answer = []
    # 1.동일 유저에 대한 신고 -> 1번으로 침. -> set
    report = list(set(report))

    # 2.신고한 유저 -> 신고당한 유저, 신고당한 유저-> 신고당한 횟수 dict 생성
    reported = collections.defaultdict(list)
    ed_num = collections.defaultdict(int)

    # 3.신고한 유저 -> 신고당한 유저, 신고당한유저 -> 신고당한 횟수 dict 채우기
    for i in report:
        t, ed = i.split(' ')
        reported[t].append(ed)
        ed_num[ed] += 1

    # 4. k가 넘는만큼 신고당한 사람이 list안에 있다면 cnt += 1
    cnt = 0
    for i in id_list:  # i = muzi, frodo, apeach, neo
        for j in reported[i]:  # reported[i] = ['frodo','neo']
            if ed_num[j] >= k:
                cnt += 1
        answer.append(cnt)
        cnt = 0

    return answer