'''
[입출력 예]
s	result
"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
"{{20,111},{111}}"	[111, 20]
"{{123}}"	[123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]
'''
import re
 
def solution(s):
    answer = []
    s = s.split(',{')
    s.sort(key = len)
    for i in s:
        numbers = re.findall("\d+", i)
        for j in numbers:
            if int(j) not in answer:
                answer.append(int(j))
    return answer