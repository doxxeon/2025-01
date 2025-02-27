# 점프투파이썬 6장 연습문제

'''

Q1. 구구단 x단 프로그램 만들기

gugu 함수를 구현해보세요.
'''

def gugu(x):
    print("구구단", x, "단")
    for i in range(1, 10):
        print(x, "X", i, '=', x*i)

num = int(input("구구단 몇 단을 출력할까요? : "))
gugu(num)


'''
Q2. 3과 5의 배수를 모두 더하기

10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다. 
1,000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
'''

list = []
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        list.append(i)

result = 0
for i in list:
    result += i

print(result)

# 또는

result = 0 
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)

'''
Q3. 게시판 페이징하기

함수 이름은? get_total_page
입력받는 값은? 게시물의 총 개수(m), 한 페이지에 보여 줄 게시물 수(n)
출력하는 값은? 총 페이지 수
'''

def get_total_page(m, n):
    if m % n == 0:
        print("총 페이지 수는", m//n, "입니다.")
    
    return print("총 페이지 수는", (m//n)+1, "입니다.")   

get_total_page(101, 10)


'''
Q4. 간단한 메모장 만들기 (잘 모르겠음 ㅠㅠ)

원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.

python memo.py -a "Life is too short"
'''

import sys

option = sys.argv[1] # 1번 인덱스를 읽어서 option 변수에 저장

if option == '-a':
    memo = sys.argv[2] # 2번 인덱스를 읽어서 memo 변수에 저장
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()

print(memo)


'''
Q5. 탭 문자를 공백 문자 4개로 바꾸기

다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.

python tabto4.py src dst
tabto4.py는 우리가 작성해야 할 파이썬 프로그램 이름, src는 탭을 포함하고 있는 원본 파일 이름, dst는 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 파일 이름이다.

예를 들어 a.txt에 있는 탭을 4개의 공백으로 바꾸어 b.txt에 저장하고 싶다면 다음과 같이 수행해야 한다.

python tabto4.py a.txt b.txt
'''

# tabto4.py
import sys # 터미널 명령어를 읽기 위한 모듈

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

fw = open(dst, 'w')
fw.write(space_content)
fw.close()

'''
Q6. 하위 디렉토리 검색하기 ⭐️ (잘 사용!)
특정 디렉터리부터 시작해서 그 하위(디렉터리 포함)의 모든 파일 중 파이썬 파일(*.py)만 출력해 주는 프로그램을 만들어보자.

필요한 기능은? 파이썬 파일만 찾아서 출력하기
입력받는 값은? 검색을 시작할 디렉터리
출력하는 값은? 파이썬 파일명
'''

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)  # 해당 디렉터리에 있는 파일들의 리스트
        # print(filenames)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)  # 디렉터리와 파일 이름을 이어주는 함수
            if os.path.isdir(full_filename):  # 디렉터리일 경우
                search(full_filename)  # 재귀함수
            else:
                ext = os.path.splitext(full_filename)[-1]  # 파일의 확장자명을 가져오는 함수 ([-1]은 확장자만 추출한다는 뜻)
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        print("권한이 없습니다.")

search("/Users/kimdohyeon/건양대학교병원_바이오헬스/2025-01/jump_to_python/0227")

# 또는

for (path, dir, files) in os.walk("/Users/kimdohyeon/건양대학교병원_바이오헬스/2025-01/jump_to_python/0227"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))