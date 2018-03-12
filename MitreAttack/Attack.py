# -*- coding: utf-8 -*-

import requests
import json
from . import Technique
from . import Tactic
from . import Group
from . import Software

class Attack:
	baseURL = "https://attack.mitre.org/api.php?action=ask&format=json&query="

	allTechniques = {}
	allTactics = {}
	allGroups = {}
	allSoftware = {}

	def __init__(self):
		self.getTechniques()
		self.getTactics()
		self.getGroups()
		self.getSoftware()
		self.linkCategories()

	def getTechniques(self):
		qualifiers = "|?Has ID"
		qualifiers += "|?Has tactic"
		qualifiers += "|?Has technical description"
		qualifiers += "|?Has data source"
		qualifiers += "|limit=9999"
		query = "{}[[Category:Technique]]{}".format(
			self.baseURL,
			qualifiers
		)
		r = requests.get(query)
		data = r.json()
		for key in data['query']['results'].keys():
			tempTechnique = data['query']['results'][key]
			# ID, displaytitle, technical_description, data_sources, full_url
			newTechnique = Technique.Technique(
				tempTechnique['printouts']['Has ID'][0], 
				tempTechnique['displaytitle'],
				tempTechnique['printouts']['Has technical description'][0], 
				tempTechnique['printouts']['Has data source'],
				tempTechnique['fullurl'],
				tempTechnique['printouts']['Has tactic']
			)
			self.allTechniques[tempTechnique['printouts']['Has ID'][0]] = newTechnique

	def getTactics(self):
		qualifiers = "|?Has description"
		qualifiers += "|limit=9999"
		query = "{}[[Category:Tactic]]{}".format(
			self.baseURL,
			qualifiers
		)
		r = requests.get(query)
		data = r.json()
		for key in data['query']['results'].keys():
			newTactic = data['query']['results'][key]
			# fulltext, description, fullurl
			self.allTactics[newTactic['fulltext']] = Tactic.Tactic(
				newTactic['fulltext'],
				newTactic['printouts']['Has description'][0], 
				newTactic['fullurl']
			)

	def getGroups(self):
		qualifiers = "|?Has ID"
		qualifiers += "|?Has alias"
		qualifiers += "|?Has description"
		qualifiers += "|?Has technique"
		qualifiers += "|?Uses software"
		qualifiers += "|limit=9999"
		query = "{}[[Category:Group]]{}".format(
			self.baseURL,
			qualifiers
		)
		r = requests.get(query)
		data = r.json()
		for key in data['query']['results'].keys():
			newGroup = data['query']['results'][key]
			# ID, displaytitle, description, fullurl, aliases, techniques, software
			self.allGroups[newGroup['printouts']['Has ID'][0]] = Group.Group(
				newGroup['printouts']['Has ID'][0],
				newGroup['displaytitle'],
				newGroup['printouts']['Has description'][0], 
				newGroup['fullurl'],
				newGroup['printouts']['Has alias'],
				newGroup['printouts']['Has technique'],
				newGroup['printouts']['Uses software']
			)

	def getSoftware(self):
		qualifiers = "|?Has ID"
		qualifiers += "|?Has alias"
		qualifiers += "|?Has description"
		qualifiers += "|?Has technique"
		qualifiers += "|limit=9999"
		query = "{}[[Category:Software]]{}".format(
			self.baseURL,
			qualifiers
		)
		r = requests.get(query)
		data = r.json()
		for key in data['query']['results'].keys():
			newSoftware = data['query']['results'][key]
			# ID, displaytitle, description, fullurl, aliases, techniques
			self.allSoftware[newSoftware['printouts']['Has ID'][0]] = Software.Software(
				newSoftware['printouts']['Has ID'][0],
				newSoftware['displaytitle'],
				newSoftware['printouts']['Has description'][0], 
				newSoftware['fullurl'],
				newSoftware['printouts']['Has alias'],
				newSoftware['printouts']['Has technique']
			)

	def linkCategories(self):
		for techniqueKey in self.allTechniques:
			for tacticKey in self.allTechniques[techniqueKey].tactics.keys():
				self.allTechniques[techniqueKey].tactics[tacticKey] = self.allTactics[tacticKey]

		for tacticKey in self.allTactics:
			for techniqueKey in self.allTechniques:
				if tacticKey in self.allTechniques[techniqueKey].tactics.keys():
					self.allTactics[tacticKey].techniques[techniqueKey] = self.allTechniques[techniqueKey]

		for techniqueKey in self.allTechniques:
			for groupKey in self.allGroups:
				if techniqueKey in self.allGroups[groupKey].techniques.keys():
					self.allGroups[groupKey].techniques[techniqueKey] = self.allTechniques[techniqueKey]
					self.allTechniques[techniqueKey].groups[groupKey] = self.allGroups[groupKey]

		for groupKey in self.allGroups:
			for softwareKey in self.allSoftware:
				if softwareKey in self.allGroups[groupKey].software.keys():
					self.allGroups[groupKey].software[softwareKey] = self.allSoftware[softwareKey]
					self.allSoftware[softwareKey].groups[groupKey] = self.allGroups[groupKey]

		for softwareKey in self.allSoftware:
			for techniqueKey in self.allTechniques:
				if techniqueKey in self.allSoftware[softwareKey].techniques.keys():
					self.allSoftware[softwareKey].techniques[techniqueKey] = self.allTechniques[techniqueKey]
					self.allTechniques[techniqueKey].software[softwareKey] = self.allSoftware[softwareKey]

	def findTechnique(self, query):
		resultList = []
		for techKey in self.allTechniques.keys():
			if self.allTechniques[techKey].displaytitle.lower().find(query.lower()) != -1:
				if self.allTechniques[techKey] not in resultList:
					resultList.append(self.allTechniques[techKey])
		if len(resultList) == 1:
			return resultList[0]
		else:
			return resultList

	def findGroup(self, query):
		resultList = []
		for groupKey in self.allGroups.keys():
			for alias in self.allGroups[groupKey].aliases:
				if alias.lower().find(query.lower()) != -1:
					if self.allGroups[groupKey] not in resultList:
						resultList.append(self.allGroups[groupKey])
		if len(resultList) == 1:
			return resultList[0]
		else:
			return resultList

	def findSoftware(self, query):
		resultList = []
		for softwareKey in self.allSoftware.keys():
			for alias in self.allSoftware[softwareKey].aliases:
				if alias.lower().find(query.lower()) != -1:
					if self.allSoftware[softwareKey] not in resultList:
						resultList.append(self.allSoftware[softwareKey])
		if len(resultList) == 1:
			return resultList[0]
		else:
			return resultList

	def search(self, query):
		# query = [{'field': field, 'value': value}]
		resultList = []
		numQueries = len(query)
		for techKey in self.allTechniques.keys():
			matches = 0
			for q in query:
				if q['field'].lower() == 'data sources':
					for source in self.allTechniques[techKey].data_sources:
						if source.lower().find(q['value'].lower()) != -1:
							matches += 1
							continue
				elif q['field'].lower() == 'tactics':
					for tacKey in self.allTechniques[techKey].tactics.keys():
						current = self.allTechniques[techKey].tactics[tacKey].fulltext.lower()
						if current.find(q['value'].lower()) != -1:
							matches += 1
							continue
				else:
					current = self.allTechniques[techKey].displaytitle.lower()
					if current.find(q['value'].lower()) != -1:
						matches += 1
						continue
			if matches == numQueries:
				if self.allTechniques[techKey] not in resultList:
					resultList.append(self.allTechniques[techKey])

		if len(resultList) == 1:
			return resultList[0]
		else:
			return resultList
