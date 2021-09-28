try:
    print("나누기 전용 계산기입니다.")
    # num1=int(input("첫번째 숫자를 입력하세요 : "))
    # num2=int(input("첫번째 숫자를 입력하세요 : "))
    # Print("{0} / {1} = {2}".format(num1/num2,int(num1/num2)))

    nums=[] # list 형태
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0}/{1}={2}".format(nums[0],nums[1], int(nums[2])))
except ValueError:
    print("에러! 잘못된값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)