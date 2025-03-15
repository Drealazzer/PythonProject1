#проект симулятор студента
import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.happy=r.randint(10,100)
        self.progress=r.randint(4,10)
        self.money=r.randint(10,100)
        self.alive=True
    def work(self):
        print("час працювати")
        self.money += r.randint(30,100)
        self.progress -= r.randint(1, 3)
        self.happy -= r.randint(5,15)
        if self.happy > 100: self.happy = 100
        if self.progress > 10: self.progress = 10
    def study(self):
        print('Час для навчання')
        self.happy -= r.randint(1,20)
        self.progress += r.randint(1,10)
        if self.happy > 100: self.happy = 100
        if self.progress > 10: self.progress = 10
    def sleep(self):
        print('Час для сну')
        self.happy += r.randint(1, 15)
        self.progress -= r.randint(1, 3)
        if self.happy > 100: self.happy = 100
        if self.progress > 10: self.progress = 10
    def chill(self):
        print('Час для відпочинку')
        self.happy+=r.randint(30,100)
        self.progress-=r.randint(1,4)
        self.money-=r.randint(5,30)
        if self.happy > 100: self.happy = 100
        if self.progress > 10: self.progress = 10
    def isAlive(self):
        if 1<=self.progress<5:
            print("Ти на грані відрахування. Починай навчатися")
            self.study()
            self.alive=True
        elif self.progress<=1:
            print("Відрахування з інституту")
            self.alive = False
        elif self.progress>=5:
            print("Відмінно навчаєшся")
            self.alive = True
    def everyday(self):
        print("Рівень щастя", self.happy)
        print("Прогрес навчання", self.progress)
        print("Кількість грошей", self.money)

    def studyLife(self, day):
        day = "День №" + str(day)
        print(day)

        if self.progress <= 4:
            self.study()
        elif self.money <= 20:
            self.work()
        elif self.happy <= 20:
            self.chill()
        else:
            res = r.randint(1, 3)
            if res == 1:
                self.study()
            elif res == 2:
                self.chill()
            elif res == 3:
                self.sleep()

        self.everyday()
        self.isAlive()

st1=Student('Олег')
print("Життя студента", st1.name)
for k in range(1,366):
    if st1.alive==False:
        break
    st1.studyLife(k)
