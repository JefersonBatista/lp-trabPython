#! /usr/bin/python
# -*- coding: utf-8 -*-

from Livro import Livro
from Data import Data

class Catalogo:
	def __init__(self):
		self.__livros = []
		
	def add(self, livro):
		catalogo = self.__livros
		catalogo = catalogo.append(livro)
	
	def sort(self, comparator):
		catalogo = self.__livros
		self.__livros = Catalogo.quicksort(catalogo, comparator)
	
	@staticmethod	
	def quicksort(lista, comparator):
		if lista == []:
			return []
			
		n = len(lista)
		pivo = lista[0]
		menores = []
		maiores = []
		
		for i in range(1, n):
			if comparator(pivo, lista[i]):
				menores.append(lista[i])
			else:
				maiores.append(lista[i])
				
		lista = Catalogo.quicksort(menores, comparator)
		lista.append(pivo)
		lista += Catalogo.quicksort(maiores, comparator)
		return lista
		
	@staticmethod
	def cutTheLast(string):
		n = len(string)
		return string[0:n-1]
		
	def ler(self):
		arquivo = open('catalogo.txt', 'r')
		lines = arquivo.readlines()
		num = len(lines)
		i = 0
		
		while i < num:
			line = Catalogo.cutTheLast(lines[i])
			code = int(line)
			livro = Livro(code)
			
			title = Catalogo.cutTheLast(lines[i+1])
			author = Catalogo.cutTheLast(lines[i+2])
			guess = Catalogo.cutTheLast(lines[i+3])
			
			strDate = Catalogo.cutTheLast(lines[i+4])
			date = Data(strDate)
			
			edit = Catalogo.cutTheLast(lines[i+5])
			
			# Indo para a primeira linha do resumo
			i = i + 6
			resume = ''
			while lines[i] != '\r\n':
				resume = resume + lines[i]
				i += 1
				if i == num:
					break
			
			livro.setTitle(title)
			livro.setAuthor(author)
			livro.setGuess(guess)
			livro.setDate(date)
			livro.setEdit(edit)
			livro.setResume(resume)
			self.add(livro)
			
			# Indo para o próximo livro
			i += 1
		
		arquivo.close()
		
	def buscarLivro(self, code):
		catalogo = self.__livros
		n = len(catalogo)
		for i in range (0, n):
			if catalogo[i].getCode() == code:
				return i
		return n
	
	def atualizar(self):
		catalogo = self.__livros
	
		arquivo = open('atual.txt', 'r')
		lines = arquivo.readlines()
		num = len(lines)
		i = 0
		
		while i < num:
			action = Catalogo.cutTheLast(lines[i])
			
			if action == 'e\r':
				print 'e'
				line = Catalogo.cutTheLast(lines[i+1])
				code = int(line)
				index = self.buscarLivro(code)
				catalogo.pop(index)
				
				# Indo para o fim da ação de exclusão
				i = i + 2
				
			if action == 'i\r':
				print 'i'
				# Indo para as informações do livro
				i = i + 1
				
				line = Catalogo.cutTheLast(lines[i])
				code = int(line)
				livro = Livro(code)
			
				title = Catalogo.cutTheLast(lines[i+1])
				author = Catalogo.cutTheLast(lines[i+2])
				guess = Catalogo.cutTheLast(lines[i+3])
			
				strDate = Catalogo.cutTheLast(lines[i+4])
				date = Data(strDate)
			
				edit = Catalogo.cutTheLast(lines[i+5])
			
				# Indo para a primeira linha do resumo
				i = i + 6
				resume = ''
				while lines[i] != '\r\n':
					resume = resume + lines[i]
					i += 1
					if i == num:
						break
			
				livro.setTitle(title)
				livro.setAuthor(author)
				livro.setGuess(guess)
				livro.setDate(date)
				livro.setEdit(edit)
				livro.setResume(resume)
				self.add(livro)
				
			if action == 'a\r':
				print 'a'
				#Indo para as informações do livro
				i = i + 1
			
				line = Catalogo.cutTheLast(lines[i])
				code = int(line)
				index = self.buscarLivro(code)
				livro = catalogo[index]
				
				title = Catalogo.cutTheLast(lines[i+1])
				author = Catalogo.cutTheLast(lines[i+2])
				guess = Catalogo.cutTheLast(lines[i+3])
			
				strDate = Catalogo.cutTheLast(lines[i+4])
				date = Data(strDate)
			
				edit = Catalogo.cutTheLast(lines[i+5])
			
				# Indo para a primeira linha do resumo
				i = i + 6
				resume = ''
				while lines[i] != '\r\n':
					resume = resume + lines[i]
					i += 1
					if i == num:
						break
			
				livro.setTitle(title)
				livro.setAuthor(author)
				livro.setGuess(guess)
				livro.setDate(date)
				livro.setEdit(edit)
				livro.setResume(resume)
			
			# Indo para a próxima ação
			i += 1
		
		arquivo.close()
	
	def registro(self):
		catalogo = self.__livros
		num = len(catalogo)
		registro = ''
		
		for i in range(0, num):
			livro = catalogo[i]
			registro += livro.strLivro()
		
		return registro


