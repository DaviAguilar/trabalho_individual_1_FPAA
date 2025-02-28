# main.py
# Implementação otimizada do Algoritmo de Karatsuba para multiplicação eficiente

def num_digits(n):
    """Calcula o número de dígitos de um número inteiro."""
    if n == 0:
        return 1
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits

def karatsuba(x, y):
    """
    Função que implementa o algoritmo de Karatsuba usando operações matemáticas.
    Args:
        x (int): Primeiro número
        y (int): Segundo número
    Returns:
        int: Resultado da multiplicação
    """
    # Caso base: se um dos números for pequeno, usa multiplicação direta
    if x < 10 or y < 10:
        return x * y

    # Calcula o número de dígitos (baseado no maior número)
    n = max(num_digits(x), num_digits(y))
    if n % 2 != 0:
        n += 1  # Garante que n seja par para divisão simétrica

    # Calcula a potência de 10 para divisão (metade dos dígitos)
    half = n // 2
    power = 10 ** half

    # Divide os números em partes usando operações aritméticas
    a = x // power  # Parte alta de x
    b = x % power   # Parte baixa de x
    c = y // power  # Parte alta de y
    d = y % power   # Parte baixa de y

    print(f"Dividindo {x} e {y} em partes: a={a}, b={b}, c={c}, d={d}")

    # Passos recursivos do algoritmo de Karatsuba
    ac = karatsuba(a, c)          # Passo 1: a * c
    bd = karatsuba(b, d)          # Passo 2: b * d
    ab_cd = karatsuba(a + b, c + d)  # Passo 3: (a + b) * (c + d)
    ad_bc = ab_cd - ac - bd       # Passo 4: (a + b)(c + d) - ac - bd

    print(f"Resultados intermediários: ac={ac}, bd={bd}, ab_cd={ab_cd}, ad_bc={ad_bc}")

    # Combina os resultados
    result = (ac * 10 ** n) + (ad_bc * 10 ** half) + bd
    return result

def main():
    """Função principal para testar a implementação do algoritmo de Karatsuba."""
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Calcula o resultado usando Karatsuba e multiplicação direta
    resultado_karatsuba = karatsuba(num1, num2)
    resultado_direto = num1 * num2

    # Exibe os resultados
    print(f"Multiplicação de {num1} x {num2}:")
    print(f"Resultado com Karatsuba: {resultado_karatsuba}")
    print(f"Resultado direto (verificação): {resultado_direto}")
    print("Correto?", "Sim" if resultado_karatsuba == resultado_direto else "Não")

if __name__ == "__main__":
    main()