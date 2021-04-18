'''
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

입출력 예
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]
'''
def solution(arr):
    answer=[]    #정답을 저장할 빈공간의 list 생성
    for i in range(len(arr)): #i를 번지수로 돌릴것이며 범위는 s의 갯수만큼
        if i == 0:          #초기값은 무조건 0이기 때문에 중복될수가 없음
            answer.append(arr[i])  #0은 바로 추가시켜줍니다
        elif arr[i] != arr[i-1]:#현재 주소와 그전의 주소가 같지 않을경우
            answer.append(arr[i])  #지금 값을 추가해줍니다
    return answer