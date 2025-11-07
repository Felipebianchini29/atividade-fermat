import math

def f(x):
    try:
        return x**3 - 5 * math.cos(x)
    except ValueError:
        return None
    except Exception as e:
        return None

def metodo_bissecao(a, b, precisao):
    fa = f(a)
    fb = f(b)
    
    if fa is None or fb is None:
        print("Não foi possível calcular a função nos pontos iniciais.")
        return None

    if fa * fb >= 0:
        print(f"\nErro: f(a) e f(b) não possuem sinais opostos.")
        print(f"O Teorema do Valor Intermediário não garante uma raiz neste intervalo.")
        return None

    iteracoes = 0
    while (b - a) >= precisao:
        iteracoes += 1
        
        m = (a + b) / 2
        fm = f(m)
        
        if fm is None:
            return None

        if abs(fm) < precisao:
            return m

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    return (a + b) / 2

PRECISAO_FIXA = 0.0001 

print("Encontrar Raiz pelo Teorema do Valor Intermediário (Método da Bisseção)")
print("-" * 50)
print(f"Função definida no código: f(x) = x^3 - 5*cos(x)")
print(f"Precisão (Erro Máximo) definida: {PRECISAO_FIXA}")
print("-" * 50)

try:
    a = float(input("Digite a primeira estimativa inicial (a): "))
    b = float(input("Digite a segunda estimativa inicial (b): "))

    if a > b:
        a, b = b, a

    print(f"\nCalculando a raiz no intervalo [{a}, {b}]...")
    
    raiz_encontrada = metodo_bissecao(a, b, PRECISAO_FIXA)

    if raiz_encontrada is not None:
        valor_f_na_raiz = f(raiz_encontrada)
        print("\n" + "=" * 50)
        print(f"  RAIZ APROXIMADA ENCONTRADA: {raiz_encontrada:.6f}")
        print(f"  Valor de f(x) na raiz:     {valor_f_na_raiz:.8f}")
        print("=" * 50)
    else:
        print("\nNão foi possível encontrar a raiz com os dados fornecidos.")

except ValueError:
    print("\nErro: Entrada inválida. Por favor, digite apenas números.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")