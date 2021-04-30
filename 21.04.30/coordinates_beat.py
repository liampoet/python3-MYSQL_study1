'''
입출력 예
v	result
[[1, 4], [3, 4], [3, 10]]	[1, 10]
[[1, 1], [2, 2], [1, 2]]	[2, 1]
입출력 예 설명
입출력 예 #1
세 점이 [1, 4], [3, 4], [3, 10] 위치에 있을 때, [1, 10]에 점이 위치하면 직사각형이 됩니다.

입출력 예 #2
세 점이 [1, 1], [2, 2], [1, 2] 위치에 있을 때, [2, 1]에 점이 위치하면 직사각형이 됩니다.
'''
#1차 길게 늘림
def solution(v):
    answer = []
    x = []
    y = []
    for i in v:
        for j in range(len(i)):
            if j == 0:
                x.append(i[j])
            else:
                y.append(i[j])
    if x[0] == x[1]:
        answer.append(x[2])
    elif x[1] == x[2]:
        answer.append(x[0])
    elif x[0] == x[2]:
        answer.append(x[1])
    if y[0] == y[1]:
        answer.append(y[2])
    elif y[1] == y[2]:
        answer.append(y[0])
    elif y[0] == y[2]:
        answer.append(y[1])

    return answer

#2차 1차를 간결하게
def solution(v):
    answer = []
    x = []
    y = []
    for i in v:
        if i[0] not in x:
            x.append(i[0])
        else:
            x.remove(i[0])
        if i[1] not in y:
            y.append(i[1])
        else:
            y.remove(i[1])
    answer = x + y
    return answer

#3차 비트사용 - XOR연산자
'''
A xor A = 0
A xor A xor B = B
같은 값 두 개와 다른 값 한 개를 XOR 하면 다른 값 한 개가 나온다는 원리
'''
def solution(v):
    answer = []
    
    answer.append(v[0][0]^v[1][0]^v[2][0])
    answer.append(v[0][1]^v[1][1]^v[2][1])
    
    return answer