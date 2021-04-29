'''
입출력 예
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]
입출력 예 설명
입출력 예 #1
1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.

1 번 스테이지 실패율 : 1/8
2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.

2 번 스테이지 실패율 : 3/7
마찬가지로 나머지 스테이지의 실패율은 다음과 같다.

3 번 스테이지 실패율 : 2/4
4번 스테이지 실패율 : 1/2
5번 스테이지 실패율 : 0/1
각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.

[3,4,2,1,5]
입출력 예 #2

모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.

[4,1,2,3]
'''

'''
1차시도
채점 결과
정확성: 51.9
합계: 51.9 / 100.0
#이유 : 코드는 정답이나 런타임이 너무 오래 걸려서 Fail
'''
def solution(N, stages):
    answer = []
    fail_rate = []
    for i in range(1,N+1):
        if i in stages:
            fail_rate.append(stages.count(i) / len(stages))
            while i in stages:
                stages.remove(i)
        else:
            fail_rate.append(0)
            
    a = sorted(fail_rate, reverse = True)
    for j in range(len(a)):
        answer.append(fail_rate.index(a[j])+1)
        fail_rate[fail_rate.index(a[j])] = 2
    return answer

'''
2차시도 : 성공
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)