#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um
#par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11,
#você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de
#"craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu
#"Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
#Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.


from random import randrange
import random
i=0 
ponto = 0
while i == 0:
    print ('__________________________________________________________________')
    print (' |||||||||| ||||||||||    |||||||||| ||||||||||  |||||||||||      ')
    print (' ||         ||      ||    ||      || ||      ||  ||               ')
    print (' ||         ||||||||||    |||||||||| ||||||||||  |||||||||||      ')
    print (' ||         ||   ||       ||      || ||                   ||      ')
    print (' ||         ||     ||     ||      || ||                   ||      ')
    print (' |||||||||| ||       ||   ||      || ||          |||||||||||      ')
    print ('__________________________________________________________________')                  
    tentativa = str(input('Quando estiver pronto para jogar os dados digite /sim/.'))
    if tentativa == 'sim':
        dados = random.randrange(2,12) 
        ponto = dados
        print('resultado: ',dados) #lance de dados
        if dados == 7 or dados  == 11:
            print ('NATURAL. Você ganhou')
            break
        if dados == 2 or dados  == 3 or dados == 12:
            print ('CRAPS. Você perdeu')
            break
        if dados == 2 or dados == 5 or dados  == 6 or dados  == 8 or dados  == 9 or dados  == 10:
            print ('Este é o seu ponto. Você precisa tirar o número ',dados,'novamente.')
            proximatentativa = str(input('Quando estiver pronto para jogar os dados digite /sim/.'))
            if proximatentativa == 'sim':
                dados = random.randrange(2,12)
                print('resultado: ',dados)
                while dados !=  ponto:
                    proximatentativa = str(input('Quando estiver pronto para jogar os dados digite /sim/.'))
                    if proximatentativa == 'sim':
                        dados = random.randrange(2,12)
                        print('resultado: ',dados)
                        if dados == 7:
                            print('Você perdeu.')
                            break
                            if dados == ponto:
                                print ('Você ganhou.')
                                break
        
       


              


   