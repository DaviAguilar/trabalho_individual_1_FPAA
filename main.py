# main.py
# Implementação do Algoritmo de Karatsuba para multiplicação eficiente

def karatsuba(x, y):
    """
    Função que implementa o algoritmo de Karatsuba para multiplicar dois números inteiros.
    Args:
        x (int): Primeiro número
        y (int): Segundo número
    Returns:
        int: Resultado da multiplicação
    """
    print(f"Karatsuba chamado com x = {x}, y = {y}")

    # Caso base: se os números tiverem menos de 2 dígitos, usar multiplicação direta
    if x < 10 or y < 10:
        print(f"Multiplicação direta: {x} * {y} = {x * y}")
        return x * y

    # Converte os números para strings para facilitar a divisão em partes
    x_str = str(x)
    y_str = str(y)

    # Garante que ambos os números tenham o mesmo comprimento preenchendo com zeros à esquerda
    max_length = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_length)
    y_str = y_str.zfill(max_length)

    # Se o comprimento for ímpar, adiciona um zero à esquerda para facilitar a divisão
    if max_length % 2 != 0:
        x_str = "0" + x_str
        y_str = "0" + y_str
        max_length += 1

    # Calcula o ponto médio para dividir os números
    mid = max_length // 2

    # Divide os números em duas partes
    a = int(x_str[:mid])  # Parte alta de x
    b = int(x_str[mid:])  # Parte baixa de x
    c = int(y_str[:mid])  # Parte alta de y
    d = int(y_str[mid:])  # Parte baixa de y

    print(f"Divisão: x = {x_str} -> a = {a}, b = {b}; y = {y_str} -> c = {c}, d = {d}")

    # Passos recursivos do algoritmo de Karatsuba
    # Passo 1: a * c
    ac = karatsuba(a, c)
    # Passo 2: b * d
    bd = karatsuba(b, d)
    # Passo 3: (a + b) * (c + d)
    ab_cd = karatsuba(a + b, c + d)
    # Passo 4: (a + b)(c + d) - ac - bd
    ad_bc = ab_cd - ac - bd

    print(f"Resultados intermediários: ac = {ac}, bd = {bd}, (a+b)(c+d) = {ab_cd}, ad+bc = {ad_bc}")

    # Combina os resultados
    # Resultado final = (ac * 10^n) + (ad + bc) * 10^(n/2) + bd
    result = (ac * 10 ** max_length) + (ad_bc * 10 ** mid) + bd

    print(f"Resultado final para x = {x}, y = {y}: {result}")
    return result


def main():
    """
    Função principal para testar a implementação do algoritmo de Karatsuba.
    """
    # Exemplos de teste
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Calcula o resultado usando o algoritmo de Karatsuba
    resultado_karatsuba = karatsuba(num1, num2)
    # Calcula o resultado usando multiplicação direta para verificação
    resultado_direto = num1 * num2

    # Exibe os resultados
    print(f"Multiplicação de {num1} x {num2}:")
    print(f"Resultado com Karatsuba: {resultado_karatsuba}")
    print(f"Resultado direto (verificação): {resultado_direto}")
    print(f"Correto? {resultado_karatsuba == resultado_direto}")


if __name__ == "__main__":
    main()