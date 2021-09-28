# # 마린 :  공격유닛, 군인 , 총을 쏠 수 있음

# name = "마린" 
# hp = 40
# damage = 5

# print("{0}유닛이 생성되었습니다.".format(name))
# print ("체력은 {0},공격력은 {1}\n".format(hp,damage))

# #탱크 : 공격유닛, 탱크 , 포를쏠수있는데, 일반모드 / 시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage =35

# print("{0}유닛이 생성되었습니다.".format(tank_name))
# print ("체력은 {0},공격력은 {1}\n".format(tank_hp,tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage =35

# print("{0}유닛이 생성되었습니다.".format(tank2_name))
# print ("체력은 {0},공격력은 {1}\n".format(tank2_hp,tank2_damage))


# def attack(name,location,damage):
#     print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# attack(tank2_name,"1시",tank_damage) #서로연관있는 변수나 집합 함수를 클래스로

class unit:
    def __init__(self,name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0} ,공격력{1}".format(self.hp,self.damage))

# marine1 = unit("마린",40,5)
# marine2 = unit("마린",40,5)
# tank = unit("탱크",150,35)

#__init__ 파이썬에서 쓰이는 생성자 ex 마린,탱크라는객체가만들어질때 자동으로 호출되는부분
# 클래스로부터 만들어지는 애들=객체 마린,탱크는  unit의 instance
#객체가생성될때는 init함수의 정의된 갯수와 동일하게 값을 줘야한다. self 제외


#9-2 멤버 변수

#레이스 
wrath1 = unit("레이스",80,5)
print("유닛이름은 {0}고,공격력 은 {1}".format(wrath1.name,wrath1.damage))

wrath2 = unit("빼앗은 레이스",80,5)
wrath2.clocking = True # 추가로 변수를 외부에서 넣어 할당.

if wrath2.clocking==True:
    print("{0} 는 현재 클로킹상태입니다.".format(wrath2.name)) 