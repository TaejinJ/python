from random import *

# print(random()) # 0.0~ 1.0미만의 임의의 값 생성
# print(random()*10) # 0.0~10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0~ 10 미만의 임의의 값 생성
# print(int(random() * 10) +1) #1~10 미만의 임의의 값 생성
# print(int(random() * 10) +1) #1~10 미만의 임의의 값 생성
# print(int(random() * 10) +1) #1~10 미만의 임의의 값 생성
# print(int(random() * 10) +1) #1~10 미만의 임의의 값 생성
# print(int(random() * 10) +1) #1~10 미만의 임의의 값 생성
# print(int(random() * 10) +1) #1~10 미만의 임의의 값 생성

# print(int(random()*45) +1) # 1~45미만의 임의의 값 생성
# print(int(random()*45) +1) # 1~45미만의 임의의 값 생성
# print(int(random()*45) +1) # 1~45미만의 임의의 값 생성
# print(int(random()*45) +1) # 1~45미만의 임의의 값 생성
# print(int(random()*45) +1) # 1~45미만의 임의의 값 생성
# print(int(random()*45) +1) # 1~45미만의 임의의 값 생성
# print(int(random()*45) +1) # 1~45미만의 임의의 값 생성

# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46미만의 임의의 값 생성

# print(randint(1,45)) #1~45이하의 임의의 값 생성
# print(randint(1,45)) #1~45이하의 임의의 값 생성
# print(randint(1,45)) #1~45이하의 임의의 값 생성
# print(randint(1,45)) #1~45이하의 임의의 값 생성
# print(randint(1,45)) #1~45이하의 임의의 값 생성
# print(randint(1,45)) #1~45이하의 임의의 값 생성

# quiz
# 조건 1 : 랜덤으로 날짜뽑아야함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import *

date =randint(4,28)
print("오프라인 스터디 모임 날짜는 매월"+ str(date) + "일로 선정되었습니다.")