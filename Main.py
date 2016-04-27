#! /usr/bin/python
# -*- coding: utf-8 -*-

from Catalogo import Catalogo
from Livro import Livro
from Data import Data

bib = Catalogo()
bib.ler()
bib.atualizar()

arquivo = open('saida.txt', 'w')

arquivo.write('Lista de Livros Ordenada Crescentemente por Codigo:\n\n')
bib.sort(Livro.cmpCode)
arquivo.write(bib.registro())

arquivo.write('Lista de Livros Ordenada Decrescentemente por Titulo:\n\n')
bib.sort(Livro.cmpTitle)
arquivo.write(bib.registro())

arquivo.write('Lista de Livros Ordenada Crescentemente por Autor:\n\n')
bib.sort(Livro.cmpAuthor)
arquivo.write(bib.registro())

arquivo.write('Lista de Livros Ordenada Decrescentemente por Data de Publicacao:\n\n')
bib.sort(Livro.cmpData)
arquivo.write(bib.registro())

arquivo.close()

arquivo = open('catalog.txt', 'w')
bib.sort(Livro.cmpCode)
arquivo.write(bib.registro())
arquivo.close()

