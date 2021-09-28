jumun = "950125-1234567"

print("성별 : " + jumun[7])
print("연 : "+ jumun[0:2]) #0부터 2직전까지 (0,1)
print("월 : "+ jumun[2:4])
print("일 : "+ jumun[4:6])

print("생년월일 : "+ jumun[:6])# 처음부터  6직전의 값까지만
print("뒤 7자리 :"+ jumun [7:])# 지정부터 끝까지 값
print("뒤 7자리(뒤에부터) : "+ jumun[-7:]) # 맨뒤에서 7번째부터 끝까지

