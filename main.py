import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 1.0
        self.money = 50
        self.alive = True

    def to_study(self):
        print("Студент навчається")
        self.progress += 0.2
        self.gladness -= 5

    def to_sleep(self):
        print("Студент спить")
        self.gladness += 3

    def to_chill(self):
        print("Студент відпочиває")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10

    def to_work(self):
        print("Студент працює")
        self.money += 30
        self.gladness -= 5

    def is_alive(self):
        if self.progress < 0:
            print("Студента відрахували")
            self.alive = False
        elif self.gladness <= 0:
            print("Студент у депресії")
            self.alive = False
        elif self.progress >= 5:
            print("Студент успішно закінчив навчання")
            self.alive = False

    def end_of_day(self):
        print(f"Щастя: {self.gladness}")
        print(f"Успішність: {self.progress}")
        print(f"Гроші: {self.money}")

    def live(self, day):
        print(f"{'День ' + str(day) + ' життя ' + self.name:=^50}")

        # продумана поведінка
        if self.money < 20:
            self.to_work()
        elif self.progress < 2:
            self.to_study()
        else:
            action = random.randint(1, 3)
            if action == 1:
                self.to_study()
            elif action == 2:
                self.to_sleep()
            else:
                self.to_chill()

        self.end_of_day()
        self.is_alive()


student = Student("Микола")

for day in range(1, 366):
    if not student.alive:
        break
    student.live(day)