'''
1단계 3진법 더하기
3진법을 너무 오래동안 안써서 까먹음 ㅜㅠㅠㅠㅠㅠㅠㅠ
결국 3진법 공부하고 타이밍 맞게 가까스로 코드 구성 성공(50/50)
'''
def solution(n):
    x = ''
    answer = 0
    while True:
        x += str(n%3)
        n = n//3
        if n == 0:
            break

    for i in range(len(x)):
        answer += int(x[-(i+1)])*int(3**i)
    return answer