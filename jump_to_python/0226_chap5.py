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
        super().add(val)
        if self.value > 100:
             self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)