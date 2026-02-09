class Programmer:
    def __init__(self,name,grade="junior"):
        self.name=name
        self.grade=grade
        self.time=0
        if grade=="junior":
            self.rate=10
        elif grade=='middle':
            self.rate=15
        elif grade=='senior':
            self.rate=20
    def info(self):
        return f"{self.name}, {self.time}, {self.time*self.rate}"
    def grade_up(self):
        if self.grade=="junior":
            self.grade='middle'
            self.rate=15
        elif self.grade=='middle':
            self.rate='senior'
            self.rate=20
        elif self.grade=='senior':
            self.rate+=1
    def work(self,time):
        self.time+=time

        
programmer = Programmer('Васильев Иван')
programmer.work(750)
print(programmer.info())
programmer.grade_up()
programmer.work(500)
print(programmer.info())
programmer.grade_up()
programmer.work(250)
print(programmer.info())
programmer.grade_up()
programmer.work(250)
print(programmer.info())