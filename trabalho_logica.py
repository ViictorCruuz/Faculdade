# Trabalho de lógica
# Tema:Conhecimento

Redes = []
Jredes = {}

Logica = []
Jlogica = {}

Modelagem = []
Jmodelagem = {}

cores = {'Limpar': '\033[m',
         'Vermelho': '\033[31m',
         'Verde': '\033[32m',
         'Amarelo': '\033[33m'}


# Tabela ANSI de cores (\033[Style;Text;Backm:
# STYLE          TEXT              BACKGROUND
# 0 None         #30     branco    #40
# 1 Bold         #31     vermelho  #41
# 4 Underline    #32     verde     #42
# 7 Negative     #33     amarelo   #43
# 34     azul      #44
# 35     rouxo     #45
# 36     ciano     #46
# 37     cinza     #47

def mensagem_acerto():
    return '\033[32mVocê acertou :)\033[m'


def mensagem_erro():
    return '\033[31mVocê errou :(\033[m'


def Menu():
    print('\033[1m-=' * 25)
    print('  JOGO DO CONHECIMENTO - APRENDA SE DIVERTINDO')
    print('-=' * 25)
    print('\033[m')
    print('1 -> Jogar\n''0 <- Sair\n''3 -> Ranking\n')
    try:
        opcao = int(input('Escolha uma opção!\n'))
        print()
        if opcao == 1:
            MenuCategoria()
        elif opcao == 3:
            MenuRanking()
        elif opcao == 0:
            return opcao
        else:
            print('{}Opção inválida, tente novamente!{}'.format(cores['Vermelho'], cores['Limpar']))
    except ValueError:
        print('{}Opção inválida, apenas números é permitido, tente novamente!{}'.format(cores['Vermelho'],
                                                                                        cores['Limpar']))
        Menu()


def MenuCategoria():
    print('\033[1m-=' * 12)
    print('  ESCOLHA UMA CATEGORIA')
    print('-=' * 12)
    print('\033[m')
    print('1 -> Redes de Computadores\n''2 -> Logica de Programação\n''3 -> Modelagem de Dados\n''4 <- Voltar\n')
    try:
        opcao2 = int(input('Escolha uma opção!\n'))
        print()
        if opcao2 == 1:
            RedesComputadores()
        elif opcao2 == 2:
            LogicaProgramacao()
        elif opcao2 == 3:
            ModelagemDados()
        elif opcao2 == 4:
            Menu()
        else:
            print('{}Opção inválida, tente novamente!{}'.format(cores['Vermelho'], cores['Limpar']))
            return MenuCategoria()
    except ValueError:
        print('{}Opção inválida, apenas números é permitido, tente novamente!{}'.format(cores['Vermelho'],
                                                                                        cores['Limpar']))
        MenuCategoria()


