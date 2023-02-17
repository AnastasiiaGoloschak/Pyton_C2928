class Human:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.weight = 0
        self.height = 0
    def live(self):
        print(self.name,' is living')

class Teacher(Human):
    def __init__(self, name):
      super().__init__(name)
      self.beauty = 0
      self.kindness = 0
    def learn(self):
        print(self.name,' is learning')
    def scream(self):
        print(self.name,' is screaming')

class Student(Human):
    def __init__(self, name):
      super().__init__(name)
      self.laziness = 0
      self.generosity = 0
    def studies(self):
        print(self.name,' is studying')
    def dohomework(self):
        print(self.name,' is doing homework')
      
      