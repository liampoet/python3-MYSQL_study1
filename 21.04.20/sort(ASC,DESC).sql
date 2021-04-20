'''
예시
예를 들어, ANIMAL_INS 테이블이 다음과 같다면

ANIMAL_ID	ANIMAL_TYPE	DATETIME	INTAKE_CONDITION	NAME	SEX_UPON_INTAKE
A349996	Cat	2018-01-22 14:32:00	Normal	Sugar	Neutered Male
A350276	Cat	2017-08-13 13:50:00	Normal	Jewel	Spayed Female
A396810	Dog	2016-08-22 16:13:00	Injured	Raven	Spayed Female
A410668	Cat	2015-11-19 13:41:00	Normal	Raven	Spayed Female
이름을 사전 순으로 정렬하면 다음과 같으며, 'Jewel', 'Raven', 'Sugar'
'Raven'이라는 이름을 가진 개와 고양이가 있으므로, 이 중에서는 보호를 나중에 시작한 고양이를 먼저 조회합니다.
따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

ANIMAL_ID	NAME	DATETIME
A350276	Jewel	2017-08-13 13:50:00
A396810	Raven	2016-08-22 16:13:00
A410668	Raven	2015-11-19 13:41:00
A349996	Sugar	2018-01-22 14:32:00
'''
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC