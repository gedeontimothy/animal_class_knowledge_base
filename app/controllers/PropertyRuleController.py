import json
from core.controller import Controller

from app.models.PropertyRule import PropertyRule

class PropertyRuleController(Controller):

	def store(self, rule_id, property_id, condition, action = None):
		print(PropertyRule.new(
			rule_id = rule_id,
			property_id = property_id,
			condition = condition,
			action = action
		).toJson())

	def show(self, id):
		print(PropertyRule.find(id).toJson())

	def all(self):
		print(PropertyRule.all(True))
