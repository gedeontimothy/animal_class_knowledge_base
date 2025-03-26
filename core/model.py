import json
from core.db.DB import DB
class Model:
	table_name : str = None
	cols : list = []
	original_data = None
	primary_key : str = None
	has_many = None

	@classmethod
	def new(cls, **kwargs):
		result = DB.prepare(f'''
			INSERT INTO {cls.table_name} ({",".join(cls.cols)})
			VALUES (:{", :".join(cls.cols)})
		''', True, **kwargs)

		ins = cls(**kwargs)
		ins.id = result['id']
		ins.original_data = ins.current_data = {'id': result['id'], **kwargs}

		return ins

	@classmethod
	def all(cls, toJson = False, toDict = False, withRelation = False, **kwargs) -> list:
		result = DB.query(f'''
			SELECT {cls.table_name}.* FROM {cls.table_name}
		''', True, **kwargs)
		res = []
		for data in result:
			id = data.pop('id')
			ins = cls(*data)
			ins.original_data = ins.current_data = {'id': id, **data}
			ins.id = id
			if(withRelation and ins.has_many != None) :
				cls.hasMany(ins, toJson or toDict)
				
			res.append(ins.toDict() if toJson or toDict else ins)
		# ins = cls(**kwargs)

		return json.dumps(res) if toJson else res

	@classmethod
	def find(cls, value, toDict = False, withRelation = False):
		key = cls.primary_key if cls.primary_key != None and cls.primary_key != '' else 'id'
		# print({f'{key}' : value})
		result = DB.prepare(f'''
			SELECT {cls.table_name}.* FROM {cls.table_name}
			WHERE {key} = :{key}
			LIMIT 1
		''', True, True, **{f'{key}' : value})
		result = result['fetch'][0] if len(result['fetch']) > 0 else None
		if result != None:
			id = result.pop('id')
			ins = cls(*result)
			ins.original_data = ins.current_data = {'id': id, **result}
			ins.id = id
			if(withRelation and ins.has_many != None) :
				cls.hasMany(ins, toDict)
			result = ins if toDict == False else ins.toDict()

		return result

	@classmethod
	def where(cls, where, value = {}, toDict = False, withRelation = False):
		result = DB.prepare(f'''
			SELECT {cls.table_name}.* FROM {cls.table_name}
			WHERE {where if isinstance(where, str) else(' AND '.join([f"{key} = :{key}" for key in where]))}
			LIMIT 1
		''', True, True, **(value if isinstance(where, str) else where))
		result = result['fetch'][0] if len(result['fetch']) > 0 else None
		if result != None:
			id = result.pop('id')
			ins = cls(*result)
			ins.original_data = ins.current_data = {'id': id, **result}
			ins.id = id
			if(withRelation and ins.has_many != None) :
				cls.hasMany(ins, toDict)
			result = ins if toDict == False else ins.toDict()
			# result = ins

		return result

	@classmethod
	def hasMany(cls, model, toDict = False) :
		result = []
		for rel in model.has_many :
			result = rel['model'].whereAll({'characteristic_id' : getattr(model, 'id')}, {}, toDict, True)
			# if val != None :
			# 	result.append(val)
		# print(result)
		k = rel['model'].__name__.lower()
		model.current_data[k] = result

	@classmethod
	def whereAll(cls, where, value = {}, toDict = False, withRelation = True, **kwargs) -> list:
		result = DB.prepare(f'''
			SELECT {cls.table_name}.* FROM {cls.table_name}
			WHERE {where if isinstance(where, str) else(' AND '.join([f"{key} = :{key}" for key in where]))}
		''', True, True, **(value if isinstance(where, str) else where))
		# ''', True, True, **{**(value if isinstance(where, str) else {f'{where}' : value}), **kwargs})
		res = []
		result = result['fetch'] if len(result['fetch']) > 0 else None
		for data in result:
			id = data.pop('id')
			ins = cls(*data)
			ins.original_data = ins.current_data = {'id': id, **data}
			if(withRelation and ins.has_many != None) :
				cls.hasMany(ins, toDict)
			ins.id = id
			res.append(ins.toDict() if toDict else ins)
		# ins = cls(**kwargs)

		return res
		# return json.dumps(res) if toDict else res
	

	def toJson(self):
		return json.dumps(self.toDict())
	
	def toDict(self):
		if self.current_data != None : return self.current_data
		else:
			self.cols = ['name']
			res = {'id' : self.id}
			for key in self.cols:
				res[key] = getattr(self, key)
			return res
