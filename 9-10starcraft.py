from random import *

#일반유닛
class unit:
    def __init__(self,name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name,location,self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#공격유닛
class AttackUnit(unit): # AttackUnit(자식클래스)이 unit(부모)을 상속받음 
    def __init__(self,name, hp, speed,damage):
        unit.__init__(self,name,hp,speed)
        self.damage = damage
    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 : {2}]"\
        .format(self.name,location, self.damage))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린",40,1,5)

    #스팀팩 : 일정시간동안 이동 및 공격속도를 증가,자기체력 10감소
    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0} : 스팀팩을 사용합니다(HP 10감소)".format(self.name))
        else:
          print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 공격력,이동불가
    siege_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.siege_mode = False #시즈모드 해제상태

    def set_siege_mode(self):
        if Tank.siege_developed == False:
            return
        #현재 시즈모드가 아닐때=> 시즈모드
        if self.siege_mode==False:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.siege_mode = True
        else:
              print("{0}: 시즈모드를 해제합니다.".format(self.name))
              self.damage /= 2
              self.siege_mode= False
        #현재 시즈모드일때 - >시즈모드 해제
    



#날수있는 기능을 가진 클래스

class FlyAble:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self,name,location):
        print("{0} : {1}방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

 #공중공격 유닛클래스           
class FlyAbleAttackUnit(AttackUnit,FlyAble):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp, 0, damage)     # 지상스피드 ㅇ      
        FlyAble.__init__(self,flying_speed) 

    def move(self,location):
        print("[공중유닛이동]")
        self.fly(self.name,location)

#레이스
class Wraith(FlyAbleAttackUnit):
    def __init__(self):
        FlyAbleAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False #클로킹모드 (해제상태)

    def clocking(self):
        if self.clocked==True:
            print("{0}: 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked =False

        else:
             print("{0}: 클로킹 모드를 설정합니다.".format(self.name))
             self.clocked =True
            
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player]님이 퇴장했습니다.")

# 게임 시작
game_start()

m1=Marine()
m2=Marine()
m3=Marine()

t1=Tank()
t2=Tank()

w1=Wraith()

#유닛 일괄 관리(생성된 모든 유닛 append처리)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1)
attack_units.append(w1)

#전군 이동

for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.siege_developed = True
print("[알림] 탱크 시즈모드가 개발되었습니다.")

#공격모드 준비(마린: 스팀팩,탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_siege_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20)) #공격은 랜덤으로 받음 (5~20)

#게임 종료
game_over()
