# 점프투파이썬 5장 연습문제

'''
Q1. 다음은 Calculator 클래스이다.

class Calculator:
  def __init__(self):
    self.value = 0

  def add(self, val):
    self.value += val
위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해보자.
'''

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -=val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


'''
Q2. 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어보자

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
단, 반드시 다음과 같은 Calculator클래스를 상속해서 만들어야한다.

class Calculator:
  def __init__(self):
    self.value = 0

  def add(self,val):
    self.value += val
'''

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
             self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

'''
Q3. 다음 결과를 예측해보자

#1번

all([1,2,abs(-3)-3])

#2번

chr(ord('a'))=='a'
'''

# 1번 : False
# 2번 : True


'''
Q4. filter와 lambda를 사용해서 리스트 [1,-2,3,-5,8,-3]에서 음수를 제거해보자.
'''

print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))
# filter(f, iterable)은 iterable에서 f함수를 통과한 요소만을 구성하는 iterator를 반환한다.


'''
Q5. 234라는 10진수의 16진수는 다음과 같이 구할 수 있다. 이번에는 반대로 16진수의 문자열 0xea를 10진수로 변경해보자.

>>> hex(234) ‘0xea’
'''

print(int('0xea', 16))


'''
Q6. map과 lambda를 사용해서 [1,2,3,4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3,6,9,12]를 만들어보자.
'''
print(list(map(lambda x: x*3, [1,2,3,4])))


'''
Q7. 다음 리스트의 최댓값과 최솟값의 합을 구해보자.

[-8, 2, 7, 5, -3, 5, 0, 1]
'''

max = max([-8, 2, 7, 5, -3, 5, 0, 1])
min = min([-8, 2, 7, 5, -3, 5, 0, 1])
result = max + min
print(result)

'''
Q8. 17/3의 결과는 다음과 같다. 소숫점 4자리까지만 반올림해서 표시해보자.
'''

print(round(17/3, 4))


'''
Q9. 다음과 같이 실행할 때 입력값을 모두 더해서 출력하는 스크립트(C:\doit\myargv.py)를 작성해보자.

>>> C:\cd doit
>>> C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
55
'''

# myargv.py
import sys

numbers = sys.argv[1:]

result = 0
for i in numbers:
    result += int(i)  

print(result)



'''
Q10. os모듈을 사용해서 다음과 같이 동작하도록 코드를 작성해라.

C:\doit 디렉터리로 이동한다.
dir 명령을 실행하고 그 결과를 변수에 담는다.
dir 명령의 결과를 출력한다.
'''

import os

os.chdir("c:\\doit")
result = os.popen("dir")
print(result.read())
result.close()



'''
Q11. glob모듈을 사용해서 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 만들어보자.
'''

import glob

print(glob.glob("c:\\doit\\*.py")) # glob.glob()은 해당 디렉터리에 있는 파일들을 리스트로 만들어서 반환한다.


'''
Q12. time모듈을 사용해서 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.
2018/04/03 17:20:32
'''

import time

print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))

'''
Q13. random 모듈을 이용해서 로또번호(1~45사이의 숫자 6개)를 생성해보자. (중복 숫자 안 됨)
'''

import random

'''
lotto = random.sample(range(1, 46),6)
'''

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)
