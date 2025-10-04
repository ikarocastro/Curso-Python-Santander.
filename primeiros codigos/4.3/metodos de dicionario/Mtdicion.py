#Os dicionários em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

'''keys(): retorna uma visualização de todas as chaves do dicionário.
values(): retorna uma visualização de todos os valores do dicionário.
items(): retorna uma visualização de todos os pares chave-valor do dicionário.
update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.'''

meu_dicionario = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
print(meu_dicionario.keys())    # Imprime dict_keys(['nome', 'idade', 'cidade'])
print(meu_dicionario.values())  # Imprime dict_values(['Ana', 25, 'São Paulo'])
print(meu_dicionario.items())   # Imprime dict_items([('nome', 'Ana'), ('idade', 25), ('cidade', 'São Paulo')])
outro_dicionario = {"profissão": "Engenheira", "idade": 26}
meu_dicionario.update(outro_dicionario)
print(meu_dicionario)  # Imprime {'nome': 'Ana', 'idade': 26, 'cidade': 'São Paulo', 'profissão': 'Engenheira'}

#Exemplo

'''pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}'''