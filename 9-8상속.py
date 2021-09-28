#일반유닛
class unit:
    def __init__(self,name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상유닛이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name,location,self.speed))
#공격유닛
class AttackUnit(unit): # AttackUnit(자식클래스)이 unit(부모)을 상속받음 
    def __init__(self,name, hp, speed,damage):
        unit.__init__(self,name,hp,speed)
        self.damage = damage
    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 : {2}]"\
        .format(self.name,location, self.damage))

    def damaged(self,damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0}: 파괴되었습니다.".format(self.name))


#드랍쉽 : 공중유닛, 수송기, 공격x
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


#건물 
class BuildingUnit(unit):
    def __init__(self, name, hp, location):
        #unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) #super 사용시 ()사용 self사용x
        self.location = location
        
     

