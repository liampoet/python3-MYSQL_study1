'''
출력 형식
튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열. 단, 10~15는 각각 대문자 A~F로 출력한다.

입출력 예제
n	t	m	p	result
2	4	2	1	"0111"
16	16	2	1	"02468ACE11111111"
16	16	2	2	"13579BDF01234567"
'''
def trans(n, num):
    arr = "0123456789ABCDEF"
    ret = ''
    if num == 0:
        return '0'
    while num > 0:
        ret = arr[num % n] + ret
        num = num // n
    return ret

def solution(n, t, m, p):
    answer = ''
    string = ''
    
    for i in range(t*m):
        string += trans(n, i)
        
    for j in range(p-1, t*m, m):
        answer += string[j]

    return answer

#다른사람
big = ["A","B","C","D","E","F"]
def solution(n, t, m, p):
    a="0"
    i=0
    #for i in range(t*m):
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer