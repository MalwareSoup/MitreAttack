
# -*- coding: utf-8 -*-
class Tactic:
	fulltext = ""
	description = ""
	fullurl = ""

	def __init__(self, fulltext, description, fullurl):
		self.fulltext = fulltext.encode("utf-8")
		self.description = description.encode("utf-8")
		self.fullurl = fullurl.encode("utf-8")
		self.techniques = {}

	def __str__(self):
		return self.fulltext

	def __repr__(self):
		return self.fulltext

	def search(self):
		pass
