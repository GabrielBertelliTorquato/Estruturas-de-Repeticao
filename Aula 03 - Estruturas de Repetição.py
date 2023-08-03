# 1. Faça um algoritmo que:
# • leia 20 números inteiros;
# • escreva os números que são negativos;
# • escreva a média dos números positivos.

positivo = 0
negativo = 0

for numeros in range (20):
    numeros = int(input('Digite um número: '))
    if numeros <0:
        negativo += 1
    else:
        positivo += 1

print(f'{positivo} números positivos')
print(f'{negativo} números negativos')    

    

 

# 2. Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é
# par ou ímpar.

for i in range(15):
    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0:
        print(numero, 'É um número par')
    else:
        print(numero, 'É um número ímpar')


# 3. Dado um conjunto de valores inteiros positivos, determinar qual o menor e qual o
# maior valor do conjunto. Um número com valor “0” (zero) indica o fim dos dados e
# não deve ser considerado.

menor = maior = int(input("Digite um valor: "))
while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    if valor < menor:
        menor = valor
    elif valor > maior:
        maior = valor
print(f"O menor valor do conjunto é {menor} e o maior valor é {maior}.")

# 4. Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos
# números ímpares entre 1 e 100.

soma_pares = 0
soma_impares = 0

for i in range(1, 101):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print("A soma dos números pares é:", soma_pares)
print("A soma dos números ímpares é:", soma_impares)

# 5. Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das
# alturas.

soma_altura = 0

for i in range (20):
     altura = float(input('Digite a altura: '))
     soma_altura += altura
    
media_alturas = soma_altura / 20    

print(f'A média de altura é {media_alturas}')

# 6. Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são
# negativos.

n = int(input("Digite a quantidade de valores a serem lidos: "))
count_negativos = 0

for i in range(n):
    valor = int(input("Digite o valor {}: ".format(i+1)))
    if valor < 0:
        count_negativos += 1

print("A quantidade de valores negativos é:", count_negativos)

# 7. Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a
# caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”.
# Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui.

tinta = float(input("Digite a quantidade de tinta na caneta: "))

while tinta >= 0.02:
    print("Enquanto tem tinta a caneta escreve...")
    tinta -= 0.02

# 8. Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de
# inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
# • o número de inscrição e a altura do atleta mais alto;
# • o número de inscrição e a altura do atleta mais baixo;
# • a altura média do grupo de atletas.

n = int(input("Digite o número de atletas: "))

mais_alto = 0
mais_baixo = float('inf')
soma_alturas = 0

for i in range(n):
    inscricao = int(input("Digite o número de inscrição do atleta: "))
    altura = float(input("Digite a altura do atleta em centímetros: "))
    
    if altura > mais_alto:
        mais_alto = altura
        inscricao_mais_alto = inscricao
    
    if altura < mais_baixo:
        mais_baixo = altura
        inscricao_mais_baixo = inscricao
    
    soma_alturas += altura

media_alturas = soma_alturas / n

print("Atleta mais alto: número de inscrição =", inscricao_mais_alto, "altura =", mais_alto, "cm")
print("Atleta mais baixo: número de inscrição =", inscricao_mais_baixo, "altura =", mais_baixo, "cm")
print("Altura média do grupo: ", media_alturas, "cm")

#9.

for x in range(10, 51):
    x /= 10.0
    y = (3 + 2*x + 6*x**2) / (1 + 9*x + 16*x**2)
    print("x =", x, "| y =", y)


# 10. Construir um algoritmo que calcule o fatorial de um número N.

n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("Número inválido. Digite um número inteiro positivo.")
else:
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    print("O fatorial de", n, "é", fatorial)

# 11. Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos: 1+2+3+4+...+100

soma = 0
for i in range(1, 101):
    soma += i
print("A soma da série de 100 termos é:", soma)

# 12.

soma = 0

for i in range(1, 101):
    termo = 1 / i
    soma += termo

print("A soma da série é:", soma)


# 13.

N = int(input("Digite o valor de N: "))
soma = 0

for i in range(1, N+1):
    termo = i / (N - i + 1)
    soma += termo

print("O valor de S é:", soma)


# 14.

soma = 0

for i in range(51):
    termo = ((-1) ** i) * (1 / ((2 * i + 1) ** 3))
    soma += termo

aprox_pi = (soma * 32) ** (1 / 3)

print("O valor aproximado de π é:", aprox_pi)

# 15.

soma = 0

for i in range(20):
    numerador = 100 - i
    fatorial = 1

    for j in range(i + 1):
        if j > 0:
            fatorial *= j

    termo = numerador / fatorial
    soma += termo

