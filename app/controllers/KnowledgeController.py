import json
from core.controller import Controller

from app.models.Knowledge import Knowledge

class KnowledgeController(Controller):

	def store(self, name):
		print(Knowledge.new(name=name).toJson())

	def show(self, id):
		print(Knowledge.find(id).toJson())

	def all(self):
		print(Knowledge.all(True))
