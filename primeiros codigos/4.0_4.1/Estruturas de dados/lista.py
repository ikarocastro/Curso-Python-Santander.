#Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma lista podem ser de diferentes tipos de dados e são encerrados entre colchetes [], separados por vírgulas.

#Criando uma lista
lista = ["maça", "banana", "cereja"]

#Acessando elementos da lista
#print(frutas[0])  # Imprime "maçã"
#print(frutas[1])  # Imprime "banana"
#print(frutas[2])  # Imprime "laranja

"""As listas em Python têm vários métodos incorporados que nos permitem manipular e modificar os elementos da lista. Alguns métodos comuns são:

append(elemento): adiciona um elemento ao final da lista.
insert(indice, elemento): insere um elemento em uma posição específica da lista.
remove(elemento): remove a primeira ocorrência de um elemento na lista.
pop(indice): remove e retorna o elemento em uma posição específica da lista.
sort(): ordena os elementos da lista em ordem ascendente.
reverse(): inverte a ordem dos elementos na lista."""

frutas = ["maçã", "banana", "laranja"]


frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]


fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"


frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]