print("A soma dos 20 primeiros termos da série é:", soma)


# 16.

import math

def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

x = float(input("Digite o valor de x: "))

resultado_ex = 0
for i in range(30):
    termo = math.pow(x, i) / calcular_fatorial(i)
    resultado_ex += termo

print("O valor de e^x é:", resultado_ex)


# 17. Foi feita uma pesquisa de audiência de canal de TV em n casas de um determinado
# bairro de Joinville, em um certo dia do mês. Na pesquisa foi utilizado um coletor de
# dados portátil. Para cada casa visitada, foi fornecido o número do canal (4, 5, 9, 12) e
# o número de pessoas que estavam assistindo a TV naquele horário, considerando que
# em cada casa só existia uma televisão. Em casas onde a televisão estava desligada, foi
# registrado zero para o número do canal e para o número de pessoas. Faça um
# algoritmo que calcule e escreva, para cada emissora, o percentual de audiência.

total_canal_4 = 0
total_canal_5 = 0
total_canal_9 = 0
total_canal_12 = 0

n = int(input("Digite o número de casas a serem visitadas: "))

for i in range(1, n+1):
    canal = int(input("Digite o número do canal (4, 5, 9 ou 12) da casa {}: ".format(i)))
    if canal == 4:
        total_canal_4 += int(input("Digite o número de pessoas assistindo o canal {}: ".format(canal)))
    elif canal == 5:
        total_canal_5 += int(input("Digite o número de pessoas assistindo o canal {}: ".format(canal)))
    elif canal == 9:
        total_canal_9 += int(input("Digite o número de pessoas assistindo o canal {}: ".format(canal)))
    elif canal == 12:
        total_canal_12 += int(input("Digite o número de pessoas assistindo o canal {}: ".format(canal)))
    else:
        print("Canal inválido.")

total_pessoas = total_canal_4 + total_canal_5 + total_canal_9 + total_canal_12
if total_pessoas == 0:
    print("Não houve audiência nesse dia.")
else:
    print("Percentual de audiência por canal:")
    print("Canal 4:", (total_canal_4 / total_pessoas) * 100, "%")
    print("Canal 5:", (total_canal_5 / total_pessoas) * 100, "%")
    print("Canal 9:", (total_canal_9 / total_pessoas) * 100, "%")
    print("Canal 12:", (total_canal_12 / total_pessoas) * 100, "%")

# 18. Uma companhia de teatro planeja dar uma série de espetáculos. A direção calcula que,
# a R$ 5,00 o ingresso, serão vendidos 120 ingressos. Com a diminuição de R$ 0,50 no
# preço dos ingressos, espera-se que haja um aumento de 26 ingressos vendidos. As
# despesas estão estipuladas em R$ 200,00 independente do número de ingressos
# vendidos. Faça um algoritmo que escreva uma tabela contendo o preço do ingresso, o
# número de ingressos e o lucro esperado em função do preço do ingresso, fazendo-se
# variar este preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em R$ 0,50. Escreva também o lucro
# máximo esperado, o preço e o número de ingressos correspondentes.

preco_ingresso = 5.00
lucro_maximo = 0
preco_lucro_maximo = 0
ingressos_lucro_maximo = 0

print("Preço do ingresso | Número de ingressos | Lucro esperado")

while preco_ingresso >= 1.00:
    if preco_ingresso == 5.00:
        ingressos = 120
    else:
        ingressos = 120 + (26 * (5.00 - preco_ingresso) / 0.50)
        lucro = (ingressos * preco_ingresso) - 200.00
    
    print("{:.2f}              | {:>2d}                  | {:.2f}".format(preco_ingresso, int(ingressos), lucro))
    
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_lucro_maximo = preco_ingresso
        ingressos_lucro_maximo = int(ingressos)
    
    preco_ingresso -= 0.50

print("\nLucro máximo esperado: R$ {:.2f}".format(lucro_maximo))
print("Preço do ingresso para o lucro máximo: R$ {:.2f}".format(preco_lucro_maximo))
print("Número de ingressos para o lucro máximo: {:d}".format(ingressos_lucro_maximo))

# 19. Faça um algoritmo que leia n números inteiros e escreva, para cada número lido, os
# divisores e quantidade de divisores.
# EXEMPLO: número lido = 12
# divisores = 1, 2, 3, 4, 6, 12

# quantidade divisores = 6

n = int(input("Digite o valor de n: "))

