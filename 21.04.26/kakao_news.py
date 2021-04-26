'''
입력 형식
입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 
기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
출력 형식
입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로, 
이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

예제 입출력
str1	str2	answer
FRANCE	french	16384
handshake	shake hands	65536
aa1+aa2	AAAA12	43690
E=M*C^2	e=m*c^2	65536

'''
import re
def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    str1 = str1.lower()  #소문자
    str2 = str2.lower()
    for i in range(len(str1)-1):  # 2개씩 뽑기
        if (str1[i] + str1[i+1]).isalpha():
            s1.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if (str2[i] + str2[i+1]).isalpha():
            s2.append(str2[i]+str2[i+1])
    summ = len(s1) + len(s2)  # 합집합
    inte = 0
    for i in s2:
        if i in s1:
            s1.remove(i)
            inte += 1
    if summ == 0: return 65536  
    return int(inte / (summ-inte) * 65536)