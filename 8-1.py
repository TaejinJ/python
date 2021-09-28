# import sys
# print("파이썬","자바", file= sys.stdout) # 표준출력
# print("파이썬","자바", file= sys.stderr) #표준에러

# scores = {"수학" :0, "영어":50, "코딩" : 100}
# for subject, score in scores.items():
#     # print(subject,score)
# #     print(subject.ljust(8),str(score).rjust(4),sep=":")


# #은행 대기 순번표
# # 001,002, 003, ...
# # for num in range(1,21):
# #     print("대기번호 : "+str(num).zfill(3) )


# # answer = input("아무값이나 입력하세요 : ")
# answer = 10
# print(type(answer))
# # print("입력하신 값은" +answer + "입니다.")


# deals = {"ranger":5000, "berzerker" :4050 , "preist" : 2500}
# for job, deal in deals.items():
#     # print(job,deal)
#     print(job.ljust(10),str(deal).rjust(8),sep= "ㅡ")
    

environment = input("환경은 어떻습니까?")
if environment == "오존층 파괴" or "남극의 유빙현상":
    print("굉장히 위험합니다.")

else:
    print("문제없습니다. 환경이 나아지고있습니다.") 

    

