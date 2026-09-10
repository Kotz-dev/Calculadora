

def soma(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtracao(a, b):
    """Retorna a subtração de a e b."""
    return a - b


def multiplicacao(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b


def formatar_resultado(a, b, simbolo, resultado):
    """Formata a mensagem de resultado de uma operação."""
    return f"Resultado: {a} {simbolo} {b} = {resultado}"


def main():
    print("Bem-vindo à Calculadora!")
    print(formatar_resultado(2, 3, "+", soma(2, 3)))
    print(formatar_resultado(5, 3, "-", subtracao(5, 3)))
    print(formatar_resultado(4, 3, "*", multiplicacao(4, 3)))


if __name__ == "__main__":
    main()
