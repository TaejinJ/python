# 당신의 회사에서는 매주 1회 작성해야하는 보고서가있습니다.
# 보고서는 항상 아래와같은 형태로 출력되어야합니다.


# -x주차 주간보고-
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차. txt','2주차 .txt',...와 같이만듭니다.


# report_file = open("report.txt","w",encoding="utf8")
# week = (range(1,51))
# print("{}주차 주간보고".format(week))
# print("이름 : ")
# print("업무 요약 : ")
# report_file.close()

# for i in range(1,51):
#     with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
#         report_file.write("-{0}주차 주간보고-".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 ")
#         report_file.write("\n업무 요약 :")
                                   #1~50주차까지 나옴
