from core.controller import Controller

from app.models.Rule import Rule

class RuleController(Controller):

	def store(self, knowledge_id, animal_class_id, name, description = None):
		print(Rule.new(
			knowledge_id = knowledge_id,
			animal_class_id = animal_class_id,
			name = name,
			description = description
		).toJson())

	def show(self, id):
		print(Rule.find(id).toJson())

	def all(self):
		print(Rule.all(True))