for i in range(n):
    num = int(input("Digite um número inteiro: "))
    divisores = []
    for j in range(1, num+1):
        if num % j == 0:
            divisores.append(j)
    qtde_divisores = len(divisores)
    print(f"Número: {num}\nDivisores: {divisores}\nQuantidade de divisores: {qtde_divisores}\n")

#20. 

total_biscoitos_quebrados = 0

for dia in range(1, 6):
    biscoitos_quebrados = 1  

    for hora in range(1, 17):
        total_biscoitos_quebrados += biscoitos_quebrados
        biscoitos_quebrados *= 3

    print(f"No final do dia {dia}, a quantidade de biscoitos quebrados é: {total_biscoitos_quebrados}")
    total_biscoitos_quebrados = 0 

# 21. Uma turma tem 50 alunos. Faça um algoritmo que:
# • leia para cada aluno o seu nome e idade;
# • escreva os nomes dos alunos que tem 18 anos;
# • escreva a quantidade de alunos que tem idade acima de 20 anos.

alunos_18_anos = []  
qtd_alunos_acima_20_anos = 0  
for i in range(1, 51):  
    nome = input(f"Informe o nome do {i}º aluno: ")
    idade = int(input(f"Informe a idade do {i}º aluno: "))
    
    if idade == 18:
        alunos_18_anos.append(nome)
    
    if idade > 20:
        qtd_alunos_acima_20_anos += 1

print("Alunos com 18 anos:")
for nome in alunos_18_anos:
    print(nome)

print(f"Quantidade de alunos com mais de 20 anos: {qtd_alunos_acima_20_anos}")

# 22. Faça um algoritmo que:
# • leia, para n pessoas, a altura e o sexo (sexo = 'M' ou sexo = 'm' para masculino e
# sexo = 'F' ou sexo = 'f' para feminino);
# • escreva a média da altura das mulheres;
# • escreva a média da altura da turma.

n = int(input("Informe a quantidade de pessoas: "))

soma_alturas_mulheres = 0  
qtd_mulheres = 0 
soma_alturas_turma = 0 

for i in range(1, n+1):
    altura = float(input(f"Informe a altura da {i}ª pessoa: "))
    sexo = input(f"Informe o sexo da {i}ª pessoa (M/F): ")
    
    soma_alturas_turma += altura
    
    if sexo.upper() == 'F':
        soma_alturas_mulheres += altura
        qtd_mulheres += 1

media_alturas_mulheres = soma_alturas_mulheres / qtd_mulheres
media_alturas_turma = soma_alturas_turma / n

print(f"Média da altura das mulheres: {media_alturas_mulheres:.2f} m")
print(f"Média da altura da turma: {media_alturas_turma:.2f} m")

# 23. Uma loja de departamentos oferece para seus clientes um determinado desconto de
# acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra
# seja maior que R$ 500,00 e de 15% caso seja menor ou igual. Faça um algoritmo que
# leia, para cada cliente, nome, endereço e valor da compra e escreva o total a pagar.
# Um nome de cliente igual a ULTIMO indica o fim da entrada de dados.

total_vendas = 0

while True:
    nome = input("Digite o nome do cliente: ")
    if nome == "ULTIMO":
        break
    
    endereco = input("Digite o endereço do cliente: ")
    
    valor_compra = float(input("Digite o valor da compra: "))
    if valor_compra > 500:
        desconto = valor_compra * 0.2
    else:
        desconto = valor_compra * 0.15
    
    total_pagar = valor_compra - desconto
    total_vendas += total_pagar
    
    print(f"Cliente: {nome}")
    print(f"Endereço: {endereco}")
    print(f"Valor da compra: R$ {valor_compra:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total a pagar: R$ {total_pagar:.2f}\n")

print(f"Total de vendas: R$ {total_vendas:.2f}")

# 24. Faça um algoritmo que leia valores, sendo que cada valor representa a idade de uma
# pessoa. Calcule e escreva a idade média do grupo de pessoas. Só devem ser
# computados no cálculo valores maiores do que zero. O algoritmo deve apresentar ao
# usuário a seguinte mensagem:
# deseja digitar mais um valor: s (SIM) / n (NAO)?,
# antes de prosseguir com a entrada de dados.

idades = []  

while True:
    idade = int(input("Digite a idade (0 para encerrar): "))
    
    if idade == 0:
        break  
    
    if idade > 0:  
        idades.append(idade)  
        
    continuar = input("Deseja digitar mais um valor? (s/n): ")
    if continuar.lower() == "n":
        break  

