# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

#\"\' : 문장내에서 따옴표
#저는 "나도코딩"입니다.

# print("저는 '나도코딩'입니다")
# print('저는 "나도코딩"입니다')
# print("저는 \"나도코딩\"입니다")

# \\ : 문장 내에서 \
# print("C:\\Users\\조태진\\Desktop\\python work space>")

#\r : 커서를 맨앞으로 이동 
# print("Red Apple\rPine")

#\b : 백스페이스 (한글자 삭제)
# print("Redd\bApple")

# #\t : 탭
# print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예)http://naver.com
# 규칙1 : http:// 부분은 제외 > naver.com
# 규칙2 : 처음만나는점 (.) 이후 부분은 제외 > naver
# 규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1
print(my_str)
my_str = my_str[0:my_str.index(".")]#규칙2 my_str[0:5] -> 0~5 직전까지,(0,1,2,3,4)
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))


  