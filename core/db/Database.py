import sqlite3
from .DBConnection import DBConnection
class Database(DBConnection) :

	def __init__(self, db_name):
		super().__init__(db_name)
		self.initDBConnection()
		# self.db_connection = DBConnection(self.db_name)
		# self.db_connection.initDBConnection()

	def getDBName(self) -> str:
		return self.db_name

	def query(self, statement, assoc_attrs = True, **kwargs):
		conn = self.getDBConnection()
		cursor = conn.cursor()
		cursor.execute(statement, kwargs if len(kwargs) > 0 else ())
		result = []
		if assoc_attrs :
			colonnes = [description[0] for description in cursor.description]
			for ligne in cursor.fetchall():
				result.append(dict(zip(colonnes, ligne)))
		else : result = cursor.fetchall()
		return result

	def prepare(self, statement, return_val = False, assoc_attrs = False, **kwargs):
		result = None
		
		conn = self.getDBConnection()
		cursor = conn.cursor()
		cursor.execute(statement, kwargs if len(kwargs) > 0 else ())
		
		result = []
		if assoc_attrs :
			colonnes = [description[0] for description in cursor.description]
			for ligne in cursor.fetchall():
				result.append(dict(zip(colonnes, ligne)))
		else: result = cursor.fetchall()

		if(return_val) :
			result = {'id' : cursor.lastrowid, 'rowcount' : cursor.rowcount, 'fetch' : result}
		
		conn.commit()

		return result
