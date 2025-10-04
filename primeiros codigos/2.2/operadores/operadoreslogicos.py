"""AND (and): devolve True se ambas as condições são verdadeiras.
OR (or): devolve True se ao menos uma das condições é verdadeira.
NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira."""

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False