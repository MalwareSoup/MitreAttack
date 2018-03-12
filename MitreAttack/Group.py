# -*- coding: utf-8 -*-

class Group:
	ID = ""
	displaytitle = ""
	description = ""
	fullurl = ""
	aliases = []

	def __init__(self, ID, displaytitle, description, fullurl, aliases, techniques, software):
		self.ID = ID.encode('ascii','replace')
		self.displaytitle = displaytitle.encode('ascii','replace')
		self.description = description.encode('ascii','replace')
		self.fullurl = fullurl.encode('ascii','replace')
		self.aliases = aliases
		self.techniques = {}
		self.software = {}
		for tech in techniques:
			self.techniques[tech['fulltext'].split('/')[1]] = tech
		for item in software:
			self.software[item['fulltext'].split('/')[1]] = item

	def __str__(self):
		return "{}: {}".format(self.ID.encode('ascii','replace'), self.displaytitle.encode('ascii','replace'))

	def __repr__(self):
		return "{}: {}".format(self.ID.encode('ascii','replace'), self.displaytitle.encode('ascii','replace'))

	def search(self,query):
		pass
