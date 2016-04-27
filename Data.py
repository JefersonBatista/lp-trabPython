#! /usr/bin/python
# -*- coding: utf-8 -*-

class Data:
	def __init__(self, dateStr):
		self.__dia = int(dateStr[0:2])
		self.__mes = int(dateStr[3:5])
		self.__ano = int(dateStr[6:10])
		
	def getDia(self):
		return self.__dia
		
	def getMes(self):
		return self.__mes
		
	def getAno(self):
		return self.__ano
		
	def strDate(self):
		return '%.2d/%.2d/%d\n' % (self.__dia, self.__mes, self.__ano)
	
	@staticmethod	
	def comparaData(date, another):
		if date.__ano < another.__ano:
			return 1
		if date.__ano > another.__ano:
			return -1
		if date.__mes < another.__mes:
			return 1
		if date.__mes > another.__mes:
			return -1
		if date.__dia < another.__dia:
			return 1
		if date.__dia > another.__dia:
			return -1
		return 0
		
		
