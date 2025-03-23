from core.model import Model
class Knowledge(Model):
	table_name = "knowledges"
	cols = ['name']
	def __init__(self, name):
		self.id = None
		self.name = name


