#42576, 완주하지 못한 선수

# 1. participant, completion 둘 다 sort
# 2. comp~ 기준, for문 중간에 완주하지 못한 친구가 있다면 return
# 3. for문 중간에 완주하지 못한 친구가 없다면 return participant[-1]
def solution(participant, completion):
    # 1.
    participant.sort()
    completion.sort()

    # 2.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
