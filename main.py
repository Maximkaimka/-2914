import random
class Maxim:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
        self.money = 13
        self.Hungry = 0


        def to_sleep(self):
            print("Хочу спати")
            self.gladness+=4
            self.Hungry-=3

        def to_working(self):
            print("Треба йти на роботу")
            self.progress+=1
            self.gladness-=3
            self.money +=30
            self.Hungry -=4
        def to_chill(self):
            print("Відпочинь")
            self.gladness+=5
            self.progress-=0.4
            self.Hungry -=1

        def to_walking(self):
            print("Погуляй")
            self.gladness+=5
            self.progress-=2
            self.money-=5
            self.Hungry -=2

        def to_shoppping(self):
            print("Час сходити в магазин")
            self.gladness+=4
            self.money-=10
            self.Hungry -=1

        def to_eating(self):
            print("Ти голодний, треба поїсти")
            self.gladness+=3
            self.Hungry +=30

        def to_Take_a_bath(self):
            print("Прийми ванну")
            self.gladness+=2

        def is_alive(self):
            if self.progress<-0.5:
                print("Звільнили з роботи")
                self.alive=False
            elif self.gladness<=0:
                print("Дипресія...")
                self.alive=False
            elif self.progress>13:
                print("Повисили посаду на роботі")
            elif self.money<-20:
                print("Мало грошей")

        def end_of_day(self):
            print(f"Радість = {self.gladness}")
            print(f"Прогрес = {round(self.progress,2)}")