def RedesComputadores():
    Jredes['Nome: '] = str(input('{}Digite seu nome para registro:{} \n'.format(cores['Amarelo'], cores['Limpar'])))
    Jredes['Pontos: '] = 0
    print('\033[1;7;32mBem vindo ao jogo {}!!.Boa sorte!!\033[m\n'.format(Jredes['Nome: ']))
    acertos = int(0)

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PERGUNTAS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print()
    print('A) Qual Camada no Modelo OSI tem o papel de localizar outros computadores?\n'
          '\n1 - Sessão\n''2 - Transporte\n''3 - Aplicação\n''4 - Rede\n')

    escolha = int(input('Sua resposta: '))

    try:
        if escolha == 4:
            acertos += 1
            Jredes['Pontos: '] += 10
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('B) Diversos tipos de redes de computadores podem ser encontrados, como as ...\n'
          '\n1 - LANs, que suportam diversas topologias, como barramento, anel e estrela\n'
          '2 - LANs, destinadas à implementação de grandes redes, como numa grande cidade\n'
          '3 - WANs, para troca de dados entre redes distinas, sem utilizar o protocolo PPP\n'
          '4 - WANs, que utilizem apenas fibras ópticas na sua implementação\n')
    try:
        escolha = int(input('Sua resposta: '))
        if escolha == 1:
            acertos += 1
            Jredes['Pontos: '] += 10
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('C) Conforme o cert.br, são mecanismos de segurança de redes Wifi, exceto:\n'
          '\n1 - WEP\n'
          '2 - WEP-2\n'
          '3 - WPA\n'
          '4 - WPA-2\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 2:
            acertos += 1
            Jredes['Pontos: '] += 10
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('D) No modelo OSI, qual é a função da camada física?\n'
          '\n1 - Gerenciar o diálogo de uma forma ordenada para determinado serviço solicitado\n'
          '2 - Realizar a fragmentação das mensagens fim a fim, quando necessário\n'
          '3 - Estabelecer e liberar conexões, além de definir a sequência de pinos de conectores e suas '
          'respectivas funções\n'
          '4 - Realizar o controle de congestionamento entre hosts\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 3:
            acertos += 1
            Jredes['Pontos: '] += 10
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    if Jredes['Pontos: '] >= 1:
        print('Parabéns {}!!! Você acertou {}/10 pergunta(s) e marcou {} ponto(s)!{}'.format(Jredes['Nome: '], acertos,
                                                                                             Jredes['Pontos: '],
                                                                                             cores['Limpar']))
    else:
        print('Ooooh não!!! Você acertou {}/10 perguntas e não marcou nenhum ponto'.format(acertos,
                                                                                           Jredes['Pontos: ']))
    print()
    Redes.append(Jredes.copy())
    return RankingRedes()


def LogicaProgramacao():
    Jlogica['Nome: '] = str(input('{}Digite seu nome para registro:{} \n'.format(cores['Amarelo'], cores['Limpar'])))
    Jlogica['Pontos: '] = 0
    print('\033[1;7;32mBem vindo ao jogo {}!!.Boa sorte!!\033[m\n'.format(Jlogica['Nome: ']))
    acertos = int(0)

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PERGUNTAS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print()
    print('1) Qual Camada no Modelo OSI tem o papel de localizar outros computadores?\n'
          '1 - Sessão\n''2 - Transporte\n''3 - Aplicação\n''4 - Rede\n')
    escolha = int(input('Sua resposta: '))
    if escolha == 4:
        acertos += 1
        Jlogica['Pontos: '] += 10
        print('\033[32mVocê acertou :)\033[m')
    else:
        print('\033[31mVocê errou :(\033[m')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('1) Qual Camada no Modelo OSI tem o papel de localizar outros computadores?\n'
          '1 - Sessão\n''2 - Transporte\n''3 - Aplicação\n''4 - Rede\n')
    escolha = int(input('Sua resposta: '))
    if escolha == 4:
        acertos += 1
        Jlogica['Pontos: '] += 10
        print('\033[32mVocê acertou :)\033[m')
    else:
        print('\033[31mVocê errou :(\033[m')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('Parabéns {} Você acertou {}/10 perguntas e marcou {} pontos!{}'.format(Jlogica['Nome: '], acertos,
                                                                                  Jlogica['Pontos: '], cores['Limpar']))
    print()
    Logica.append(Jlogica.copy())
    return RankingLogica()


def ModelagemDados():
    Jmodelagem['Nome: '] = str(input('{}Digite seu nome para registro:{} \n'.format(cores['Amarelo'], cores['Limpar'])))
    Jmodelagem['Pontos: '] = 0
    print('\033[1;7;32mBem vindo ao jogo {}!!.Boa sorte!!\033[m\n'.format(Jmodelagem['Nome: ']))
    acertos = int(0)

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PERGUNTAS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print()
    print('1) Qual Camada no Modelo OSI tem o papel de localizar outros computadores?\n'
          '1 - Sessão\n''2 - Transporte\n''3 - Aplicação\n''4 - Rede\n')
    escolha = int(input('Sua resposta: '))
    if escolha == 4:
        acertos += 1
        Jmodelagem['Pontos: '] += 10
        print('\033[32mVocê acertou :)\033[m')
    else:
        print('\033[31mVocê errou :(\033[m')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('1) Qual Camada no Modelo OSI tem o papel de localizar outros computadores?\n'
          '1 - Sessão\n''2 - Transporte\n''3 - Aplicação\n''4 - Rede\n')
    escolha = int(input('Sua resposta: '))
    if escolha == 4:
        acertos += 1
        Jmodelagem['Pontos: '] += 10
        print('\033[32mVocê acertou :)\033[m')
    else:
        print('\033[31mVocê errou :(\033[m')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('Parabéns {} Você acertou {}/10 perguntas e marcou {} pontos!{}'.format(Jmodelagem['Nome: '], acertos,
                                                                                  Jmodelagem['Pontos: '],
                                                                                  cores['Limpar']))
    print()
    Modelagem.append(Jmodelagem.copy())
    return RankingModelagem()


def MenuRanking():
    print('\033[1m-=' * 20)
    print('                 RANKING')
    print('-=' * 20)
    print('\033[m')
    print('1 -> Redes de Computadores')
    print('2 -> Lógica de Programação')
    print('3 -> Modelagem de Dados')
    print('4 <- Voltar')
    print()
    try:
        opcao3 = int(input('Escolha uma opção'))
        if opcao3 == 1:
            RankingRedes()
            return MenuRanking()
        elif opcao3 == 2:
            RankingLogica()
            return MenuRanking()
        elif opcao3 == 3:
            RankingModelagem()
            return MenuRanking()
        elif opcao3 == 4:
            Menu()
        else:
            print('{}Opção inválida, tente novamente!{}'.format(cores['Vermelho'], cores['Limpar']))
            return MenuRanking()
    except ValueError:
        print('{}Opção inválida, apenas números é permitido, tente novamente!{}'.format(cores['Vermelho'],
                                                                                        cores['Limpar']))
        MenuRanking()


def RankingRedes():
    print('\033[1;7;34m-=-=-=-=-=-= Redes de Computadores =-=-=-=-=-=-=-=\033[m')
    for pessoas in Redes:
        for k, v in pessoas.items():
            print(f'{k}{v}')
        print()


def RankingLogica():
    print('\033[1;7;31m-=-=-=-=-=-=-= Lógica de Programação =-=-=-=-=-=-=\033[m')
    for pessoas in Logica:
        for k, v in pessoas.items():
            print(f'{k}{v}')
        print()


def RankingModelagem():
    print('\033[1;7;36m-=-=-=-=-=-=-=-= Modelagem de Dados =-=-=-=-=-=-=-\033[m')
    for pessoas in Modelagem:
        for k, v in pessoas.items():
            print(f'{k}{v}')
        print()


while True:
    try:
        opcao = Menu()
        if opcao == 0:
            break
    except ValueError:
        print('{}Opção inválida, tente novamente!{}'.format(cores['Vermelho'], cores['Limpar']))
