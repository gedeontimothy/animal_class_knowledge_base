from core.model import Model
from .Property import Property
class Characteristic(Model):
	table_name = "characteristics"
	cols = ['name', 'description']
	has_many = [
		{
			'model' : Property,
			'pk' : 'id'
		}
	]
	
	def __init__(self, name, description=None):
		self.id = None
		self.name = name
		self.description=description
