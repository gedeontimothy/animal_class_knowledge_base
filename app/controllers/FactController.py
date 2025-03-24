import json
from core.controller import Controller

from app.models.Fact import Fact

class FactController(Controller):

	def store(self, knowledge_id, animal_class_id, name, description = None):
		print(Fact.new(
			knowledge_id = knowledge_id,
			animal_class_id = animal_class_id,
			name = name,
			description = description
		).toJson())

	def show(self, id):
		print(Fact.find(id).toJson())

	def all(self):
		print(Fact.all(True))
