"""Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas. Isso é útil quando deseja lidar com situações específicas do seu programa.

Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses."""

condicao = True
def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro") #verifica-se uma condição e, se for satisfeita, gera-se uma exceção utilizando a declaração raise. Em vez de criar uma classe personalizada, utiliza-se diretamente a classe base Exception para gerar a exceção.


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")

"""Depois, utiliza-se um bloco try-except para capturar e lidar com a exceção. A variável e é utilizada para acessar a descrição do erro fornecida ao gerar a exceção.

O tratamento de erros e exceções é uma parte fundamental da programação em Python. Permite lidar com situações inesperadas de maneira controlada e evitar que seu programa trave ou pare abruptamente.

Quando ocorre um erro no seu código, o Python gera uma exceção. Ao utilizar blocos try-except, você pode capturar e lidar com essas exceções de maneira adequada. Pode especificar diferentes blocos except para lidar com diferentes tipos de exceções e realizar ações específicas em cada caso."""

#Considere os possíveis erros que podem ocorrer no seu código e utilize o tratamento de exceções adequado para lidar com eles de maneira apropriada. Isso tornará seus programas mais robustos e confiáveis