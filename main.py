class Human:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.weight = 0
        self.height = 0 
    def live(self):
        print(self.name,' is living')
    def fight(self):
        print(self.name,' is fighting')
  
class Hero(Human):
    def __init__(self, name):
      super().__init__(name)
      self.strong = 0
      self.smart = 0
      self.kindness = 0
    def win(self):
        print(self.name,' is winning')
    def savetheworld(self):
        print(self.name,' is saveingtheworld')

class Enemy(Human):
    def __init__(self, name):
      super().__init__(name)
      self.cunning = 0
      self.evil = 0 
      self.madness = 0
    def lose(self):
        print(self.name,' is lost')
    def violate(self):
        print(self.name,' is violating') 