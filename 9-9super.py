class unit:
    def __init__(self):
        print("unit 생성자")

class Flyabe:
    def __init__(self):
        print("Flyabe 생성자")

class FlyAbleUnit(Flyabe,unit):
    def __init__(self):
        super().__init__()
        unit.__init__(self)
        Flyabe.__init__(self)


#드랍쉽
dropship = FlyAbleUnit()


 