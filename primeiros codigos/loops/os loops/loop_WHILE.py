#O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte:

"""while condição:

    # Bloco de código a repetir
    instruções"""

#Exemplo 1: Contando de 1 a 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
"""Neste exemplo, o loop while continua a executar o bloco de código enquanto a variável contador for menor ou igual a 5. A cada iteração, o valor de contador é incrementado em 1, e o valor atual é impresso. Quando contador se torna 6, a condição deixa de ser verdadeira, e o loop termina.""" #Ou seja 5 + 1 = 6, que é falso.

"""É importante ter cuidado ao usar o loop while, pois, se a condição nunca se tornar falsa, o loop será executado indefinidamente, o que é conhecido como um loop infinito.""" #para evitar isso, certifique-se de que a condição eventualmente se tornará falsa dentro do bloco de código do loop.


