import sqlite3
class DBConnection:

	def __init__(self, db_name):
		self.db_name = db_name
		self.connection = None

	def initDBConnection(self):
		if(self.connection == None):
			self.newDBConnection()

	def newDBConnection(self):
		self.connection = sqlite3.connect(self.db_name)
	
	def getDBConnection(self):
		self.initDBConnection()
		return self.connection
		