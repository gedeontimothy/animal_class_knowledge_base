import json
from core.controller import Controller

from app.models.Property import Property

class PropertyController(Controller):

	def store(self, characteristic_id, libelle):
		print(Property.new(characteristic_id = characteristic_id, libelle = libelle).toJson())

	def show(self, id):
		print(Property.find(id).toJson())

	def all(self):
		print(Property.all(True))
