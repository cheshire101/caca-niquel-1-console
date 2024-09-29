import random

# Inicializando os valores aleatórios
valor1 = random.randint(1, 3)
valor2 = random.randint(1, 3)
valor3 = random.randint(1, 3)

# Funções para verificar os valores
def verifica():
    print("Todos os valores são exatamente iguais!")
    print(f"n1: {n1} e random {valor1}")
    print(f"n2: {n2} e random {valor2}")
    print(f"n3: {n3} e random {valor3}")

def verificaValor1():
    print("Apenas o primeiro valor é igual!")
    print(f"n1: {n1} e random {valor1}")
    print(f"n2: {n2} e random {valor2}")
    print(f"n3: {n3} e random {valor3}")

def verificaValor2():
    print("Dois valores são iguais!")
    print(f"n1: {n1} e random {valor1}")
    print(f"n2: {n2} e random {valor2}")
    print(f"n3: {n3} e random {valor3}")

def verificaValor3():
    print("Nenhum valor é igual!")
    print(f"n1: {n1} e random {valor1}")
    print(f"n2: {n2} e random {valor2}")
    print(f"n3: {n3} e random {valor3}")

# Coletando os valores do usuário
n1 = int(input('Qual valor escolherá?: '))
n2 = int(input('Qual valor escolherá? segundo: '))
n3 = int(input('Qual valor escolherá? terceiro: '))

# Verificando os valores com condições corrigidas
if n1 == valor1 and n2 == valor2 and n3 == valor3:
    verifica()
elif n1 == valor1 and n2 == valor2:
    verificaValor2()
elif n1 == valor1:
    verificaValor1()
else:
    verificaValor3()
