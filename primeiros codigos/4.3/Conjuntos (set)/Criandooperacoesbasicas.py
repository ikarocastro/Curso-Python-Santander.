#Para criar um conjunto, utilize chaves ou a função set():

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = set([4, 5, 6, 7, 8])
conjunto3 = {"maça","banana","laranja"} 
print(conjunto1)  # Imprime {1, 2, 3, 4, 5}
print(conjunto2)  # Imprime {4, 5, 6, 7, 8}
print(conjunto3)  # Imprime {'maça', 'banana', 'laranja'}

#Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).

print("Operações com conjuntos:\n")

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
'''Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().'''


