#list of python modules
#glob : 경로내의 폴더 /파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py인 모든 파일

#os : 운영체제에서 제공하는 기본기능
# import os
# print(os.getcwd()) #현재 디렉토리를 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder,"폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간관련 외장 함수
# import time
# print(time.localtime())
# print(time.strftime("%y-%m-%d %H: %M: %S"))

import datetime
# print("오늘 날짜는 ",datetime.date.today())

#timedelta : 두날짜사이의 간격
today = datetime.date.today() #오늘 날짜저장
td = datetime.timedelta(days=100) # 100일 뒤 저장
print("퇴직한지 100째는 ", today +td)