# import theather_module 
# theather_module.price(3)  #3명이서 영화보러갔을때 가격
# theather_module.price_morning(4) #4명이서 조조할인영화보러갔을때
# theather_module.price_soldier(5) # 군인 5명이서 영화보러갔을때

# import theather_module as mv  #theater_module -> mv로 변환
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theather_module import *
# #from random import * 
# price(3)
# price_morning(4)
# price_soldier(5)

# from theather_module import price,price_morning
# price(5)
# price_morning(6)
# price_soldier(9)

from theather_module import price_soldier as price # price_soldier -> price
price(5)