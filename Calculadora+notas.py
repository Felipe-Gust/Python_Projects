##Calculadora de notas
##Uma calculadora de notas feita pensando em não restringir a quantidade de provas e atividades que o aluno possui, pois sabemos que nem todas escolas/faculdades avaliam da mesma forma.

valid = False
notet = []
notea = []
repeat = "s"
repeat2 = "s"
test_avg = 0
act_avg = 0
x = 0
y = 0

print("Essa calculadora irá calcular suas notas semestrais, sendo que você informa a quantidade de provas e atividades conforme sua escola, ou faculdade, realiza. Aperte enter para prosseguir.")

average = float(input("Digite qual a nota mínima para que o aluno NÃO reprove: "))

porct_t01 = int(input("Digite a porcentagem utilizada para cálculo das provas(não usar o sinal '%'): "))
porct_rt = porct_t01/100

porct_a01 = int(input("Digite a porcentagem utilizada para cálculo das atividades(não usar o sinal '%'): "))
porct_ra = porct_a01/100

valid = False
while valid == False:
  while repeat == "s":
    note_test = input("Digite a nota da prova do aluno: ")
    try:
      note_test = float(note_test)
      notet.append(note_test)
      test_avg += note_test
      x += 1
      repeat = input("Caso possua mais de uma prova para o semestre, ou ano, digite 's' e insira a nota da outra avaliação. Ou aperte Enter para ir ao próximo item.").lower()
      if note_test < 0 or note_test > 10:
        print("Nota inválida. Valor deve ser entre 0 a 10.")
      else:
        valid = True
    except:
      print("Formato inválido. Digite o valor com ponto ao invés de vírgula (ex.: 7.5).")

valid = False
while valid == False:
  while repeat2 == "s":
    note_activity = input("Digite a nota de atividade do aluno: ")
    try:
      note_activity = float(note_activity)
      notea.append(note_activity)
      act_avg += note_activity
      y += 1
      repeat2 = input("Caso possua mais de uma atividade para o semestre, ou ano, digite 's' e insira a nota da outra atividade. Ou aperte Enter para ir ao próximo item.").lower()
      if note_test < 0 or note_test > 10:
        print("Nota inválida. Valor deve ser entre 0 a 10.")
      else:
        valid = True
    except:
      print("Formato inválido. Digite o valor com ponto ao invés de vírgula (ex.: 7.5).")

print("Média de prova do aluno: ", (test_avg * porct_rt)/x)
print("Média de atividade do aluno ", (act_avg * porct_ra)/y)

avg_final = float((((test_avg * porct_rt)/x) + ((act_avg * porct_ra)/y)))
print("Média final semestral/anual do aluno: ", avg_final)

if avg_final >= average:
  print("Aluno aprovado, média final maior que ", average, ".")
else:
  print("Aluno reprovado, média final menor que ", average, ".")
 
