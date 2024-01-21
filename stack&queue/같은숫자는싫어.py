#pro, 같은 숫자는 싫어, 12906

def solution(arr):
    cnt = []
    cnt.append(arr[0])
    for i in arr:
        if i == cnt[-1]:
            pass
        else:
            cnt.append(i)
    return cnt