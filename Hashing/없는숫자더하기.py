#86051, 없는숫자더하기

#1. num_lst : 0~9 숫자넣은 리스트 만들기
#2. num_lst 돌면서 numbers에 없다면 answer에 더하기
def solution(numbers):
    answer = 0
    num_lst = [0,1,2,3,4,5,6,7,8,9]
    for i in num_lst:
        if i not in numbers:
            answer += i
    return answer