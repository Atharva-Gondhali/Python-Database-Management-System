
class variables:
	def __init__( self ):
		self.a = 10
		self.b = 10
		self.add = 0

	def add(self):
		self.add = self.a + self.b

class calculate:
	def display(self):
		print( self.add )


obj = variables()	
obj.add()
calculate.display( obj )