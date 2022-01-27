import random

def jogar():
    print ("*************************************")
    print ("  Bem-vindo ao jogo de adivinhação")
    print ("*************************************")
    print ("Tente adivinhar o número secreto")  

    numero_secreto = (round(random.randrange(1,101)))
    # print (numero_secreto)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("[1]Fácil,[2]Médio,[3]Difícil")
    nivel_str = input ("Defina um nível")
    nivel = int(nivel_str)


    while not nivel in range (1,4):
      nivel_str = input ("Defina um nível entre 1 e 3")
      nivel = int(nivel_str)
      if nivel in range (1,4):
        break

    if nivel == 1:
      total_de_tentativas=20
    elif nivel == 2:
      total_de_tentativas= 10
    elif nivel == 3:
      total_de_tentativas= 5


    for rodada in range (1, total_de_tentativas + 1):
      # print(f"Tentativa número {rodada} de {total_de_tentativas}")
      print("Tentativa número {} de {}".format(rodada,total_de_tentativas))
      chute_str = input ("Digite um número entre 1 e 100:")
      chute = int(chute_str)

      if chute < 1 or chute > 100 :
          print ("Você deve digitar um número entre 0 e 100")
          continue
      
      acertou = chute == numero_secreto
      maior = chute > numero_secreto
      menor = chute < numero_secreto

      if acertou:
        print("Parabéns, você adivinhou o número secreto!!!!" )
        print("Você fez {} pontos".format(pontos) )
        break
      else:
        if maior:
          print("Você errou!! o número escolhido é maior que o número secreto,tente outra vez")
        elif menor:
          print("Você errou!! o número escolhido é menor que o número secreto,tente outra vez")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    if rodada >= total_de_tentativas:
      print("Você perdeu!! fim de jogo!")
      print("Você fez {} pontos".format(pontos) )

if (__name__ == "__main__"):
    jogar()