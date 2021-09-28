# while문은  적혀있는 조건에 만족할때까지 계속 문장을 반복.
customer = "토르"
index = 5
# while(조건):
while index >= 1:
    print("{0}, 커피가 준비되었습니다.{1}번남았어요".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기했습니다.")

# customer = "토르"
# index=1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출{1}회".format(customer,index))
#     index += 1

