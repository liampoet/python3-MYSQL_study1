'''
예시
예를 들어 ANIMAL_INS 테이블이 다음과 같다면

ANIMAL_ID	ANIMAL_TYPE	DATETIME	INTAKE_CONDITION	NAME	SEX_UPON_INTAKE
A399552	Dog	2013-10-14 15:38:00	Normal	Jack	Neutered Male
A379998	Dog	2013-10-23 11:42:00	Normal	Disciple	Intact Male
A370852	Dog	2013-11-03 15:04:00	Normal	Katie	Spayed Female
A403564	Dog	2013-11-18 17:03:00	Normal	Anna	Spayed Female
이 중 가장 보호소에 먼저 들어온 동물은 Jack입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

NAME
Jack
'''
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1