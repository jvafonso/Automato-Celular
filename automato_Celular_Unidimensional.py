import numpy as np
import matplotlib.pyplot as plt

# Função que converte um numero inteiro para sua representação binaria (0 - 255)
def converte_binario(numero) :
    binario = bin(numero)
    binario = binario[2:]
    if len(binario) < 8:
        zero = [0]*(8-len(binario))
        binario = zero + list(binario)
    return list(binario)

# Inicio do script de AC
numero_celulas = int(input('Entre com o numero de celulas do automato: '))
MAX = 2*numero_celulas
g = np.zeros(numero_celulas)
ng = np.zeros(numero_celulas)
regra = int(input('Entre com o numero da regra: '))
codigo = converte_binario(regra)

# Matriz em que cada linha armazena uma geração do autômato
matriz_evolucao = np.zeros((MAX, len(g)))

# Define a geração inicial
g[len(g)//2] = 1

# Laço principal: atualiza as gerações
for i in range(MAX) :
    matriz_evolucao[i,:] = g
    # Percorre células da geração atual
    for j in range(len(g)) :
        if (g[j-1] == 0 and g[j] == 0 and g[(j+1) % len(g)] == 0):
            ng[j] = int(codigo[7])
        elif (g[j-1] == 0 and g[j] == 0 and g[(j+1) % len(g)] == 1):
            ng[j] = int(codigo[6])
        elif (g[j-1] == 0 and g[j] == 1 and g[(j+1) % len(g)] == 0):
            ng[j] = int(codigo[5])
        elif (g[j-1] == 0 and g[j] == 1 and g[(j+1) % len(g)] == 1):
            ng[j] = int(codigo[4])
        elif (g[j-1] == 1 and g[j] == 0 and g[(j+1) % len(g)] == 0):
            ng[j] = int(codigo[3])
        elif (g[j-1] == 1 and g[j] == 0 and g[(j+1) % len(g)] == 1):
            ng[j] = int(codigo[2])
        elif (g[j-1] == 1 and g[j] == 1 and g[(j+1) % len(g)] == 0):
            ng[j] = int(codigo[1])
        elif (g[j-1] == 1 and g[j] == 1 and g[(j+1) % len(g)] == 1):
            ng[j] = int(codigo[0])

    g = ng.copy() # se não usar o copy ambos os vetores tornam-se o mesmo

# plota a matriz resultante como imagem
plt.figure(1)
plt.axis('off')
plt.imshow(matriz_evolucao, cmap='gray')
plt.savefig('Automato_Celular.png', dpi=300)
plt.show()

    