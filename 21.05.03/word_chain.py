'''
입출력 예
n	words	result
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", 
"establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]
입출력 예 설명
입출력 예 #1
3명의 사람이 끝말잇기에 참여하고 있습니다.

1번 사람 : tank, wheel, mother
2번 사람 : kick, land, robot
3번 사람 : know, dream, tank
와 같은 순서로 말을 하게 되며, 3번 사람이 자신의 세 번째 차례에 말한 tank라는 단어가 1번 사람이 자신의 첫 번째 차례에 말한 tank와 같으므로 
3번 사람이 자신의 세 번째 차례로 말을 할 때 처음 탈락자가 나오게 됩니다.

입출력 예 #2
5명의 사람이 끝말잇기에 참여하고 있습니다.

1번 사람 : hello, recognize, gather
2번 사람 : observe, encourage, refer
3번 사람 : effect, ensure, reference
4번 사람 : take, establish, estimate
5번 사람 : either, hang, executive
와 같은 순서로 말을 하게 되며, 이 경우는 주어진 단어로만으로는 탈락자가 발생하지 않습니다. 따라서 [0, 0]을 return하면 됩니다.

입출력 예 #3
2명의 사람이 끝말잇기에 참여하고 있습니다.

1번 사람 : hello, even, now, draw
2번 사람 : one, never, world
와 같은 순서로 말을 하게 되며, 1번 사람이 자신의 세 번째 차례에 'r'로 시작하는 단어 대신, 
n으로 시작하는 now를 말했기 때문에 이때 처음 탈락자가 나오게 됩니다.
'''
#1차시도 - but너무 길었음
def solution(n, words):
    answer = []
    arr = []
    count = 1
    j = 0
    for i in words:
        j += 1
        if j < len(words):
            v = words[j]
        if i not in arr:
            arr.append(i)
            if i[-1] != v[0]:
                if count % n != 0:
                    count += 1
                else: count = 1
                return [(j%n)+1, (j//n)+1]
            if count % n != 0:
                count += 1
            else: count = 1
        elif i in arr:
            return [(j%n)+1, (j//n)+1]
    return [0,0]

#2차시도
def solution(n, words):
    answer = [0, 0]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[0:i]: 
            answer[0] = ( i % n ) + 1 
            answer[1] = ( i // n ) + 1 
            break 
    return answer
