#문자열 겹쳐쓰기, 181943

#문자열은 immutable type이라 바꿀 수 없으므로, 리스트로 변환 후 바꿔주거나 이어붙이기..
#1. 리스트로 변환 후 변경
def solution(my_string, overwrite_string, s):
    answer = ''
    leng = len(overwrite_string)
    my_string = list(my_string)
    overwrite_string = list(overwrite_string)
    for i in range(s,s+leng):
        my_string[i] = overwrite_string[i-s]
    answer = "".join(my_string)
    return answer

#2. 문자열 합치기
def solution(my_string, overwrite_string, s):
    leng = len(overwrite_string)
    return my_string[:s] + overwrite_string + my_string[s+leng:]