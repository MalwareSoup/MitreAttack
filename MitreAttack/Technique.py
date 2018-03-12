# -*- coding: utf-8 -*-

class Technique:
	ID = ""
	displaytitle = ""
	technical_description = ""
	full_url = ""
	data_sources = []

	def __init__(self, ID, displaytitle, technical_description, data_sources, full_url, thetactics):
		self.ID = ID.encode('ascii','replace')
		self.displaytitle = displaytitle.encode('ascii','replace')
		self.technical_description = technical_description.encode('ascii','replace')
		self.full_url = full_url.encode('ascii','replace')
		self.data_sources = data_sources
		self.tactics = {}
		self.groups = {}
		self.software = {}
		for i in thetactics:
			self.tactics[i['fulltext']] = i

	def __str__(self):
		return "{}: {}".format(self.ID.encode('ascii','replace') ,self.displaytitle.encode('ascii','replace'))

	def __repr__(self):
		return "{}: {}".format(self.ID.encode('ascii','replace'),self.displaytitle.encode('ascii','replace'))

	def search(self):
		pass
