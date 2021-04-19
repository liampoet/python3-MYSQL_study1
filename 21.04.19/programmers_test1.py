'''
1단계 배열 [[]] 더하기(50/50)
'''
def solution(arr1, arr2):
    bowl = []
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr2[i])):
            bowl.append(arr1[i][j] + arr2[i][j])
        answer.append(bowl)
        bowl = []
    return answer