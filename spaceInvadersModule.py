import viz
class Ship:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		viz.startLayer(viz.QUADS)
		viz.vertexColor(1, 0, 0)
		viz.pointSize(100)
		viz.vertex(-5,0)
		viz.vertex(+5, 10)
		viz.vertex(+5, 0)
		viz.vertex(-5, 10)
		viz.endLayer()
		
		viz.startLayer(viz.QUADS)
		viz.vertexColor(0, 0, 1)
		viz.pointSize(100)
		viz.vertex(-1, +10)
		viz.vertex(+1, +10)
		viz.vertex(+1, +15)
		viz.vertex(-1, +15)
		viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
class Alien:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		viz.startLayer(viz.QUADS)
		viz.vertexColor(0,0 , 0)
		viz.pointSize(100)
		viz.vertex(-1, 0)
		viz.vertex(+1, 0)
		viz.vertex(+1, 1)
		viz.vertex(-1, 1)
		viz.endLayer()
		
		viz.startLayer(viz.QUADS)
		viz.vertexColor(0, 1, 0)
		viz.pointSize(100)
		viz.vertex(-5, 0)
		viz.vertex(+5, 0)
		viz.vertex(+5, 10)
		viz.vertex(-5, 10)
		viz.endLayer()
		
		
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
class Bullet:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		viz.startLayer(viz.QUADS)
		viz.vertexColor(0,0 , 0)
		viz.pointSize(100)
		viz.vertex(-1, 0)
		viz.vertex(+1, 0)
		viz.vertex(+1, 2)
		viz.vertex(-1, 2)
		viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
window = viz.MainWindow		
window.ortho(-100,100,-100,100,-1,1)
window.clearcolor(viz.WHITE)
s = Ship(0, 0)
a = Alien(0,0)
b = Bullet(0,0)
viz.eyeheight(0)
viz.go()