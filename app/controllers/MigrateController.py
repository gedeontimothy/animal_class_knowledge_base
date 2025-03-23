from core.controller import Controller
from core.db.DB import DB
from app.models.Knowledge import Knowledge

class MigrateController(Controller):

	# def seed(self):
	# 	# print(Knowledge.find(1))
	# 	# for s in Knowledge.all():
	# 	# 	print(s.toJson())
	# 	# Knowledge.new(name='Kiol')

	def run(self):
		DB.query('''
CREATE TABLE IF NOT EXISTS animal_classes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL
)'''
		)

		DB.query('''
CREATE TABLE IF NOT EXISTS knowledges (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(500) NOT NULL
)'''
		)

		DB.query('''
CREATE TABLE IF NOT EXISTS characteristics (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(500) NOT NULL,
	description TEXT NOT NULL
)'''
		)

		DB.query('''
CREATE TABLE IF NOT EXISTS properties (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	characteristic_id INTEGER,
	libelle VARCHAR(500) NOT NULL,

	FOREIGN KEY (characteristic_id) REFERENCES characteristics(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)'''
		)

		DB.query('''
CREATE TABLE IF NOT EXISTS facts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	knowledge_id INTEGER,
	animal_class_id INTEGER,
	name VARCHAR(500) NOT NULL,
	description TEXT NOT NULL,

	FOREIGN KEY (knowledge_id) REFERENCES knowledges(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,

	FOREIGN KEY (animal_class_id) REFERENCES animal_classes(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)'''
		)

		DB.query('''
CREATE TABLE IF NOT EXISTS rules (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	knowledge_id INTEGER,
	animal_class_id INTEGER,
	name VARCHAR(500) NOT NULL,
	description TEXT NOT NULL,

	FOREIGN KEY (knowledge_id) REFERENCES knowledges(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,

	FOREIGN KEY (animal_class_id) REFERENCES animal_classes(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)'''
		)

		DB.query('''
CREATE TABLE IF NOT EXISTS property_facts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	fact_id INTEGER,
	property_id INTEGER,

	FOREIGN KEY (property_id) REFERENCES properties(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,

	FOREIGN KEY (fact_id) REFERENCES facts(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)'''
		)

		DB.query('''
CREATE TABLE IF NOT EXISTS property_rules (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	rule_id INTEGER,
	property_id INTEGER,

	FOREIGN KEY (property_id) REFERENCES properties(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,

	FOREIGN KEY (rule_id) REFERENCES rules(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)'''
		)