if len(idades) > 0:
    media = sum(idades) / len(idades)
    print(f"A idade média do grupo é {media:.2f}")
else:
    print("Não foram digitadas idades válidas.")

# 25. Um hotel cobra R$ 50,00 de diária por hóspede e mais uma taxa de serviços. A taxa de
# serviços é de:
# • R$ 7,50 por diária, caso o número de diárias seja menor que 15;
# • R$ 6,50 por diária, caso o número de diárias seja igual a 15;
# • R$ 5,00 por diária, caso o número de diárias seja maior que 15.

# Faça um algoritmo que apresente as seguintes opções ao recepcionista:
# 1. encerrar a conta de um hóspede
# 2. verificar número de contas encerradas
# 3. finalizar a execução

# Caso a opção escolhida seja a primeira, leia o nome e o número de diárias do hóspede
# e escreva o nome e total a ser pago. Caso a opção escolhida seja a segunda, informe o
# número de hóspedes que deixaram o hotel (número de contas encerradas).

contas_encerradas = 0  

while True:
    print("Escolha uma opção:")
    print("1. Encerrar a conta de um hóspede")
    print("2. Verificar número de contas encerradas")
    print("3. Finalizar a execução")
    
    opcao = int(input("Opção: "))
    
    if opcao == 1:
        nome = input("Digite o nome do hóspede: ")
        num_diarias = int(input("Digite o número de diárias do hóspede: "))
        
        if num_diarias < 15:
            taxa_servicos = 7.50
        elif num_diarias == 15:
            taxa_servicos = 6.50
        else:
            taxa_servicos = 5.00
        
        total_pagar = (50.00 * num_diarias) + taxa_servicos
        
        print(f"Hóspede: {nome}")
        print(f"Total a ser pago: R$ {total_pagar:.2f}")
        
        contas_encerradas += 1
        
    elif opcao == 2:
        print(f"Número de contas encerradas: {contas_encerradas}")
        
    elif opcao == 3:
        break  
        
    else:
        print("Opção inválida. Digite novamente.")

# 26. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a sua massa inicial em Kg, faça um algoritmo que determine o tempo necessário
# para que essa massa se torne menor que 0,5 gramas. Escreva a massa inicial, a massa
# final e o tempo.

massa_inicial = float(input("Digite a massa inicial em Kg: "))

massa_final = 0.0005  
tempo = 0  

while massa_inicial >= massa_final:
    massa_inicial /= 2  
    tempo += 50

print("Resultados:")
print(f"Massa inicial: {massa_inicial:.6f} Kg")
print(f"Massa final: {massa_final} Kg")
print(f"Tempo necessário: {tempo} segundos")

# 27. Um motorista acaba de voltar de um feriado prolongado. Antes de sair de viagem e
# imediatamente após retornar, o motorista encheu o tanque do veículo e registrou as
# medidas do odômetro. Em cada parada feita durante a viagem, foi registrado o valor
# do odômetro e a quantidade de combustível comprado para reabastecer o veículo
# (suponha que o tanque ficou vazio e foi enchido a cada parada). Faça um algoritmo
# que leia o número total de reabastecimentos feitos (incluindo o primeiro) e os dados
# registrados relativos à compra de combustível. Calcule e escreva:
# a) a quilometragem obtida por litro de combustível entre cada par de paradas
# b) a quilometragem média obtida por litro de combustível em toda a viagem.

odometro_inicial = float(input("Digite a leitura inicial do odômetro: "))
combustivel_inicial = float(input("Digite a quantidade de combustível no tanque: "))

quilometragens = []
litros_totais = combustivel_inicial

n = int(input("Digite o número de paradas feitas: "))
odometro_anterior = odometro_inicial
for i in range(n):
    odometro_atual = float(input(f"Digite a leitura do odômetro na parada {i+1}: "))
    combustivel_comprado = float(input(f"Digite a quantidade de combustível comprado na parada {i+1}: "))
    quilometragem = (odometro_atual - odometro_anterior) / combustivel_comprado
    quilometragens.append(quilometragem)
    litros_totais += combustivel_comprado
    odometro_anterior = odometro_atual

quilometragem_media = (odometro_atual - odometro_inicial) / litros_totais

print("Quilometragem obtida por litro de combustível em cada parada:")
for i, q in enumerate(quilometragens):
    print(f"Parada {i+1}: {q:.2f} km/L")

print(f"Quilometragem média obtida por litro de combustível em toda a viagem: {quilometragem_media:.2f} km/L")

