from core.model import Model
class PropertyFact(Model):
	table_name = "property_facts"
	cols = ['fact_id', 'property_id']

	def __init__(self, fact_id, property_id):
		self.id = None
		self.fact_id = fact_id
		self.property_id = property_id
