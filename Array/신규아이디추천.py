#신규 아이디 추천, Lv1

# 아이디 생성
# 1. 길이 3~15
# 2. 알파벳 소문자, 숫자, -,_,.
# 3. .는 처음과 끝 불가, 연속사용 불가
def solution(new_id):
    answer = ''

    pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for _ in new_id:
        if _ in pos:
            answer += _

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if len(answer) >= 1:
        if answer[0] == '.':
            answer = answer[1:]
        elif answer[-1] == '.':
            answer = answer[:-1]

    # 5단계
    if len(answer) < 1:
        answer += 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[:-1]

        # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
    print(answer)

    return answer