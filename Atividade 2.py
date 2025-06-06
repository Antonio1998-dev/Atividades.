def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

def maior_numero(num1, num2):
    return max(num1, num2)

def calcular_media(numeros):
    return sum(numeros) / len(numeros) if numeros else 0


def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
