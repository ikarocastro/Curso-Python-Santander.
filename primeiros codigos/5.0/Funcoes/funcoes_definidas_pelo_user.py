def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("Media:", calcular_media(10, 20, 30, 40))

def somar_3(x):
        return x + 3

somar = lambda x: x + 3

print("Somando com o numero 3:", somar(5))