'''
입출력 예
s	answer
"pPoooyY"	true
"Pyy"	false
입출력 예 설명
입출력 예 #1
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

입출력 예 #2
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.
'''
def solution(s):
    answer = True
    s = s.lower()
    if(s.count('p') == s.count('y') or s.count('p')==s.count('y') ==0):return True
    else:return False