#점프투파이썬 2장 연습문제

'''
Q1. 홍길동의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수는?

국어 - 80, 영어 -75, 수학 - 55
'''

hong = {'국어': 80,
        '영어': 75,
        '수학': 55}
a, b, c = hong.values()
score = a+b+c
print(float(score/3))

#또는

kor = 80
eng = 75
math = 55
sum = kor + eng + math
print(sum/3)


'''
Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법?
'''

d = 13
if (d%2 == 0):
    print("짝수")
else:
    print("홀수")


'''
Q3. 홍길동의 주민등록번호는 881120-1068234이다. 홍길동의 주민등록번호를 연원일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
'''

hongs = [8,8,1,1,2,0,1,0,6,8,2,3,4]
birth = hongs.copy()
del birth [6:]
others = hongs.copy()
del others [:6]
print("연월일: ",birth,", 뒷자리: ",others)

#또는

num = '881120-1068234'
print(num[:6])
print(num[7:])

print(num.split('-'))


'''
Q4. 주민등록번호 뒷자리(Q3의 주민등록번호 사용)의 맨 첫 번째 숫자는 성별을 나타낸다. 성별을 나타내는 숫자를 출력해보자.
'''

if others[0] == 1 or 3:
    print("남자")
else:
    print("여자")


'''
Q5. 다음과 같은 문자열 a:b:c:d:가 있다. 문자열의 replace함수를 이용하여 a#b#c#d로 바꿔보자.
'''

str1 = 'a:b:c:d:'
print(str1.replace(':', '#'))


'''
Q6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.(Hint : sort() 함수와 reverse() 함수)
'''

list1 = [1, 3, 5, 4, 2]
list1.sort()
list1.reverse()
print(list1)


'''
Q7. [‘Life’, ‘is’, ‘too’, ‘short’] 리스트를 Life is too short 문자열로 만들어 출력해 보자.(Hint : join()함수)
'''

# join 함수는 list를 문자열로 바꿀 때 사용한다. (TXT 파일)

a = ['life', 'is', 'too', 'short']
print(' '.join(a))


'''
Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
'''

tuple1 = (1,2,3)
list_new = list(tuple1)
list_new.append(4)
tuple1=tuple(list_new)
print(tuple1)


'''
Q9. 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

1. a[‘name’] = ‘python’
>> 새로운 key: 'name', value: 'python'

2. a[(‘a’,)] = ‘python’
>> 새로운 key: 'a',, value: 'python'

3. a[[1]] = ‘python’

4. a[250] = ‘python’
>> 새로운 key: 250, value: 'python'
'''

# 3번이 오류이다.
# 딕셔너리의 key로 list가 올 수 없는 이유는 list가 가변 데이터로 이루어져있기 때문이다.


'''
Q10. 딕셔너리 a에서 ‘B’에 해당되는 값을 추출해 보자.

>>> a = {'A':90, 'B':80, 'C':70}
'''

a={'A':90, 'B':80, 'C':70}
print(a['B'])


'''
Q11. a 리스트에서 중복 숫자를 제거해 보자.

>>> a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
'''

a = [1,1,1,2,2,3,3,3,4,4,5]
new_a=set(a)
a=list(new_a)
print(a)


'''
Q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

>>> a = b = [1, 2, 3]   
>>> a[1] = 4   
>>> print(b)

 [1, 4, 3]

'''

 #이유: a, b는 동일한 리스트인 객체를 가리키고 있다. (동일한 주소값)
 #만약 a와 b를 각각 독립적으로 가르키는 변수로 만들고 싶다면, deepcopy()를 사용해야 한다.
 #(이때, copy()는 사용하면 안된다. 왜냐하면 copy는 겉부분만 새로운 복사본을 만들고 내부 요소는 원본과 동일해지기 때문이다.)