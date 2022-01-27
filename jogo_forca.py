import random

def jogar():
    
    mensagem_abertura()
    
    palavra_secreta = gerar_palavra_secreta()
    
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0
    print (letras_acertadas)
    
    while (not acertou and not enforcou):
        
        chute = requere_chute()
        
        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta,chute,letras_acertadas)
        else:
            erros += 1
            desenho_forca(erros)
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        
        print (letras_acertadas)

    print("Fim do jogo")
    if acertou:
        mensagem_vitoria()
    elif enforcou:
        mensagem_derrota(palavra_secreta)


def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def gerar_palavra_secreta():
    arquivo_palavras = open("palavras.txt", "r", encoding='utf-8')
    palavras = []
    
    for linha in arquivo_palavras:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo_palavras.close()

    numero_random = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero_random].upper()
    return palavra_secreta

def inicia_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def requere_chute():
    chute = input ("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta,chute,letras_acertadas):
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1

def mensagem_derrota (palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_vitoria ():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar() 
