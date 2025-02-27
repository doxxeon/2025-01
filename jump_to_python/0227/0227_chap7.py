# 점프투파이썬 7장 연습문제

'''
Q1. 문자열 바꾸기 다음과 같은 문자열이 있다.

a:b:c:d
문자열의 split와 join함수를 사용하여 위 문자열을 다음과 같이 고치시오.

a#b#c#d
'''

a = 'a:b:c:d'
new_a = a.split(':')
a = '#'.join(new_a)
print(a)


'''
Q2. 딕셔너리 값 추출하기 다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.

a = {'A':90, 'B':80} a['C']
a딕셔너리에는 'C'라는 key가 없으므로 오류가 발생한다. 'C'에 해당하는 key값이 없을 경우 오류대신 70을 얻을 수 있도록 수정하시오.
'''

a = {'A':90, 'B':80}

if a.get('C') == None:
    a['C'] = 70

print(a['C'])


'''
3. 리스트의 더하기와 extend 함수 다음과 같은 리스트가 있다.

a = [1, 2, 3]
리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.

a = [1, 2, 3] a = a + [4, 5] print(a) >> [1, 2, 3, 4, 5]
리스트 a에 [4, 5]를 extend를 사용하여 더한 결과는 다음과 같다.

a = [1, 2, 3] a.extend([4, 5]) print(a) >> [1, 2, 3, 4, 5]
+ 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.
'''

# 기호를 사용하여 더하면, a 라는 리스트에 새로운 리스트가 더해진 '새로운 리스트'가 생성되는 것이기 때문에 주소값이 변한다.
# extend를 사용하면, a 라는 리스트에 새로운 리스트가 더해지는 것이기 때문에 주소값이 변하지 않는다.


'''
4. 리스트 총합 구하기 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
'''

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
list = []
for i in A:
    if i >= 50:
        list.append(i)

result = 0
for i in list:
    result += i

print(result)


'''
5. 피보나치 함수 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.

0, 1, 1, 2, 3, 5, 8, 13 ...
입력을 정수 n으로 받았을 때, n이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
'''

def fib(n):
    a, b = 0, 1
    while (a <= n):
        print(a)
        a, b = b, a+b

fib(40)

# 또는

input = int(input('숫자 입력: '))

def fib_a(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_a(n-2)+fib_a(n-1)

for i in range(input):
    print(fib_a(i))

'''
Q6. 숫자의 총합 구하기 사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)

65, 45, 2, 3, 45, 8
'''

nums = input("숫자를 입력하세요: ")
nums = nums.split(',')
result = 0

for i in nums:
    result += int(i)

print(result)

# 또는

val = input('숫자를 입력하세요: ')
a = map(int, val.split(','))  
# split으로 나눈 숫자들을 int 형태로 바꾸어라
# <class 'map'>

result = 0
for i in a:
    result += i
print(result)

'''
Q7. 한 줄 구구단 사용자로부터 2~9까지의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오. 실행 예)

구구단을 출력할 숫자를 입력하세요(2~9): 2 2 4 6 8 10 12 14 16 18
'''

nums = int(input("구구단 숫자 입력: "))
for i in range(1, 10):
    print(i*nums, end=' ')


'''
8. 역순 저장

다음과 같은 내용의 파일 abc.txt가 있다.

AAA

BBB

CCC

DDD

EEE

이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

EEE

DDD

CCC

BBB

AAA


'''

f1 = open('abc.txt', 'r', encoding='utf-8')
lines = f1.readlines()
lines.reverse()

f1.close()

f2 = open('abc.txt', 'w', encoding='utf-8')
for i in lines:
    f2.write(i.strip())
    f2.write('\n')

f2.close()


'''
Q9. 평균값 구하기

오른쪽 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.

70

60

55

75

95

90

80

80

85

100
'''

f = open('sample.txt', 'r', encoding='utf-8') 
lines = f.readlines()
f.close()

total = 0

for i in lines:
    score = int(i)
    total += score

average = total / len(lines)

f = open('result.txt', 'w', encoding='utf-8')
f.write(str(average))
f.close()


'''
Q 사칙연산 계산기

다음과 같이 동작하는 클래스 Calculator를 작성하시오.

>>> cal1 = Calculator([1,2,3,4,5])
>>> cal1.sum() # 합계
15
>>> cal1.avg() # 평균
3.0
>>> cal2 = Calculator([6,7,8,9,10])
>>> cal2.sum() # 합계
40
>>> cal2.avg() # 평균
8.0
'''

class Calculator():
    def __init__ (self, list):
        self.list = list

    def sum(self):
        result = 0
        for i in self.list:
            result += i
        return result
    
    def avg(self):
        result = self.sum()/len(self.list)
        return result

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())


'''
11. 모듈 사용 방법

C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서 차이썬 셸을 열어 이 모듈을 import 해서 사용할 수 있는 방법을 모두 기술하시오.
'''