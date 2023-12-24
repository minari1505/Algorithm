#큰 수 만들기, 42883

# number의 앞 자리부터 넣고, 앞자리 수가 그 다음 숫자보다 작으면 지우기

def solution(number, k):
    answer = []
    for i in number:
        #answer에 아무것도 없다면, answer에 i를 추가
        if not answer:
            answer.append(i)
            continue
        
        #k의 숫자가 아직 남아있고, i가 answer[-1]보다 크다면 answer[-1]을 지우고, k - 1
        #answer에 i 넣기
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
                    
        answer.append(i)
        
    answer = answer[:-k] if k > 0 else answer
    
    return ''.join(answer)
