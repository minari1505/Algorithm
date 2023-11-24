#92334, 신고 결과 받기

# 1. 한 유저를 여러번 신고도 가능하지만, 신고횟수는 1번으로 처리 -> set으로 중복지우기
# 2. 신고한유저->신고당한유저, 신고당한유저->신고당한횟수 저장할 dict 생성
# 3. k번 이상 신고되면 게시판 이용정지, 정지되었다는 사실을 신고한 유저들에게 보냄
# 4. 신고한 유저가 몇 번 메일을 받는지 return

import collections


def solution(id_list, report, k):
    answer = []  # 신고한 유저가 이메일을 받을 횟수 저장

    re_dic = collections.defaultdict(list)  # 신고한 유저 - 신고당한 유저
    ed_dic = collections.defaultdict(int)  # 신고당한 유저 - 신고당한 횟수

    # 1. 중복 제거
    report = list(set(report))

    # 2. 신고한유저->신고당한유저, 신고당한유저->횟수 저장
    for i in report:
        rep, ed = i.split()  # rep : 신고한 유저, ed: 신고당한 유저
        re_dic[rep].append(ed)  # re_dic에 신고한 유저 -> 신고당한유저 넣기
        ed_dic[ed] += 1

        # 3.re_dic value에 k번 넘은 사람이 있다면, cnt += 1
    for i in id_list:
        cnt = 0
        for j in re_dic[i]:
            if ed_dic[j] >= k:  # 신고당한 유저의 신고당한 횟수가 k번보다 같거나 크다면
                cnt += 1

        answer.append(cnt)

    return answer