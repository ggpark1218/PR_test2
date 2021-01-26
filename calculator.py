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


m = int(input("모드를 입력하세요 : "))

if m == 1:
    first = int(input("첫번째 수를 입력하세요 : "))

    second = int(input("두번쨰 수를 입력하세요 : "))

    print("결과값 :", first + second)

if m == 5:
    first = int(input("첫번째 수를 입력하세요 : "))

    second = int(input("두번쨰 수를 입력하세요 : "))

    print("결과값 :", first % second)
