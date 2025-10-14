#Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

"""Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura ("r"). Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines()"""

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#Neste exemplo, o arquivo "dados.txt" é aberto em modo de leitura utilizando open(). Depois, todo o conteúdo do arquivo é lido utilizando o método read() e armazenado na variável conteudo. Finalmente, o conteúdo é mostrado na tela e o arquivo é fechado utilizando o método close().

 