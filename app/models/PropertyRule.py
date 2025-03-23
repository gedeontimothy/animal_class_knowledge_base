from core.model import Model
class PropertyRule(Model):
	table_name = "property_rules"
	cols = ['rule_id', 'property_id', 'condition', 'action']

	def __init__(self, rule_id, property_id, condition, action = None):
		self.id = None
		self.rule_id = rule_id
		self.property_id = property_id
		self.condition = condition
		self.action = action
