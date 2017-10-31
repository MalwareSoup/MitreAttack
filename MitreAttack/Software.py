class Software:
	ID = ""
	displaytitle = ""
	description = ""
	fullurl = ""
	aliases = []

	def __init__(self, ID, displaytitle, description, fullurl, aliases, techniques):
		self.ID = ID
		self.displaytitle = displaytitle
		self.description = description
		self.fullurl = fullurl
		self.aliases = aliases
		self.techniques = {}
		self.groups = {}
		for tech in techniques:
			self.techniques[tech['fulltext'].split('/')[1]] = tech

	def __str__(self):
		return "{}: {}".format(self.ID, self.displaytitle)

	def __repr__(self):
		return "{}: {}".format(self.ID, self.displaytitle)

	def search(self,query):
		pass