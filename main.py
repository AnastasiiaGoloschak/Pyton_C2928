from random import randint
class Student:
  def __init__(self, name):
 		self.name = name
 		self.gladness = 0
    self.progress = 0
 		self.money = 0
 		self.alive = True
	def work(self):
 		self.money += 50
 		self.progress -= 5
 		print('Work time')
 	def study(self):
 		self.progress += 20
 		self.gladness -= 10
 		print('Study time')
 	def chill(self):
 		self.gladness += 35
 		self.progress -= 8
 		print('Chill time')
 	def sleep(self):
 		self.gladness += 4
 		print('Sleep time')
 	def say_hello(self):
 		print('Hello!')
 	def live(self):
 		live_cube = randint(1,4)
 		if live_cube == 1:
 			self.study()
 		elif live_cube == 2:
 			self.chill()
 		elif live_cube == 3:
 			self.sleep()
 		elif live_cube == 4:
 			self.say_hello()
 		elif live_cube == 5:
 			self.work()
 		self.final()
 	def final(self):
 		if self.progress == 100:
 			print('Amazing! You graduated!')
 			self.alive = False
 		elif self.progress < -20:
 			print('Too bad... You are stupid')
 			self.alive = False
 		elif self.gladness < -20:
 			print('Depression :(')
 			self.alive = False
    elif self.money < -20:
 			print('you are homeless')
 			self.alive = False
    elif self.money == 100:
 			print('Amazing! You are rich!')
 			self.alive = False