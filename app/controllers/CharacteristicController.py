import json
from core.controller import Controller

from app.models.Characteristic import Characteristic

class CharacteristicController(Controller):

	def store(self, name, description=None):
		print(Characteristic.new(name = name, description = description).toJson())

	def show(self, id):
		print(Characteristic.find(id).toJson())

	def all(self):
		print(Characteristic.all(True))
