#! /usr/bin/python
# -*- coding: utf-8 -*-

from Data import Data

class Livro:
	def __init__(self, code):
		self.__code = code
		
	def strLivro(self):
		string = ''
		string += str(self.__code) + '\n'
		string += self.__title
		string += self.__author
		string += self.__guess
		string += self.__date.strDate()
		string += self.__edit
		string += self.__resume
		return string + '\n'
	
	def setTitle(self, title):
		self.__title = title
	
	def setAuthor(self, author):
		self.__author = author
		
	def setGuess(self, guess):
		self.__guess = guess
		
	def setDate(self, date):
		self.__date = date
	
	def setEdit(self, edit):
		self.__edit = edit
	
	def setResume(self, resume):
		self.__resume = resume
		
	def getCode(self):
		return self.__code
		
	@staticmethod	
	def cmpCode(book, another):
		return book.__code > another.__code
	
	@staticmethod
	def cmpTitle(book, another):
		if book.__title < another.__title:
			return True
		if book.__title > another.__title:
			return False
		else:
			return Livro.cmpCode(book, another)
	
	@staticmethod
	def cmpAuthor(book, another):
		if book.__author > another.__author:
			return True
		if book.__author < another.__author:
			return False
		else:
			return Livro.cmpCode(book, another)
			
	@staticmethod
	def cmpData(book, another):
		if Data.comparaData(book.__date, another.__date) == 1:
			return True
		if Data.comparaData(book.__date, another.__date) == -1:
			return False
		if comparaData(book.__date, another.__date) == 0:
			return Livro.cmpCode(book, another)
	
	
