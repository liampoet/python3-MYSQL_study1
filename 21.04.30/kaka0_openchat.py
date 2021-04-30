'''
입출력 예
record	result
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
'''
def solution(record):
    answer = []
    name = {}
    case = []
    action = {'Enter' : '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
    for i in record:
        i = i.split(' ')
        act = i[0]
        if act != 'Leave':
            name[i[1]] = i[2]
        if act != 'Change':
            case.append((act, i[1]))
    for act, id in case:
        answer.append(name[id] + action[act])
    return answer