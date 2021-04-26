'''
출력 형식
원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

입출력 예제
매개변수	값
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]
매개변수	값
n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
'''
def solution(n, arr1, arr2):
    answer = []
    bowl = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b')
        arr2[i] = format(arr2[i], 'b')
        
        a = (str(int(arr1[i]) + int(arr2[i])))
        k = ''
        if len(a) < n:
            a = a.zfill(n)
        for j in a:
            if j == '0':
                k = k + ' '
            else:
                k = k + '#'
        answer.append(k)
    return answer