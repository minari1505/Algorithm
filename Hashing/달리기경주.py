#178871, 달리기 경주
#실패, 9~13 시간초과

def solution(players, callings):
    # 1. 인덱스 변경
    for i in callings:
        idx = players.index(i)
        players[idx], players[idx - 1] = players[idx - 1], players[idx]

    return players