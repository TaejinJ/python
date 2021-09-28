# import travel.thailand # import xxxxx.ppppp< 뒤에 import를 쓸땐pppp는 모듈이나 패키지 와야한다
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage # 이건 작동가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import * 
from travel import *   # * 별이라는건 travel이라는 패키지에서 모든것을갖고온다는뜻
# # trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()


#위치확인하는법
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))