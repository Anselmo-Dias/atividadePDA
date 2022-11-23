# 4.1 Os alunos do PdA estão sendo avaliados, para passar para o próximo ciclo, deverão  tirar 7 na média.

# -Se o aluno tirar maior ou igual a 7 ele está aprovado. (>=7)
# -Se o aluno tiver nota 6 e for participativo, irá para recuperação. (==6)
# -Senão, será reprovado. (else {print("reprovado")})
# Faça um algoritmo que auxilie a avaliar a nota dos alunos.

# media = 7
# nota_do_aluno = int(input("Qual foi a sua nota? "))


# if nota_do_aluno >= media:
#     print("Você foi aprovado!")
# elif nota_do_aluno == 6:
#     participacao =  input('você foi participativo [S/N]')
#     if participacao.upper() == 'S':
#         print("Você está em recuperação.")
#     else:
#         print('Reprovado')
# else:
#     print("Estude mais. Reprovado.")

# ----------------------------------------------------------------


# 4.2 A PDA quer verificar se o Tiago está qualificado tirar férias. Para estar em condições, os seguintes requisitos devem ser satisfeito:
# - Ter trabalhado no mínimo 12 meses completos.
# - Ter disponibilidade de tirar férias entre dezembro e janeiro.
# Faca um algoritmo que valide ou não essas duas opções para saber se o Tiago pode tirar férias. O programa deverá escrever a mensagem “Tiago pode sair de férias “ ou  “Tiago não pode sair de férias”.

# meses_trabalhados = int(input('Quantos meses você trabalhou? '))
# disponibilidade = input('Você tem disponibilidade para tirar férias entre dezembro e janeiro? [S/N]')

# if meses_trabalhados == 12 and disponibilidade.upper() == 'S':
#     print('Tiago pode sair de férias')
# else:
#     print('Tiago não pode sair de férias')

# ----------------------------------------------------------------


# 4.3 A PdA fará uma confraternização em um grande parque aquático em São Paulo, mas para conseguir se programar e fechar a data precisa analisar a temperatura.
# Faça um programa que avalie e entregue as seguintes respostas:
#     - Maior que 25 graus ("Oba! A PDA pode marcar a data").
#     - Menor ou igual a 25 graus ("Vamos! O que vale é a companhia").
#     - Menor ou igual a 15 graus ("Estará muito frio, não podemos alugar nessa data").

# temperature_current = int(input(' Qual a temperatura atual: '))

# temperature_high = temperature_current  > 25

# temperature_average  = temperature_current  <= 25 and temperature_current > 15

# temperature_low = temperature_current <= 15

# if temperature_high:
#     print('Yay! The PDA can mark the date')
# elif temperature_average:
#     print('We will! What matters is the company')
# elif temperature_low: 
#     print('It will be very cold, we cannot rent on that date')

# ----------------------------------------------------------------

# DESAFIOS EXTRAS - OPCIONAIS

# DESAFIO_01 = Estamos com dificuldade em identificar se um número é positivo, negativo ou neutro.

# Faça uma programa que imprima se o número é positivo, neutro ou negativo.

# value = int(input('Digite um número'))

# if value < 0: 
#     print('número negativo')
# elif value >= 0:
#     print('número positivo')
# else: 
#     print('número neutro')




# DESAFIO_02 = Precisamos identificar a menor média de um aluno para saber se ele pode seguir para a próxima fase de um projeto.

# Faça um programa que peça as três notas do aluno e imprima a menor deles.

# notas_aluno_1 = int(input(' Digite aqui uma da suas notas: ')) 
# notas_aluno_2 = int(input(' Digite aqui uma da suas notas: '))
# notas_aluno_3 = int(input(' Digite aqui uma da suas notas: '))

# if notas_aluno_1 < notas_aluno_2 and notas_aluno_1 < notas_aluno_3:
#     print( ' Sua menor nota foi ➡',notas_aluno_1)
# elif notas_aluno_2 < notas_aluno_1 and notas_aluno_2 < notas_aluno_3:
#     print( ' Sua menor nota foi ➡',notas_aluno_2)
# elif notas_aluno_3 < notas_aluno_1 and notas_aluno_3 < notas_aluno_2:
#     print( ' Sua menor nota foi ➡',notas_aluno_3)
