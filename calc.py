def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Erro: Não é possível dividir por zero!")
    return a / b

def percentagem(a, b):
    return (a * b) / 100  # Calcula a percentagem: (a * b) / 100

def percentagem(a, b):
    if a < 0 or b < 0:
        raise ValueError("Erro: Percentagem não aceita valores negativos!")
    return (a * b) / 100
