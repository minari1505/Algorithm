import collections
import math


def solution(fees, records):
    answer = []
    total_time = collections.defaultdict(int)  # 차량번호 별 이용시간 저장할 dict
    check = collections.defaultdict(str)  # 차량 in,out 확인할 check
    # 기본시간, 기본요금, 단위시간, 단위요금
    basic_t = int(fees[0])
    basic_f = int(fees[1])
    unit_t = int(fees[2])
    unit_f = int(fees[3])

    # 차량번호 정렬할 리스트
    number_lst = []
    for record in records:
        temp = record.split()
        number_lst.append(int(temp[1]))

    for record in records:
        t, num, io = record.split()  # i,o시간, 차량번호, i or o
        if num not in check.keys():  # check 리스트에 차량번호가 없다면 -> in
            check[num] = t
        else:  # 차량번호가 있다면 out시간-in시간,
            out_t = int(t.split(':')[0]) * 60 + int(t.split(':')[1])
            in_t = int(check[num].split(':')[0]) * 60 + int(check[num].split(':')[1])
            total_time[num] += out_t - in_t
            del check[num]  # out time 계산 끝난 후, check[num] 지우기

    hours = int(23 * 60 + 59)  # 00:00 ~ 23:59까지 분으로 쳤을 때
    # in만 있고 out이 없을 때
    # check dict에 존재한다면
    if check:
        for i in check.keys():
            in_t = int(check[i].split(':')[0]) * 60 + int(check[i].split(':')[1])
            total_time[i] += hours - in_t

    # 차량번호 오름차순 순으로 가격을 계산하기 위해 total_time => lst로 변경
    # 어차피 변경할거 처음부터 2차원리스트로 하는건?
    result = []
    for i in total_time:
        result.append([i, total_time[i]])
    result.sort(key=lambda x: x[0])

    # answer에 요금 넣기
    for i in result:
        temp_num = total_time[i[0]]  # 각 차량의 total_time

        if temp_num > basic_t:
            answer.append(basic_f + math.ceil((temp_num - basic_t) / unit_t) * unit_f)
        else:
            answer.append(basic_f)

    return answer
