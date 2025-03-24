import json
from core.controller import Controller

from app.models.AnimalClass import AnimalClass

class AnimalClassController(Controller):

	def store(self, name, description=None):
		print(AnimalClass.new(name = name, description = description).toJson())

	def show(self, id):
		print(AnimalClass.find(id).toJson())

	def all(self):
		print(AnimalClass.all(True))
