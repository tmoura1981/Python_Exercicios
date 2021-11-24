import math
angulo = float(input('\033[1;31mInforme um ângulo qualquer: \033[m'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'\033[1;33mO ângulo de {angulo} tem o seno de {seno:.2f}, o cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}.')

'''As medidas trigonométricas seno, cosseno, tangente, etc, 
são informadas em radianos no Python. 
Sendo assim,
deve-se, colocar como .radians os valores dos ângulos informados que estão como graus centígrados.'''