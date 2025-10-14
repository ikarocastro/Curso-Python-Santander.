#Em Python, a entrada e saída de dados nos permite interagir com o usuário e manipular arquivos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos externos.

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")


print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")

#Neste exemplo, solicita-se ao usuário que insira seu nome e idade utilizando a função input(). Os valores inseridos são armazenados nas variáveis nome e idade, respectivamente. Em seguida, essas variáveis são utilizadas para mostrar uma saudação personalizada na tela.

"""A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita utilizando funções como int() ou float()."""

