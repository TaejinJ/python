# cabinet = {3:"유재석", 100:"김태호"}   #방법 1사전일경우 중괄호사용  {key:"value"}형태
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5])    # 오류출력후 프로그램종료
# print(cabinet.get(5))      #none이라고 출력하고 값을 계속출력가능 
# print(cabinet.get(5,"사용가능")) 
# print("hi")

# print(3 in cabinet) # boolean 
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet)

# 새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key,value 둘다 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)