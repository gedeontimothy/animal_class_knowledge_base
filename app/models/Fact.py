from core.model import Model
class Fact(Model):
	table_name = "facts"
	cols = ['name', 'knowledge_id', 'animal_class_id', 'description']
	
	def __init__(self, knowledge_id, animal_class_id, name, description = None):
		self.id = None
		self.name = name
		self.knowledge_id = knowledge_id
		self.animal_class_id = animal_class_id
		self.description = description

