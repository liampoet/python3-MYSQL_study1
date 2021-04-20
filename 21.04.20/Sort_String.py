'''
입출력 예
strings	n	return
["sun", "bed", "car"]	1	["car", "bed", "sun"]
["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]
입출력 예 설명
입출력 예 1
"sun", "bed", "car"의 1번째 인덱스 값은 각각 "u", "e", "a" 입니다. 
이를 기준으로 strings를 정렬하면 ["car", "bed", "sun"] 입니다.

입출력 예 2
"abce"와 "abcd", "cdx"의 2번째 인덱스 값은 "c", "c", "x"입니다. 
따라서 정렬 후에는 "cdx"가 가장 뒤에 위치합니다. "abce"와 "abcd"는 사전순으로 정렬하면 "abcd"가 우선하므로, 
답은 ["abcd", "abce", "cdx"] 입니다.
'''
def solution(strings, n):
    answer = []
    n_arr = []
    strings.sort()
    for i in strings:
        n_arr.append(i[n])
    n_arr.sort()

    for j in n_arr:
        for k in strings:
            if k not in answer:
                if j == k[n]:
                    answer.append(k)
    return answer