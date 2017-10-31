class Group:
	ID = ""
	displaytitle = ""
	description = ""
	fullurl = ""
	aliases = []

	def __init__(self, ID, displaytitle, description, fullurl, aliases, techniques, software):
		self.ID = ID
		self.displaytitle = displaytitle
		self.description = description
		self.fullurl = fullurl
		self.aliases = aliases
		self.techniques = {}
		self.software = {}
		for tech in techniques:
			self.techniques[tech['fulltext'].split('/')[1]] = tech
		for item in software:
			self.software[item['fulltext'].split('/')[1]] = item

	def __str__(self):
		return "{}: {}".format(self.ID, self.displaytitle)

	def __repr__(self):
		return "{}: {}".format(self.ID, self.displaytitle)

	def search(self,query):
		pass