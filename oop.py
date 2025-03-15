# class Car:
#     #speed=110
#     def __init__(self, speed_car):
#         self.speed=speed_car
#     def info(self):
#         print("Швидкість авто:",self.speed)
# sp=int(input('Максимальная скорость авто: '))
# auto=Car(sp)
# #print("Швидкість авто:",auto.speed)
# auto.info()
# auto2=Car(180)
# auto2.info()
#from itertools import count


# class Pupils:
#     count=0
#     def __init__(self, name, height):
#         self.name=name
#         self.height=height
#         Pupils.count+=1
#     def __str__(self):
#         print("Ім'я учня:", self.name,"Зріст: ", self.height)
#     def __bool__(self):
#         return self.name!=None
#     def __len__(self):
#         return self.height
#
# p1=Pupils("Ігор",155)
# p1.__str__()
# p2=Pupils("Ольга",158)
# p2.__str__()
# p3=Pupils("Петро",156)
# p3.__str__()
# print("Учнів:",p1.count)
# #print(p1.__bool__())
# print("Чи є им'я у другого учня? (bool)",bool(p2))
# #print(p3.__len__())
# print("Який зріст у третього учня? (len)",len(p3))


#проект симулятор студента
import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.happy=r.randint(10,100)
        self.progress=r.randint(0,10)
        self.alive=True
    def study(self):
        print('Час для навчання')
        self.happy-=r.randint(1,50)
        self.progress+=r.randint(1,10)
    def sleep(self):
        print('Час для сну')
        self.happy += r.randint(1, 10)
    def chill(self):
        print('Час для відпочинку')
        self.happy+=r.randint(50,100)
        self.progress-=r.randint(5,10)
    def isAlive(self):
        if 1<self.progress<5:
            print("Ти на грані відрахування. Починай навчатися")
            self.alive=False
        elif self.progress<=1:
            print("Відрахування з інституту")
            self.alive = False
        elif self.progress >=5:
            print("Відмінно навчаєшся")
            self.alive = True
    def everyday(self):
        print("Рівень щастя", self.happy)
        print("Прогрес навчання", self.progress)
    def studyLife(self,day):
        day = "День №"+str(day)
        print(day)
        res=r.randint(1,3)
        if res == 1:
            self.study()
        elif res == 2:
            self.chill()
        elif res ==3:
            self.sleep()
        self.everyday()
        self.isAlive()

st1=Student('Олег')
print("Життя студента", st1.name)
for k in range(1,8):
    if st1.alive==False:
        break
    st1.studyLife(k)
