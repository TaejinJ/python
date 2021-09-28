# 자료구조의 변경
menu = {"커피","우유", "주스"}   #중괄호를 이용했기떄문에 set로 이용
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu=set(menu)
print(menu, type(menu))

