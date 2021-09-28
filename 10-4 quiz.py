# 동네에 항상 대기손님이 있는 치킨맛집있습니다.
# 대기손님의 치킨요리시간을 줄이고자 자동 주문시스템을 제작
# 시스템코드를 확인하고 적절한 예외처리 구문을 넣으시오

# 조건1 : 1보다 작거나 숫자가 아닌입력값이 들어올때는 ValueError로 처리
#         출력메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기손님이 주문할수 있는 총치킨량은 10마리로 한정
#         치킨소진시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램종료
#         출력 메시지 : "재고가 소진되어 더이상 주문을 받지 않습니다."

# [코드]

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 #홀은 만석 대기번호 1부터시작.
while(True):
    try:

        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order >  chicken : 
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
    
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다."\
            .format(waiting,order))
        waiting += 1
        chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldOutError:
        print("재고가 소진되어 더이상 주문을 받지 않습니다.")
    break