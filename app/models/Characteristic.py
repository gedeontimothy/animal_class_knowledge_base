from core.model import Model
class Characteristic(Model):
	table_name = "characteristics"
	cols = ['name', 'description']
	
	def __init__(self, name, description=None):
		self.id = None
		self.name = name
		self.description=description
