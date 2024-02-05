#qrcode, 181903

# 인덱스를 q로 나누었을 때 나머지가 r 인 문자열만 이어붙이기
# 1. code문자열의 각 인덱스 저장
# 2. 첫번째 시작 문자열을 저장하고, 그 문자열의 인덱스 + q*n 번째 문자열 저장
# => 시작인덱스 = r, 다음 인덱스 = r+q*n(n>=1)

# #1,2,7,10,12,15,18 실패
#반례 : 3,1, "qjnwezgrpirldywtl" -> "jerryl"이어야하는데, 'jerry'나옴
# def solution(q, r, code):
#     answer = ''
#     n = 0
#
#     for i in range(len(code) // q):
#         answer += code[r + q * n]
#         n += 1
#
#     return answer
#

# #1,6,18 실패
#반례 : 6,0, "repeat" -> "r"이어야하는데 "repeat"나옴
# def solution(q, r, code):
#     answer = ''
#
#     return code[r::q]
#

def solution(q, r, code):
    answer = ''
    for idx, val in enumerate(code):
        if idx % q == r:
            answer += val
        else:
            pass
    return answer