# 28. Em uma disputa de pingue-pongue os pontos são anotados como D, ponto para o
# jogador do lado direito, e E, ponto para o jogador do lado esquerdo da mesa. Faça um
# algoritmo que leia o código do ponto de cada jogada e determine o vencedor. A
# partida encerra quando:
# a) um dos jogadores chegar a 21 pontos e a diferença de pontos entre os jogadores for
# maior ou igual a dois;
# b) o jogador com mais de 21 pontos conseguir uma diferença de dois pontos sobre o
# adversário, caso a primeira condição não seja atendida.

pontos_direita = 0
pontos_esquerda = 0

while True:
    jogada = input("Digite o código da jogada (D/E): ")

    if jogada == "D":
        pontos_direita += 1
    elif jogada == "E":
        pontos_esquerda += 1

    if pontos_direita >= 21 and pontos_direita - pontos_esquerda >= 2:
        print("Jogador da direita venceu!")
        break
    elif pontos_esquerda >= 21 and pontos_esquerda - pontos_direita >= 2:
        print("Jogador da esquerda venceu!")
        break

# 29. Os regulamentos de uma competição de pesca impõem um limite no peso total de
# pesca de um dia. Faça um algoritmo que leia o limite diário (em quilogramas) e então
# leia o peso (em gramas) de cada peixe e escreva o peso total da pesca obtido até
# aquele ponto. Quando o limite diário for excedido escreva uma mensagem e encerre a
# execução do algoritmo. O algoritmo deve ainda apresentar ao usuário a seguinte
# mensagem: informar o peso de mais um peixe: s (SIM) / n (NÃO)? antes de prosseguir
# com a entrada de dados.

limite_diario = float(input("Digite o limite diário de peso de pesca (em quilogramas): "))
peso_total = 0

while True:
    peso_peixe = float(input("Digite o peso do peixe (em gramas): "))
    peso_total += peso_peixe / 1000  

    if peso_total > limite_diario:
        print("Limite diário de peso de pesca excedido!")
        break

    opcao = input("Informar o peso de mais um peixe? (s/N): ")
    if opcao.lower() != 's':
        break

print(f"Peso total da pesca: {peso_total:.2f} kg")

# 30. Foi feita uma pesquisa do consumo mensal de energia elétrica em uma determinada
# cidade. Para cada consumidor, são fornecidos os seguintes dados: número de
# identificação do consumidor, quantidade de kWh consumidos durante o mês, código
# do tipo de consumidor (R - residencial, C - comercial, I - industrial). Faça um algoritmo
# que:
# a) leia o preço do kWh por tipo de consumidor;
# b) leia os dados de n consumidores;
# c) escreva o número de identificação e o total a pagar, para cada consumidor;
# d) escreva a quantidade total de KWh consumida para cada um dos três tipos de
# consumidores;
# e) escreva a quantidade média geral de consumo.

preco_r = float(input("Digite o preço do kWh para consumidores residenciais: "))
preco_c = float(input("Digite o preço do kWh para consumidores comerciais: "))
preco_i = float(input("Digite o preço do kWh para consumidores industriais: "))

consumo_r = 0
valor_r = 0
consumo_c = 0
valor_c = 0
consumo_i = 0
valor_i = 0
quantidade_consumidores = int(input("Digite a quantidade de consumidores: "))

for i in range(quantidade_consumidores):
    identificacao = input(f"Digite a identificação do consumidor {i + 1}: ")
    consumo = float(input(f"Digite o consumo em kWh do consumidor {i + 1}: "))
    codigo = input(f"Digite o código do tipo de consumidor (R, C ou I) do consumidor {i + 1}: ")

    if codigo == "R":
        valor = consumo * preco_r
        consumo_r += consumo
        valor_r += valor
    elif codigo == "C":
        valor = consumo * preco_c
        consumo_c += consumo
        valor_c += valor
    elif codigo == "I":
        valor = consumo * preco_i
        consumo_i += consumo
        valor_i += valor

    print(f"O consumidor {identificacao} deve pagar R$ {valor:.2f}.")

consumo_total = consumo_r + consumo_c + consumo_i
valor_total = valor_r + valor_c + valor_i

print(f"Consumo total de kWh para consumidores residenciais: {consumo_r:.2f}.")
print(f"Consumo total de kWh para consumidores comerciais: {consumo_c:.2f}.")
print(f"Consumo total de kWh para consumidores industriais: {consumo_i:.2f}.")
print(f"Quantidade média geral de consumo: {consumo_total / quantidade_consumidores:.2f}.")
