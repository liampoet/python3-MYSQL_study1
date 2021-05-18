'''
ㅇㅖ시
당첨 번호	31	10	45	1	6	19	결과
최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등

입출력 예
lottos	win_nums	result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]
'''
def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    n,m = 0,0
    if lottos.count(0) == 6: return[1,6]
    if 0 not in lottos and lottos == win_nums: return[1,1]
    for i in lottos:
        if i == 0:
            n += 1
        for j in win_nums:
            if i == j:
                n += 1
                m += 1
    if n == 0: answer.append(6)
    else: answer.append(7-n)
    if m == 0: answer.append(6)
    else: answer.append(7-m)
    return answer