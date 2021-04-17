# -*- coding: utf-8 -*- 

''' 1번 문제 - 구구단 2단 만들기
def GuGu(dan):
    result = []
    i = 1
    while i < 10:
        result.append(dan * i)
        i += 1
    return result

x = input() 

print(GuGu(x))
'''

''' 2번 문제 - 1 ~ 1000 사이에 3과 5의 배수의 총 합
n = 0
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
    
print(result)
'''

''' 3번 문제 - 게시판 페이징
n = 10

def getTotalPage(m):
    x = 1
    if m <= n:
        print('총 페이지의 수는 1 입니다.')
    elif m > n:
        while m > n:
            m = m - n
            x += 1 
    print('총 페이지의 수는 %d 입니다'% x)


print('게시물의 갯수를 입력하시오')
m = int(input())

getTotalPage(m)
'''

'''4번 문제 - 1 ~ 10000 8 개수 새기
print str(range(1,10001)).count('8')
'''

'''5번 문제 - n개의 정수를 가진 배열이 있다. 이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.

정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.

n = [-1, 1, 3, -2, 2]
m, z = [], []
def s(n):
    for i in n:
        if i < 0:
            m.append(i)
        elif i >= 0:
            z.append(i)

    result = m + z

    return result

print(s(n))
'''

''' 6번 문제 - 자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다. 예를 들면, 6과 28은 완전수이다. 
6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수
입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드
N = int(input())
Total = []
for i in range(1, N+1):
    x = 0
    for j in range(1,i):
        if i % j == 0:
            x += j
            
    if i == x:
        Total.append(i)

print(Total)
'''

''' 7번 문제 - 1~1000에서 각 숫자의 개수 구하기
for x in range(0,10):
    print '%d = %s' % (x, str(range(1,1001)).count(str(x)))
'''

''' 8번 문제
a = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(',')
for x in a[0:] : print x.rstrip('이재영')
'''

''' 9번 문제 - 10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
print(sum(eval('*'.join(str(x))) for x in range(10, 1001)))
'''

''' 10번 문제 - text를 불러와서 가장 많은 단어 내림순으로 찾기
f = open('/Users/imgwangmin/work/study.py/study1.txt').read()
word_list = f.replace(',', ' ').replace('.', ' ').split() 
word_list_no_duplicate = list(set(word_list))  # 중복 삭제
w_count = []
for word in word_list_no_duplicate:
    w_count.append((word_list.count(word),word))
n=0
for result in sorted(w_count, reverse=True):
    n+=1
    print(result[1], ':', result[0])
    if n==10:
        break
'''

''' 11번 문제 - 2진수로 변경
a=233
v=[]
def c(a):
    while 1<=a:
        z = a%2
        v.append(z)
        a = a/2

    return v

print(c(a))
'''

'''12번 문제 - 모스부호 번역하기
morse = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'.split(' ')
dic={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z','':' '}
v = []
def code(morse):
    for x in morse:
        v.append(dic[x])
    return v

print(code(morse))
'''

'''
a='a1b2cde3~g45hi6'
def math(a):
    l = list(a)
    for i in range(1, len(l), 2):
        if l[i].isdigit():
            l[i] = '*'
    return l

print(math(a))
'''

a = input("0~9 사이의 숫자로 이루어진 문자열 입력 : ")
print('true' if len(a) == len(set(a)) == 10  else 'false')