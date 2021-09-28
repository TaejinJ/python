# if 조건 == : 
#     실행 명령문

# weather = input("오늘 날씨는 어때요? ") #input은 출력하고 뒤에 입력값을 넣으면 답이나온다.

# if weather =="비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
    
# else:                              # 위두가지가 아니면 출력함
#     print("준비물 필요없어요.")

temp = int(input("기온은 어때요?"))  # 기온은 숫자로 받기때문에 int로감싸준다.
if 30 <= temp :
    print("너무더워요 나가지마세요.")
elif 10 <= temp and temp <= 30:
        print("괜찮아요.")
elif 0<= temp and temp <10:
    print("외투를 챙기세요.")
else:
    print("너무추워요 나가지마세요.")


    
