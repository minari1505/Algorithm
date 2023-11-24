#178871, 달리기 경주

# 1. pl-rank, rank-pl dict 두 개 생성
# 2. callings에 불릴 때 마다 불린사람의 pl_dic에서의 value값, ra_dic에서의 value값 변경하기
import collections


def solution(players, callings):
    # 1.
    pl_dic = {player: rank for rank, player in enumerate(players)}
    ra_dic = {rank: player for rank, player in enumerate(players)}

    for call in callings:
        rank = pl_dic[call]  # 이름 불린 선수의 현재 랭크

        # pl_dic의 value값 변경하기
        pl_dic[ra_dic[rank - 1]], pl_dic[ra_dic[rank]] = pl_dic[ra_dic[rank]], pl_dic[ra_dic[rank - 1]]

        # ra_dic의 value값 변경하기
        ra_dic[rank - 1], ra_dic[rank] = ra_dic[rank], ra_dic[rank - 1]

    return list(ra_dic.values())