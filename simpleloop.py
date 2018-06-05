

# Simple Fibonacci series
# the sum of two elements defines the next set 

class Fibonacci():
	"""docstring for Fibonacci"""
	def __init__(self, a,b):
		self.a = a
		self.b = b
		
	def series(self):
		while(True):
			yield(self.b)
			self.a,self.b = self.b, self.a + self.b



f = Fibonacci(5,1)

for r in f.series():
	if r > 1000: break
	print(r,end=' ') # print fibonacci series