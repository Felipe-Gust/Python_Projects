## Decida por mim
## Um script que irá responder, com respostas aleatorias, uma pergunta escolhida pelo usuário

import random
ask = {"1":"1: O que eu como hoje: lanche, pizza ou salada?", "2":"2: Devo sair esse final de semana?", "3":"3: Viajo para a praia ou interior?", "4":"4: Série ou filme?", "5":"5: Sair com os amigos(as) ou ficar em casa?", "6":"6: Viajar esse final de semana ou não?", "7":"7: Sair para o parque ou shopping?", "8":"8: Final de semana: dormir até tarde ou acordar um pouco mais cedo?", "9":"9: O que ouvir agora: rock, sertanejo, forró, pagode ou samba ou música clássica?", "10":"10: O que eu faço hoje: corrida ao ar livre, academia, zumba ou começo um novo esporte?", "11":"11: Qual estilo de dança treino hoje: forró, salsa, dança de rua ou sertanejo universitário?", "12":"12: Teatro ou cinema?", "13":"13: Happy hour ou voltar para casa?"}
repeat = "s"
   
print("Este programa possui respostas para aqueles momentos de dúvida que temos: 'Se faço isso ou aquilo?', 'Qual a melhor opção?'. Basta escolher a sua dúvida entre as opções e então deixar que ele decida por você :) ")
while repeat == "s":
  print("\n1: O que eu como hoje: lanche, pizza ou salada?", "\n2: Devo sair esse final de semana?", "\n3: Viajo para a praia ou interior?", "\n4: Série ou filme??", "\n5: Sair com os amigos(as) ou ficar em casa?", "\n6: Viajar esse final de semana ou não?", "\n7: Sair para o parque ou shopping?", "\n8: Final de semana: dormir até tarde ou acordar um pouco mais cedo?", "\n9: O que ouvir agora: rock, sertanejo, forró, pagode ou samba ou música clássica?", "\n10: O que eu faço hoje: corrida ao ar livre, academia, zumba ou começo um novo esporte?", "\n11: Qual estilo de dança treino hoje: forró, salsa, dança de rua ou sertanejo universitário?", "\n12: Teatro ou cinema?", "\n13: Happy hour ou voltar para casa?")
  option = input("Escolha uma das opções acima: ")
  phrase = ask.get(option, "\n")
  print("\nOpção escolhida: ", phrase)

  if option == "1":
    numberlist1 = ["Massa seria uma boa hoje. Vamos de Pizza!","Coma salada hoje, assim não ficará com a consciência pesada.","A resposta que tantos querem ouvir: hoje é dia de lanche!"]
    print("Sua resposta é: ", random.choice(numberlist1))
  elif option == "2":
    numberlist2 = ["Hoje está com cara de dia de filme em casa e com pipoca.","Com certeza, a vida é feita para ser aproveitada!","Só se for para comer!!", "Hoje é dia de aproveitar com a família."]
    print("Sua resposta é: ", random.choice(numberlist2))
  elif option == "3":
    numberlist3 = ["Sinta a areia do mar, partiu praia!!","Sentir a brisa e a sombra..interior hoje.","Nem precisa perguntar, dia de praia!","Dia de estender a rede num lugar bem tranquilo, hoje é interior."]
    print("Sua reposta é: ", random.choice(numberlist3))
  elif option == "4":
    numberlist4 = ["Comece aquela série que sempre quis, mas não teve coragem ainda de começar.", "Nenhum dos dois, vá ler um livro!","Hoje é dia de juntar a família e ver aquele filme de comédia.", "Lembra daquele filme que ainda não teve coragem de ver, então..assiste ele!","Comece aquela série que te indicaram ;)"]
    print("Sua resposta é: ", random.choice(numberlist4))
  elif option == "5":
    numberlist5 = ["Reúna todos aqueles que tem mais apreço e combinem de sair para aquele lugar divertido para darem risadas", "Ficar em casa, deitar no sofá e assistir aquela série (ou anime) nunca é demais. Aproveite para ficar em casa hoje.", "Saía com os amigos(as) e marquem de ir naquele lugar bom para jogar conversa fora."]
    print("Sua resposta é: ", random.choice(numberlist5))
  elif option == "6":
    numberlist6 = ["Viajar nunca é demais não é mesmo?! Então aproveite e faça isso.", "Sim, aproveite para levar aquelas pessoas que gosta de ter por perto, familiares ou amigos.", "Que tal aproveitar com a família, ou amigos, nesse final de semana?! Faça algo que há muito tempo não faziam!"]
    print("Sua resposta é: ", random.choice(numberlist6))
  elif option == "7":
    numberlist7 = ["Aproveite o dia para relaxar, vá ao parque hoje.", "Hoje é dia de shopping ;) ."]
    print("Sua resposta é: ", random.choice(numberlist7))
  elif option == "8":
    numberlist8 = ["Acho que você queria ouvir isso: durma até tarde.","Entre dormir mais e aproveitar, aproveite o final de semana, acorde um pouco mais cedo e aproveite ele.", "Aproveite e acorde um pouco mais cedo para fazer aquela atividade física ;) ."]
    print("Sua resposta é: ", random.choice(numberlist8))
  elif option == "9":
    numberlist9 = ["Ouça uma playlista de rock.", "Ouça sertanejo agora.", "Partiu ouvir forró.", "Que tal pagode agora?!", "Vamos de samba agora.", "Ouça música clássica agora."]
    print("Sua resposta é: ", random.choice(numberlist9))
  elif option == "10":
    numberlist10 = ["Pratique corrida ao ar livre.", "Hoje é dia de academia.", "Treine zumba e caso nunca tenha praticado, tente hoje ;) .", "Vamos tentar algo novo, comece um novo esporte."]
    print("Sua resposta é: ", random.choice(numberlist10))
  elif option == "11":
    numberlist11 = ["Pratique, ou aprenda, forró.", "Treine, ou aprenda, salsa.", "Sabe dançar 'dança de rua'?! Se sabe treine ela hoje, se não aprenda ela ;) .", "Treine uma bem conhecida hoje, o sertanejo universitário."]
    print("Sua resposta é: ", random.choice(numberlist11))
  elif option == "12":
    numberlist12 = ["Hoje é dia de cinema e com pipoca.", "Já foi ao teatro?! Se não foi, vá ao  teatro essa semana.", "Hoje é dia de filme, vamos de cinema.", "Hoje é dia de teatro."]
    print("Sua resposta é: ", random.choice(numberlist12))
  elif option == "13":
    numberlist13 = ["Dia de happy hour!!", "Já que me perguntou, hoje é melhor voltar para casa.", "Chama a galera do trabalho, pois hoje é dia de happy hour!", "Hoje é dia de..voltar pra casa."]
    print("Sua resposta é: ", random.choice(numberlist13))

  repeat = input("Caso queira continuar digite 'S' para sim, mas se quiser sair digite 'N'.").lower()
