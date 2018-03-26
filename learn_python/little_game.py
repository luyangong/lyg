from collections import deque

def student(name, homeworks):
	for homework in homeworks.items():
		yield (name, homework[0], homework[1])
class Teacher(object):
	def __init__(self, students):
		self.students = deque(students)
	def handle(self):
		student = self.students.pop()
		try:
			homework = next(student)
			print('handling', homework[0], homework[1], homework[2])
		except StopIteration:
			pass
		else:
			self.students.appendleft(student)
			
			
			
			