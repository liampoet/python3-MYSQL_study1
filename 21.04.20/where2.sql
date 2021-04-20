'''
예시
예를 들어 ANIMAL_INS 테이블이 다음과 같다면

ANIMAL_ID	ANIMAL_TYPE	DATETIME	INTAKE_CONDITION	NAME	SEX_UPON_INTAKE
A365172	Dog	2014-08-26 12:53:00	Normal	Diablo	Neutered Male
A367012	Dog	2015-09-16 09:06:00	Sick	Miller	Neutered Male
A365302	Dog	2017-01-08 16:34:00	Aged	Minnie	Spayed Female
A381217	Dog	2017-07-08 09:41:00	Sick	Cherokee	Neutered Male
이 중 젊은 동물은 Diablo, Miller, Cherokee입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

ANIMAL_ID	NAME
A365172	Diablo
A367012	Miller
A381217	Cherokee
'''
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
WHERE INTAKE_CONDITION != 'Aged'