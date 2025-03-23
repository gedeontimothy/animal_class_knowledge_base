from core.model import Model
class AnimalClass(Model):
	table_name = "animal_classes"
	cols = ['name', 'description']

	def __init__(self, name, description=None):
		self.id = None
		self.name = name
		self.description = description
