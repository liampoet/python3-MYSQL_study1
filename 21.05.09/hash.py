'''
예제 #1
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 
blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.
1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
예제 #2
face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.
1. crow_mask
2. blue_sunglasses
3. smoky_makeup
'''
def solution(clothes):
    arr = {}
    for i in clothes:
        if i[1] in arr: arr[i[1]] += 1
        else: arr[i[1]] = 1
                
    answer = 1
    for i in arr.values():
        answer *= (i+1)
    return answer - 1 # none(-1)