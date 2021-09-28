# score_file = open("score.txt","w", encoding="utf8") #utf8을 정의해주지않으면 한글로 제대로 안된다?
# print("수학 : 0", file=score_file) #w는 쓰기용 파일 ->덮어쓰기
# print("영어 : 50", file=score_file)
# score_file.close() # 열은 파일은 닫아줘야한다

# score_file = open("score.txt","a",encoding="utf8") #->이어서 쓰고싶으면 append의 a사용
# score_file.write("과학 : 80")  # print할땐 자동줄바꿈가능, write를통할땐 줄바꿈따로없다.
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8") # 모든내용 불러오기
# print(score_file.read())
# score_file.close() 

# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.readline(),end="") # 줄별로 읽기, 한줄읽고 커서는 다음줄로이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

score_file = open("score.txt","r", encoding="utf8")
lines = score_file.readlines() # 모든라인을갖고와서 list형태로저장
for line in lines:
    print(line,end="")
score_file.close()