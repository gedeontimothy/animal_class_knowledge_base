from core.controller import Controller
from core.db.DB import DB
from app.models.AnimalClass import AnimalClass
from app.models.Knowledge import Knowledge
from app.models.Characteristic import Characteristic
from app.models.Property import Property
from app.models.Fact import Fact
from app.models.Rule import Rule
from app.models.PropertyFact import PropertyFact
from app.models.PropertyRule import PropertyRule

class SeedController(Controller):

	def run(self):
		for data in [
			{'name' : "Amphibien", 'description' : None},
			{'name' : "Insectes", 'description' : None},
			{'name' : "Mamifère", 'description' : None},
			{'name' : "Oiseau", 'description' : None},
			{'name' : "Poisson", 'description' : None},
			{'name' : "Reptile", 'description' : None},
		]:
			AnimalClass.new(**data)
		print("> Seed Table [AnimalClass]\n")

		# for data in [
		# 	{}
		# ]:
		# 	Knowledge.new(**data)
		# print("> Seed Table [Knowledge]\n")

		# for data in [
		# 	{}
		# ]:
		# 	Characteristic.new(**data)
		# print("> Seed Table [Characteristic]\n")

		# for data in [
		# 	{}
		# ]:
		# 	Property.new(**data)
		# print("> Seed Table [Property]\n")

		# for data in [
		# 	{}
		# ]:
		# 	Fact.new(**data)
		# print("> Seed Table [Fact]\n")

		# for data in [
		# 	{}
		# ]:
		# 	Rule.new(**data)
		# print("> Seed Table [Rule]\n")

		# for data in [
		# 	{}
		# ]:
		# 	PropertyFact.new(**data)
		# print("> Seed Table [PropertyFact]\n")

		# for data in [
		# 	{}
		# ]:
		# 	PropertyRule.new(**data)
		# print("> Seed Table [PropertyRule]\n")
