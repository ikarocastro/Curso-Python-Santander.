pessoa = {"nome": ["Ana"], "idade": [25], "cidade": ["São Paulo"]}
print(pessoa["nome"])  # Imprime ['Ana']
print(pessoa["idade"])  # Imprime [25]
print(pessoa["cidade"])  # Imprime ['São Paulo']

get("chave", valor_padrao)  # Retorna o valor associado à chave ou valor_padrao se a chave não existir
print(pessoa.get("nome", "Chave não encontrada"))  # Imprime ['Ana']
