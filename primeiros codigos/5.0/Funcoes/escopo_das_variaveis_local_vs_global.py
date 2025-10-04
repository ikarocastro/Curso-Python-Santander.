#As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.

def função():
    
    print(variavel_local)

variavel_local = 10
variavel_global = 20

def função2():
    print(variavel_global)

função()
função2()
print(variavel_global)
print(variavel_local)