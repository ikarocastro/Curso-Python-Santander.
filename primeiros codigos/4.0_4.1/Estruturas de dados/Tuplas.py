#Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.

#Criação e acesso

ponto = (3, 4)

#Para acessar os elementos de uma tupla, utilize o índice do elemento entre colchetes, similar às listas:

print(ponto[0])  # Imprime 3
print(ponto[1])  # Imprime 4
#ponto[0] = 5  # Isso gerará um erro, pois tuplas são imutáveis

#Ao contrário das listas, as tuplas são imutáveis, o que significa que não podem ser modificadas uma vez criadas. Não se pode adicionar, eliminar ou alterar elementos em uma tupla existente.

#As tuplas são úteis quando você precisa armazenar uma coleção de elementos que não devem ser modificados, como coordenadas ou dados de configuração.
