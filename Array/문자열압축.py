#문자열 압축,Lv2
#70점

import collections
def solution(s):
    answer = ''
    repeat = collections.defaultdict(int) #문자열 + 문자열의 길이 저장할 dict
    r_s = '' #반복할 문자열
    string = '' #문자열 저장
    for i in range(1,(len(s)//2)+1): #1~len(s//2)까지,문자열을 몇 개씩 자를건지
        cnt = 1 #반복횟수 저장할 변수
        for j in range(len(s)):
            r_s = s[i*j:i*(j+1)]
            if s[i*(j+1):i*(j+2)] == r_s: #다음 반복횟수의 문자열이 이전 문자열과 같다면 cnt +1
                cnt += 1
            else: #다음 반복횟수의 문자열이 이전 문자열과 다르다면 string에 cnt,r_s 저장후 cnt,r_s 리셋
                string += str(cnt)
                string += r_s
                r_s = ''
                cnt = 1
        string = string.replace('1','')
        repeat[string] = len(string)
        string = ''
    return min(repeat.values())

'''
def solution(s):
    result = len(s)
    for i in range(1, len(s)//2+1):
        previous = s[:i]

        count = 1
        string = ''
        for j in range(i, len(s), i):
            if previous == s[j:j+i]:
                count += 1
            else:
                string += str(count)+previous if count != 1 else previous
                previous = s[j:j+i]
                count = 1

        string += str(count)+s[j:] if count != 1 else s[j:]
        # string = string.replace('1', '')  # 10, 11, 12 ... 문제 발생
        result = min(result, len(string))
    return result  
'''