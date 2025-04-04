import os
from .Database import Database

class DB :

	db_name = None
	db_instance = None
	app_path = None

	@classmethod
	def getDBConnection(self):
		return DB.initDBInstance().getDBConnection()

		
	@classmethod
	def newDBConnection(self, db_name = None):
		DB.setDBInstance(Database(db_name if db_name != None else DB.getDBName()))
		return DB.db_instance

	@classmethod
	def initDBInstance(self) -> Database:
		if DB.db_instance == None:
			DB.newDBConnection()
		return DB.getDBInstance() 

	@classmethod
	def getDBInstance(self):
		return DB.db_instance

	@classmethod
	def setDBInstance(self, instance):
		DB.db_instance = instance

	@classmethod
	def getDBName(cls):
		if cls.db_name == None :
			work_path = cls.app_path if cls.app_path != None else os.getcwd()
			cls.db_name = work_path + os.sep + 'db' + os.sep + 'tp_1_ia.sqlite'
		return cls.db_name

	@classmethod
	def query(cls, *args, **kwargs):
		return DB.initDBInstance().query(*args, **kwargs)

	@classmethod
	def prepare(self, *args, **kwargs):
		return DB.initDBInstance().prepare(*args, **kwargs)
