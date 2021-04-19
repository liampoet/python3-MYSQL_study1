'''
입출력 예
a	b	result
[1,2,3,4]	[-3,-1,0,2]	3
[-1,0,1]	[1,0,-1]	-2
입출력 예 설명
입출력 예 #1

a와 b의 내적은 1*(-3) + 2*(-1) + 3*0 + 4*2 = 3 입니다.
입출력 예 #2

a와 b의 내적은 (-1)*1 + 0*0 + 1*(-1) = -2 입니다.
'''
def solution(a, b):
    array = []
    for i in range(len(a)):
        array.append(a[i]*b[i])

    answer = sum(array)
    return answer