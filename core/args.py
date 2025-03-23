import sys
import argparse

class Args:

	argv = None

	@classmethod
	def init(self):
		if Args.argv == None:
			Args.argv = sys.argv

	@classmethod
	def getArgs(self):
		return sys.argv
	
	@classmethod
	def first(self):
		return Args.getArgs()[1] if len(Args.getArgs()) > 1 else None

	@classmethod
	def getFilterArgs(self):
		return Args.getArgs()[2:] if len(Args.getArgs()) > 2 else []
	
	@classmethod
	def parser(self, message=None, *args, **kwargs):
		parser = argparse.ArgumentParser(description=("CLI Manage args" if message == None else message))
		for key, value in kwargs.items():
			parser.add_argument(key, **value)
		return parser