import json
from core.controller import Controller

from app.models.PropertyFact import PropertyFact

class PropertyFactController(Controller):

	def store(self, fact_id, property_id):
		print(PropertyFact.new(
			fact_id = fact_id,
			property_id = property_id
		).toJson())

	def show(self, id):
		print(PropertyFact.find(id).toJson())

	def all(self):
		print(PropertyFact.all(True))
