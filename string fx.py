python ="Python is Amazing"
# print(python.lower())
# print(python. upper())
# print(python[0]. isupper())
# print(len(python))
# print(python.replace("Python", "Java")) # replace 찾기후 변경

index = python.index("n")
print(index)
index = python.index("n", index +1) # 두번째 n찾는거 
print(index)

# print(python.find("java")) #find에선 없으면 -1 로 반환
# # print(python.index("Java"))
# print(python.count("n"))