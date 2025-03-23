from .args import Args

class Route:
	routes = {}

	@classmethod
	def add(self, route_name, class_):
		if Route.hasRoute(route_name) == False:
			Route.routes[route_name] = class_

	@classmethod
	def exec(self):
		if(Args.first() != None and Route.hasRoute(Args.first())) :
			el = Route.getRoute(Args.first())
			controller = el[0]()
			if hasattr(controller, el[1]):
				getattr(controller, el[1])(*Args.getFilterArgs())

	@classmethod
	def getRoutes(self):
		return Route.routes

	@classmethod
	def getRoute(self, key):
		return Route.routes[key]

	@classmethod
	def hasRoute(self, route_name):
		return True if route_name in Route.getRoutes() else False
