#자연수 뒤집어 배열로 만들기, 12932
def solution(n):
    n = list(str(n))
    return list(map(int,n[-1::-1]))