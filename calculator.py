#calculator 만들기

# 더하기 1 : 배한재
# 빼기 2 : 소명
# 나누기 3 : 주영
# 곱하기 4 : 요한
# %(//) 5 : 수민
# 제곱 6 : 규경
# 제곱근 7 : 규찬
# sin 8 : 주환
# cos 9 : 다희 
# tan 10 : 예원
# 파이값 출력 11 : 하람
# 자연 상수 값 출력 12 : 하은

import math

m = int(input("모드를 입력하세요 : "))

if m == 1:
    first = int(input("첫번째 수를 입력하세요 : "))
    second = int(input("두번쨰 수를 입력하세요 : "))

    # muliplication: 요한
    
    print("결과값 :", first + second)

if m == 2;
    first = int(input("첫번째 수를 입력하세요 : "))

    second = int(input("두번쨰 수를 입력하세요 : "))
    
    print("결과값 :", first - second)
    
if m == 3:
    first = int(input("첫번째 수를 입력하세요 : "))

    second = int(input("두번쨰 수를 입력하세요 : "))

    print("결과값 :", first / second)

if m == 4:
    first = int(input("첫번째 수를 입력하세요 : "))
    second = int(input("두번쨰 수를 입력하세요 : "))

    # muliplication: 요한
    mul = first * second

    print("결과값 :", mul)
    
    
if m == 5:
    first = int(input("첫번째 수를 입력하세요 : "))

    second = int(input("두번째 수를 입력하세요 : "))

    print("결과값 :", first % second)
    
if m == 7:
    first = int(input("첫번째 수를 입력하세요 : "))

    second = int(input("두번째 수를 입력하세요 : "))

    print("결과값 :", first * second)
    
if m == 8;
    frist = int(input("첫번째 수를 입력하세요 : "))
    
    print("결과값 :", math.sin(first))

if m == 9;
    first = int(input("첫번째 수를 입력하세요: "))

    print("결과값:", math.cos(first))
    

if m == 10:
    tan = math.tan(first)
    tan2 = math.tan(second)

    print("tan 결과값 :", tan + tan2)  
   
if m == 11:
    print(math.pi)

if m == 12:
    print(math.e)
    
