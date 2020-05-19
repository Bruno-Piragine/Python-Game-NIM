import sys

def main():
    n = m = x = y = 0
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    while x != 1 or x != 2:
        x = float(input("\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
        if x == 1:
            print('\nVocê escolheu uma partida isolada!')
            partida(n, m)
            
        if x == 2:
            print("\nVocê escolheu um campeonato!")
            campeonato(n, m)
            
    
def partida(n, m):
    while n < 1 or m < 1:
        n = int(input("\nQuantas peças? "))
        m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("\nVocê começa!")
        while n != 0:
            n = n - (usuario_escolhe_jogada(n, m))
            if n > 0:
                n = n - (computador_escolhe_jogada(n, m))
        print("\nFim de jogo! O computador venceu!")
                    
    else:
        print("\nComputador começa")
        while n != 0:
            n = n - (computador_escolhe_jogada(n, m))
            if n > 0:
                n = n - (usuario_escolhe_jogada(n, m))
            else:
                print("\nFim de jogo! O computador venceu!")
            
def usuario_escolhe_jogada(n, m):
    u = int(input("\nQuantas peças você vai tirar? "))
    while u > m or u <= 0 or u > n:
        u = int(input("Ops!! Jogada inválida! Tente de novo.\nQuantas peças você vai tirar? "))
    if u == 1:
        print("\nVocê tirou",u,"peça") 
    else:
        print("\nVocê tirou",u,"peças")
    if n == 1:
        print("Agora resta apenas",n - u,"peça no tabuleiro")
    else:
        print("Restam",n - u,"peças no tabuleiro")
    return u

def computador_escolhe_jogada(n, m):    
    y = n % (m + 1)
    if y == 1:
        print("\nComputador tirou",y,"peça") 
    else:
        print("\nComputador tirou",y,"peças")
    n = n - y
    if n == 1:
        print("Agora resta apenas",n,"peça no tabuleiro")
    if n >= 1:
        print("Restam",n,"peças no tabuleiro")
    return y

    
     
def campeonato(n, m):
    print("\n**** Rodada 1 ****\n")
    partida(n, m)
    print("\n**** Rodada 2 ****\n")
    partida(n, m)
    print("\n**** Rodada 3 ****\n")
    partida(n, m)
    print("\n**** Final do campeonato! ****\nPlacar: Você 0 X 3 Computador\n")

main()

        
                
        
    
    
