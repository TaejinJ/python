# 표준 체중을 구하는 프로그램을 작성하시오

# *표준체중 : 각 개인의 키에 적당한 체중 

# (성별에 따른 키공식)
# 남자 : 키(m) x 키(m) x22
# 여자 : 키(m) x 키(m) x21

# 조건 1 : 표준 체중은 별도의 함수내에서 계산
#             *함수명 : std_weight
#             *전달값 : 키(height), 성별(gender)
# 조건 2 : 표준체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준체중은 67.38kg입니다.

# gender = "male" or "female"
# height = int(178)
# std_weight = height * height * 22
# if gender == "male":
#     print("키{0}남자의 표준 체중은 {}kg입니다".format(height,std_weight))
# elif gender == "female":
#      print(("키{0}여자의 표준 체중은 {}kg입니다".format(height,std_weight))

def std_weight(height, gender):
    if gender =="남자":
        return height * height * 22
    else:  # else
        return height * height * 21

height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준체중은 {2}입니다.".format(height,gender,weight))