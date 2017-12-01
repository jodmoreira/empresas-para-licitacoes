# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import numpy as np


def dadoEmpresa(requi2, records):
	for requi3 in requi2:
		caminho = requi3["_links"]["self"]["href"]
		url = "http://compras.dados.gov.br"+caminho+".json"
		resposta = requests.get(url).json()
		coleta(resposta, records)

def coleta(resposta, records):
	try:
		id = (resposta["id"])
		
	except:
		id = "vazio"
	print (id)
	try:
		cnpj = resposta["cnpj"]
	except:
		try:
			cnpj = resposta['cpf']+' - CPF'
		except:
			cnpj = "vazio"
	print (cnpj)
	try:
		razaosocial = resposta["razao_social"]
		razaosocial.decode('cp1252').encode('utf-8')
	except:
		razaosocial = 'vazio'
	print (razaosocial)
	escrita(id, cnpj, razaosocial, records)
	

def escrita(id, cnpj, razaosocial, records):
	try:
		records.append((id, cnpj, razaosocial))
		dataframe = pd.DataFrame(records)
		dataframe.to_csv('dados.csv', mode="w", header=["ID", "CNPJ", "Razao Social"])
		try:
			print proxurl
		except:
			print caminho
	except:
		print "FALHA DE ESCRITA"
		try:
			print proxurl
		except:
			print caminho
def paginacao(records, respostaBruto):
	proxurl = "http://compras.dados.gov.br" + respostaBruto["_links"]["next"]["href"]
	print proxurl
	respostaBruto = requests.get(proxurl).json()
	requi2 = respostaBruto["_embedded"]["fornecedores"]
	dadoEmpresa(requi2, records)
	paginacao(records, respostaBruto)
	
urlinit= "http://compras.dados.gov.br//fornecedores/v1/fornecedores.json?uf=DF&offset=0"
requi1 = requests.get(urlinit).json()
requi2 = requi1["_embedded"]["fornecedores"]
records = []

for requi3 in requi2:
	caminho = requi3["_links"]["self"]["href"]
	url = "http://compras.dados.gov.br"+caminho+".json"
	resposta = requests.get(url).json()
	try:
		id = (resposta["id"])
	except:
		id = "vazio"
	print (id)
	try:
		cnpj = resposta["cnpj"]
	except:
		try:
			cnpj = resposta['cpf']+' - CPF'
		except:
			cnpj = "vazio"
	print (cnpj)
	try:
		razaosocial = resposta["razao_social"]
		razaosocial = razaosocial.decode('cp1252').encode('utf-8')
	except:
		razaosocial = 'vazio'
	print (razaosocial)
	escrita(id, cnpj, razaosocial, records)

proxurl = "http://compras.dados.gov.br" + requi1["_links"]["next"]["href"]
print proxurl
respostaBruto = requests.get(proxurl).json()
requi2 = respostaBruto["_embedded"]["fornecedores"]
dadoEmpresa(requi2, records)
paginacao(records, respostaBruto)

