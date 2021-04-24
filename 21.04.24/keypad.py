'''
엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
입출력 예
numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
'''
def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0), 2:(0,1), 3:(0,2),
             4:(1,0), 5:(1,1), 6:(1,2),
             7:(2,0), 8:(2,1), 9:(2,2),
             '*':(3,0), 0:(3,1), '#':(3,2)}
    l = [1,4,7]
    r = [3,6,9]
    l_hand = '*'
    r_hand = '#'
    for i in numbers:
        if i in l:
            answer += 'L'
            l_hand = i
        elif i in r:
            answer += 'R'
            r_hand = i
        else: # 맨하튼 거리 계산법 .....공부할게 많다 힘내자
            '''
            def manhattan_distance(pt1, pt2):
                distance = 0
                for i in range(len(pt1)):
                    distance += abs(pt1[i] - pt2[i])
                return distance
            '''
            curPos = keypad[i]
            l_last = keypad[l_hand]
            r_last = keypad[r_hand]
            ldist = abs(curPos[0]-l_last[0]) + abs(curPos[1]-l_last[1])
            rdist = abs(curPos[0]-r_last[0]) + abs(curPos[1]-r_last[1])

            if ldist < rdist:
                answer += 'L'
                l_hand = i
            elif ldist > rdist:
                answer += 'R'
                r_hand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    l_hand = i
                else:
                    answer += 'R'
                    r_hand = i

    return answer