#92341, 주차 요금 계산
import collections
import math


def solution(fees, records):
    answer = []

    total_time = collections.defaultdict(int)  # 차량별 이용시간 저장할 dict
    check = collections.defaultdict(str)  # 차량별 입출차 기록

    # 기본시간, 기본요금, 단위시간, 단위요금
    basic_t, basic_f, unit_t, unit_f = int(fees[0]), int(fees[1]), int(fees[2]), int(fees[3])

    # 차량별 입출차 기록, 이용시간 기록
    for record in records:
        t, num, io = record.split()  # 시간, 차량번호, i/o

        if num not in check.keys():  # check dic의 key에 num이 없다면 => 입차하지 않은 차량
            check[num] = t  # 입차시간 저장

        else:  # check dic의 key에 num이 있다면 => 입차한 차량
            out_t = int(t.split(':')[0]) * 60 + int(t.split(':')[1])
            in_t = int(check[num].split(':')[0]) * 60 + int(check[num].split(':')[1])

            total_time[num] += out_t - in_t  # total_time[num]에 출차시간-입차시간만큼 저장

            del check[num]  # 출차시간-입차시간 뺀 이후, value를 없애서 이후에 같은 차가 다시 들어올 때를 대비

    # 만약 입차 후 출차하지 않았다면
    oneday = int(23 * 60 + 59)  # 00:00 ~ 23:59를 분으로 변환
    if check:
        for i in check.keys():
            in_t = int(check[i].split(':')[0]) * 60 + int(check[i].split(':')[1])
            total_time[i] += oneday - in_t

    # 차량 번호 오름차순 정렬을 위해 list로 변환
    lst = []
    for i in total_time:
        lst.append([i, total_time[i]])

    # 차량번호 별 오름차순정렬
    lst.sort(key=lambda x: x[0])

    # answer에 요금 넣기
    for car_num in lst:
        temp = total_time[car_num[0]]  # 각 차량의 total time

        # 1.차량이 basic time보다 오래 있었다면
        if temp > basic_t:
            answer.append(basic_f + math.ceil((temp - basic_t) / unit_t) * unit_f)

            # 2.차량이 basic time보다 같거나 적게 있었다면
        else:
            answer.append(basic_f)

    return answer