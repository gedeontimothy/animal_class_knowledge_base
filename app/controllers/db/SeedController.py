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

		for data in [
			{'name' : 'Classes d\'animaux'}
		]:
			Knowledge.new(**data)
		print("> Seed Table [Knowledge]\n")

		for data in [
			{'name' : "Locomotion", 'description' : None},
			{'name' : "Reproduction", 'description' : None},
			{'name' : "Respiration", 'description' : None},
			{'name' : "Vertebrale", 'description' : None},
			{'name' : "Corporelle", 'description' : None},
			{'name' : "Alimentation", 'description' : None},
		]:
			Characteristic.new(**data)
		print("> Seed Table [Characteristic]\n")

		locomotive_id = Characteristic.where({'name': 'Locomotion'}).id
		reproduction_id = Characteristic.where({'name': 'Reproduction'}).id
		respiration_id = Characteristic.where({'name': 'Respiration'}).id
		vertebrale_id = Characteristic.where({'name': 'Vertebrale'}).id
		corporelle_id = Characteristic.where({'name': 'Corporelle'}).id
		alimentation_id = Characteristic.where({'name': 'Alimentation'}).id
		for data in [
			{'characteristic_id' : locomotive_id, 'libelle' : 'Aquatique'},
			{'characteristic_id' : locomotive_id, 'libelle' : 'Terrestre'},
			{'characteristic_id' : locomotive_id, 'libelle' : 'Aériennes'},

			{'characteristic_id' : reproduction_id, 'libelle' : 'Vivipares'},
			{'characteristic_id' : reproduction_id, 'libelle' : 'Ovipares'},
			{'characteristic_id' : reproduction_id, 'libelle' : 'Ovovivipares'},

			{'characteristic_id' : respiration_id, 'libelle' : 'Pulmonaire'},
			{'characteristic_id' : respiration_id, 'libelle' : 'Branchiale'},
			{'characteristic_id' : respiration_id, 'libelle' : 'Cutanée'},
			{'characteristic_id' : respiration_id, 'libelle' : 'Trachéenne'},

			{'characteristic_id' : vertebrale_id, 'libelle' : 'Vertebré'},
			{'characteristic_id' : vertebrale_id, 'libelle' : 'Invertebré'},

			{'characteristic_id' : corporelle_id, 'libelle' : 'Homéothermes'},
			{'characteristic_id' : corporelle_id, 'libelle' : 'Poïkilothermes'},

			{'characteristic_id' : alimentation_id, 'libelle' : 'Herbivores'},
			{'characteristic_id' : alimentation_id, 'libelle' : 'Carnivores'},
			{'characteristic_id' : alimentation_id, 'libelle' : 'Omnivores'},
			{'characteristic_id' : alimentation_id, 'libelle' : 'Détritivores'},
		]:
			Property.new(**data)
		print("> Seed Table [Property]\n")

		amphibien_id = AnimalClass.where({'name': 'Amphibien'}).id
		insecte_id = AnimalClass.where({'name': 'Insectes'}).id
		mamifere_id = AnimalClass.where({'name': 'Mamifère'}).id
		oiseau_id = AnimalClass.where({'name': 'Oiseau'}).id
		poisson_id = AnimalClass.where({'name': 'Poisson'}).id
		reptile_id = AnimalClass.where({'name': 'Reptile'}).id

		knowledge_id = Knowledge.where({'name': 'Classes d\'animaux'}).id
		for data in [
			{
				'knowledge_id': knowledge_id,
				'animal_class_id': amphibien_id,
				'name': 'Base des fait des Amphibiens',
				'description': "Est de la classe Amphibien"
			},
			{
				'knowledge_id': knowledge_id,
				'animal_class_id': insecte_id,
				'name': 'Base des fait des Insectes',
				'description': "Est de la classe Insecte"
			},
			{
				'knowledge_id': knowledge_id,
				'animal_class_id': mamifere_id,
				'name': 'Base des fait des Mamifère',
				'description': "Est de la classe Mamifère"
			},
			{
				'knowledge_id': knowledge_id,
				'animal_class_id': oiseau_id,
				'name': 'Base des fait des Oiseau',
				'description': "Est de la classe Oiseau"
			},
			{
				'knowledge_id': knowledge_id,
				'animal_class_id': poisson_id,
				'name': 'Base des fait des Poissons',
				'description': "Est de la classe Poisson"
			},
			{
				'knowledge_id': knowledge_id,
				'animal_class_id': reptile_id,
				'name': 'Base des fait des Reptiles',
				'description': "Est de la classe Reptile"
			},
		]:
			Fact.new(**data)
		print("> Seed Table [Fact]\n")

		for data in [
			{
				'knowledge_id': 1,
				'animal_class_id': amphibien_id,
				'name': 'Base des règles des Amphibiens',
				'description': None
			},
			{
				'knowledge_id' : 1,
				'animal_class_id' : mamifere_id,
				'name' : "Base des Règles des Mamifère",
				'description' : None,
			},
		]:
			Rule.new(**data)
		print("> Seed Table [Rule]\n")

		fact_is_amphibien_id = Fact.where({'knowledge_id': knowledge_id, 'animal_class_id': amphibien_id}).id
		fact_is_insecte_id = Fact.where({'knowledge_id': knowledge_id, 'animal_class_id': insecte_id}).id
		fact_is_mamifere_id = Fact.where({'knowledge_id': knowledge_id, 'animal_class_id': mamifere_id}).id
		fact_is_oiseau_id = Fact.where({'knowledge_id': knowledge_id, 'animal_class_id': oiseau_id}).id
		fact_is_poisson_id = Fact.where({'knowledge_id': knowledge_id, 'animal_class_id': poisson_id}).id
		fact_is_reptile_id = Fact.where({'knowledge_id': knowledge_id, 'animal_class_id': reptile_id}).id
		for data in [
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Terrestre',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Aquatique',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': reproduction_id,
					'libelle': 'Ovipares',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': respiration_id,
					'libelle': 'Pulmonaire',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': respiration_id,
					'libelle': 'Branchiale',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': respiration_id,
					'libelle': 'Cutanée',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': vertebrale_id,
					'libelle': 'Vertebré',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': corporelle_id,
					'libelle': 'Poïkilothermes',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Carnivores',
				}).id,
			},
			{
				'fact_id': fact_is_amphibien_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Omnivores',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Aquatique',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Terrestre',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Aériennes',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': reproduction_id,
					'libelle': 'Ovipares',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': respiration_id,
					'libelle': 'Trachéenne',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': vertebrale_id,
					'libelle': 'Invertebré',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': corporelle_id,
					'libelle': 'Poïkilothermes',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Herbivores',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Carnivores',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Omnivores',
				}).id,
			},
			{
				'fact_id': fact_is_insecte_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Détritivores',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Aquatique',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Terrestre',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': reproduction_id,
					'libelle': 'Vivipares',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': respiration_id,
					'libelle': 'Pulmonaire',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': vertebrale_id,
					'libelle': 'Vertebré',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': corporelle_id,
					'libelle': 'Homéothermes',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Herbivores',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Carnivores',
				}).id,
			},
			{
				'fact_id': fact_is_mamifere_id,
				'property_id': Property.where({
					'characteristic_id': alimentation_id,
					'libelle': 'Omnivores',
				}).id,
			},
		]:
			PropertyFact.new(**data)
		print("> Seed Table [PropertyFact]\n")

		for data in [
			{
				'rule_id' : Rule.where({
					'knowledge_id': knowledge_id,
					'animal_class_id': amphibien_id,
				}).id,
				'property_id' : Property.where({
					'characteristic_id': locomotive_id,
					'libelle': 'Terrestre',
				}).id,
				'condition' : 'S\'il se déplace sur terre, sable, route, goudron, macadam',
				'action' : None
			}
		]:
			PropertyRule.new(**data)
		print("> Seed Table [PropertyRule]\n")
