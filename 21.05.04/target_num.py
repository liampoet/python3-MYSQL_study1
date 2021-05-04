'''
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
입출력 예
numbers	target	return
[1, 1, 1, 1, 1]	3	5
'''
def solution(numbers, target):
    t = [0]
    for num in numbers:
        sub_t = []
        for t_num in t:
            sub_t.append(t_num + num)
            sub_t.append(t_num - num)
        t = sub_t
    return t.count(target)