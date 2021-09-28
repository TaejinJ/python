# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))   # close해줄필요가없다.

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고있어요.")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read()) #study.txt 내용을 불러오기.