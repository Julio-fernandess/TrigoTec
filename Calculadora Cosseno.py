#A função math.radians é usada para converter o ângulo de graus para radianos, pois a função math.cos espera um ângulo em radianos como argumento.
A função math.cos calcula o cosseno do ângulo.
O resultado é impresso com quatro casas decimais usando a formatação :.4f.

import math

# Lê o valor do ângulo em graus
ang = int(input('Ângulo: '))

# Converte o ângulo de graus para radianos
rad = math.radians(ang)

# Calcula o cosseno do ângulo
cosseno = math.cos(rad)

# Imprime o resultado
print(f'O cosseno do ângulo {ang} é {cosseno:.4f}')
