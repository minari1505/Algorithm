#160586, 대충 만든 자판

# 특정 문자열 작성 시, 키를 최소 몇 번 눌러야 작성 가능한 지

# 1.dict key에 A~Z, value에 min(keymap) 위치 넣어놓으면..?
# 2.target 돌면서 cnt 계산, answer에 값 저장
def solution(keymap, targets):
    answer = []
    # 1.
    alp_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
                'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for i in keymap:
        for j in range(len(i)):
            if alp_dict[i[j]] == 0:
                alp_dict[i[j]] += j + 1
            else:
                alp_dict[i[j]] = min(j + 1, alp_dict[i[j]])

    # 2.
    for i in targets:
        cnt = 0
        for j in range(len(i)):
            if alp_dict[i[j]] == 0:
                cnt = -1
                break
            else:
                cnt += alp_dict[i[j]]
        answer.append(cnt)

    return answer