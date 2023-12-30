#시각
def hours(n):
    count = 0
    #시/분/초
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                #매 시각 안에 3이 포함되어있으면 카운트 +1
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    print(count)

hours(5)
