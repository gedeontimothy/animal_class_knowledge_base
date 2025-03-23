from core.model import Model
class Property(Model):
	table_name = "properties"
	cols = ['characteristic_id', 'libelle']

	def __init__(self, characteristic_id, libelle):
		self.id = None
		self.characteristic_id = characteristic_id
		self.libelle = libelle
