import json
from core.db.DB import DB
class Model:
	table_name : str = None
	cols : list = []
	original_data = None
	primary_key : str = None

	@classmethod
	def new(cls, **kwargs):
		result = DB.prepare(f'''
			INSERT INTO {cls.table_name} ({",".join(cls.cols)})
			VALUES (:{",".join(cls.cols)})
		''', True, **kwargs)

		ins = cls(**kwargs)
		ins.id = result['id']
		ins.original_data = {'id': result['id'], **kwargs}

		return ins

	@classmethod
	def all(cls, toJson = False, **kwargs) -> list:
		result = DB.query(f'''
			SELECT {cls.table_name}.* FROM {cls.table_name}
		''', True, **kwargs)
		res = []
		for data in result:
			id = data.pop('id')
			ins = cls(*data)
			ins.original_data = {'id': id, **data}
			ins.id = id
			res.append(ins.toDict() if toJson else ins)
		# ins = cls(**kwargs)

		return json.dumps(res) if toJson else res

	@classmethod
	def find(cls, value):
		key = cls.primary_key if cls.primary_key != None and cls.primary_key != '' else 'id'
		print({f'{key}' : value})
		result = DB.prepare(f'''
			SELECT {cls.table_name}.* FROM {cls.table_name}
			WHERE {key} = :{key}
			LIMIT 1
		''', True, True, **{f'{key}' : value})
		result = result['fetch'][0] if len(result['fetch']) > 0 else None
		if result != None:
			id = result.pop('id')
			ins = cls(*result)
			ins.original_data = {'id': id, **result}
			ins.id = id
			result = ins

		return result

	def toJson(self):
		return json.dumps(self.toDict())
	
	def toDict(self):
		if self.original_data != None : return self.original_data
		else:
			self.cols = ['name']
			res = {'id' : self.id}
			for key in self.cols:
				res[key] = getattr(self, key)
			return res
