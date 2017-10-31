class Tactic:
	fulltext = ""
	description = ""
	fullurl = ""

	def __init__(self, fulltext, description, fullurl):
		self.fulltext = fulltext
		self.description = description
		self.fullurl = fullurl
		self.techniques = {}

	def __str__(self):
		return self.fulltext

	def __repr__(self):
		return self.fulltext

	def search(self):
		pass