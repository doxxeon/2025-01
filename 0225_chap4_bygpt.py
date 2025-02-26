'''
Q1. 문자열을 반대로 뒤집는 함수 작성하기

주어진 문자열을 반대로 뒤집는 함수 reverse_string을 작성하세요. 
예를 들어, 입력 문자열이 “Python”이면 출력은 “nohtyP”이어야 합니다.
'''

def reverse_string(str):
    return str[::-1] 
    # 처음부터 -1 간격으로 출력
    # 문법이니 외우고 있기
    # "::" 을 기준으로 왼쪽 이상부터 오른쪽 간격으로 출력

str = 'Python'
reverse_string(str)


'''
소수를 판별하는 함수 작성하기

주어진 숫자가 소수인지 아닌지를 판별하는 함수 is_prime을 작성하세요. 소수는 1과 자기 자신만을 약수로 갖는 1보다 큰 양의 정수입니다. 함수는 소수일 경우 True를 반환하고, 아닐 경우 False를 반환해야 합니다.

'''

def is_prime(num):
    for i in range (num):
        if num%i==0:
            print("False")
        i+=1
    print("True")

num = int(input("숫자 입력: "))
is_prime(num)