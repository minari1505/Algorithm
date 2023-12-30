def solution(people, limit):
    count = 0
    #몸무게 적은사람 순으로 오름차순 정렬
    people.sort()
    
    #몸무게 제일 적은 사람의 인덱스 = 0, 몸무게 제일 많은 사람의 인덱스 = len(people)-1
    first, last = 0, len(people)-1 
    
    #사람들을 모두 데려올 때 까지.
    while first <= last:
        #몸무게 적은사람 + 많은 사람이 한 번에 들어가면
        if people[first] + people[last] <= limit:
            first += 1 #가장 적은 사람 한 명 더
            
        last -= 1
        count += 1
    return count
