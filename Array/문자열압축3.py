#문자열 압축,Lv2
#100점
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
                if cnt != 1:
                    string += str(cnt)
                    string += r_s
                    r_s = ''
                    cnt = 1
                else:
                    string += r_s
                    r_s = ''
                    cnt = 1
        # string = string.replace('1','') #사용 시 반복횟수가 17,18 -> 7,8
        repeat[string] = len(string)
        string = ''

    #!문자열의 길이가 1이라면 첫번째 for문에 들어가지 못함!
    if len(s) == 1:
        repeat[s] = 1
    return min(repeat.values())