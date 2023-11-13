#보석 쇼핑, Lv3
import collections

def solution(gems):
    answer = [0, 0]
    sH = collections.defaultdict(int)
    k = len(set(gems))  # 보석종류의 수
    lt = 0
    maxL = 100000  # 최대 길이
    for rt in range(len(gems)):  # lt는 정해져있고, rt를 늘려가면서 확인하기
        sH[gems[rt]] += 1  # sH, key = 보석이름, value += 1

        while (len(sH) == k):  # sH 길이가 보석종류의 수와 같다면
            if rt - lt + 1 < maxL:  # rt-lt+1 : 구간의 길이
                maxL = rt - lt + 1  # maxL을 구간길이로 변경
                answer = [lt + 1, rt + 1]  # answer를 lt,rt 번호 +1(각 진열대 번호)로 변경
            sH[gems[lt]] -= 1  # lt를 한 칸 옆으로 옮기기 위해, 진열대번호 lt에 있는 보석에 -1해주기

            # !lt를 하나 지웠는데,갯수가 0이 된다면 key를 지워버려야 while문 True가 되지 않음!
            if sH[gems[lt]] == 0:
                del sH[gems[lt]]

            lt += 1  # lt를 오른쪽으로 한 칸 옮기기
    return answer