#Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

"""
add(elemento): adiciona um elemento ao conjunto.
remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
clear(): remove todos os elementos do conjunto.
"""

frutas = {"maçã", "banana", "laranja"}

frutas.add("uva")
print(frutas)  # Imprime {'maçã', 'banana', 'laranja', 'uva'}

frutas.remove("banana")
print(frutas)  # Imprime {'maçã', 'laranja', 'uva'}

frutas.discard("kiwi")  # Não faz nada, pois "kiwi" não está no conjunto
print(frutas)  # Imprime {'maçã', 'laranja', 'uva'}

frutas.clear()
print(frutas)  # Imprime set()  # Conjunto vazio

'''Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().'''