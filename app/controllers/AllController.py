import json
from core.controller import Controller

from app.models.AnimalClass import AnimalClass
from app.models.Knowledge import Knowledge
from app.models.Characteristic import Characteristic
from app.models.Property import Property
from app.models.Fact import Fact
from app.models.Rule import Rule
from app.models.PropertyFact import PropertyFact
from app.models.PropertyRule import PropertyRule

class AllController(Controller):

	def run(self):
		data = {
			'Knowledge': Knowledge.all(False, True),
			'AnimalClass': AnimalClass.all(False, True),
			'Rule': Rule.all(False, True),
			'Fact': Fact.all(False, True),
			'Characteristic': Characteristic.all(False, True),
			'Property': Property.all(False, True),
			'PropertyFact': PropertyFact.all(False, True),
			'PropertyRule': PropertyRule.all(False, True),
		}
		print(
			json.dumps(data)
		)
		# print(AnimalClass.new(name = name, description = description).toJson())
