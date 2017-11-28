import requests
import json
import pandas as pd
import numpy as np

def coleta():
    print(url)
    try:
        id = resposta["id"]
        print(id)
    except:
        id = 'vazio'
    try:
        cnpj = resposta["cnpj"]
    except:
        try:
            cnpj = resposta['cpf']+' - CPF'
        except:
            cnpj = 'vazio'
    try:
        razaosocial = resposta["razao_social"]
        print(razaosocial)
    except:
        razaosocial = 'vazio'
    # try:
    #     nomefantasia = resposta["nome_fantasia"]
    # except:
    #     nomefantasia = 'vazio'
    # idunidadecadastradora = resposta["id_unidade_cadastradora"]
    # idnaturezajuridica = resposta["id_natureza_juridica"]
    # idramonegocio = resposta["id_ramo_negocio"]
    # idporteempresa = resposta["id_porte_empresa"]
    # logradouro = resposta["logradouro"]
    # bairro = resposta["bairro"]
    # idmunicipio = resposta["id_municipio"]
    # cep = resposta["cep"]
    # ativo = resposta["ativo"]
    # try:
    #     recadastro = resposta["recadastro"]
    # except:
    #     recadastro = "vazio"
    # habilitadolicitar = resposta["habilitado_licitar"]
    # try:
    #     uf = resposta["uf"]
    # except:
    #     uf = "vazio"
    # try:
    #     idcnae = resposta["id_cnae"]
    # except:
    #     idcnae = "vazio"
    records.append((id, cnpj, razaosocial))
    dataframe = pd.DataFrame(records)
    print (dataframe)
    header = ['id', 'cnpj', 'razaosocial']
    dataframe.to_csv('dados.csv', mode='a', columns=header)

urlinit= "http://compras.dados.gov.br//fornecedores/v1/fornecedores.json?uf=DF&offset=0"
requi1 = requests.get(urlinit).json()
requi2 = requi1["_embedded"]["fornecedores"]
# print(requi2)
x = 1

for requi3 in requi2:
    caminho = requi3["_links"]["self"]["href"]
    url = "http://compras.dados.gov.br"+caminho+".json"
    resposta = requests.get(url).json()
    # print(resposta)
    records = []
    coleta()

    # for dados in resposta:



        #

