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
    acertos = 0

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PERGUNTAS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print()
    print('A) Qual Camada no Modelo OSI tem o papel de localizar outros computadores?\n'
          '\n1 - Sessão\n''2 - Transporte\n''3 - Aplicação\n''4 - Rede\n')

    escolha = int(input('Sua resposta: '))

    try:
        if escolha == 4:
            acertos += 1
            Jredes['Pontos: '] += 20
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
            Jredes['Pontos: '] += 20
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
            Jredes['Pontos: '] += 20
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
            Jredes['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('E) Como é denominado o protocolo responsável por fazer o gerencimento de máquinas que estejam funcionan em '
          '1rede com o padrão TCP/IP?\n'
          '\n1 - SMTP\n'
          '2 - POP\n'
          '3 - FTP\n'
          '4 - SNMP\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 4:
            acertos += 1
            Jredes['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    if Jredes['Pontos: '] >= 1:
        print('Parabéns {}!!! Você acertou {}/5 pergunta(s) e marcou {} pontos!{}'.format(Jredes['Nome: '], acertos,
                                                                                          Jredes['Pontos: '],
                                                                                          cores['Limpar']))
    else:
        print('Ooooh não!!! Você acertou {}/5 perguntas e não marcou nenhum ponto'.format(acertos,
                                                                                          Jredes['Pontos: ']))
    print()
    Redes.append(Jredes.copy())
    return RankingRedes()


def LogicaProgramacao():
    Jlogica['Nome: '] = str(input('{}Digite seu nome para registro:{} \n'.format(cores['Amarelo'], cores['Limpar'])))
    Jlogica['Pontos: '] = 0
    print('\033[1;7;32mBem vindo ao jogo {}!!.Boa sorte!!\033[m\n'.format(Jlogica['Nome: ']))
    acertos = 0

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PERGUNTAS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print()
    print('A) Um algoritmo pode ou não ter solução computacional. Baseado nisso, assinale a alternativa que indique '
          'um problema que têm solução computacional, ou seja, a partir do algoritmo é possível construir um programa '
          'de computador\n'
          '\n1 - Problema de cubo mágico\n'
          '2 - Trocar um pneu furado\n'
          '3 - Converter um valor em dólares ($) para reais (R$)\n'
          '4 - Amarrar os cadarços\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 3:
            acertos += 1
            Jlogica['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('B) A linguagem Python criada no início da década de 90 surgiu com o objetivo de aumentar a produtividade '
          'do programador, com as seguintes características:\n'
          '\n1 - Linguagem de baixo e alto nível com licença proprietária e semelhante à linguagem C e Pascal\n'
          '2 -  Linguagem de alto nível com licença pública, linguagem interpretada e interativa com criação de '
          'scripts que permite portabilidade e automatização de tarefas\n'
          '3 - Linguagem de baixo nível com compilador interativo que permite a criação de executáveis\n'
          '4 - Linguagem de alto nível com licença proprietária totalmente orientada a eventos.\n')

    try:
        escolha = int(input('Sua escolha: '))

        if escolha == 2:
            acertos += 1
            Jlogica['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('C) Tanto o interpretador como o compilador transformam o código escrito em linguagem humana para linguagem '
          'de máquina, porém o compilador faz isto em tempo de compilação enquanto o interpretador faz isto em tempo '
          'de execução.\n'
          '\n1 - Verdadeiro\n'
          '2 - Falso\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 1:
            acertos += 1
            Jlogica['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha == 2:
            print(mensagem_erro())
        else:
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('D) De acordo com a sequência numérica abaixo, diga qual seria o próximo número da lista:\n')

    lista = [1, 3, 7, 15, 31, 63, 127]
    for n in lista:
        print(n)
        if n == 63:
            break
    print()

    print('1 - 64\n'
          '2 - 79\n'
          '3 - 154\n'
          '4 - 127\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 4:
            acertos += 1
            Jlogica['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('E) A afirmação: o bloco do comando if também é conhecido como um desvio, é:\n'
          '\n1 - Verdadeiro\n'
          '2 - Falso\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 1:
            acertos += 1
            Jlogica['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha == 2:
            print(mensagem_erro())
        else:
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
    except ValueError:
        print('Isso não é um número!!!')

    if Jlogica['Pontos: '] >= 1:
        print('Parabéns {}!!! Você acertou {}/5 pergunta(s) e marcou {} pontos!{}'.format(Jlogica['Nome: '], acertos,
                                                                                          Jlogica['Pontos: '],
                                                                                          cores['Limpar']))
    else:
        print('Ooooh não!!! Você acertou {}/5 perguntas e não marcou nenhum ponto'.format(acertos,
                                                                                          Jlogica['Pontos: ']))

    print()
    Logica.append(Jlogica.copy())
    return RankingLogica()


def ModelagemDados():
    Jmodelagem['Nome: '] = str(input('{}Digite seu nome para registro:{} \n'.format(cores['Amarelo'], cores['Limpar'])))
    Jmodelagem['Pontos: '] = 0
    print('\033[1;7;32mBem vindo ao jogo {}!!.Boa sorte!!\033[m\n'.format(Jmodelagem['Nome: ']))
    acertos = 0

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PERGUNTAS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print()
    print('A) Em Modelagem de Dados, um tipo de atributo, que não pertence propriamente ao objeto (entidade ou '
          'relacionamento) onde está alocado, mas fez algum tipo de citação ou ligação desse objeto com outro, '
          'recebe um nome. Assinale a alternativa referente a esse atributo.\n'
          '\n1 - Atributo chave\n'
          '2 - Atributo descritivo derivado\n'
          '3 - Atributo referencial\n'
          '4 - Atributo descritivo composto')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 3:
            acertos += 1
            Jmodelagem['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('B) No Modelo Entidade Relacionamento, o modelo de dados pode ser classificado nos seguintes níveis de '
          'abstração:\n'
          '\n1 - Conceitual, normativo e físico\n'
          '2- Lógico, normativo e associativo\n'
          '3 - Conceitural, lógico e físico\n'
          '4 - Físico, descritivo e relacionamento\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 3:
            acertos += 1
            Jmodelagem['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print(
        'C) Um Analista de Sistemas, ao fazer a modelagem de um banco de dados, constatou a necessidade de representar'
        'um relacionamento com origem e destino em um mesmo conjunto de entidades. Esse tipo de relacionamento '
        'denomina-se\n'
        '\n1 - Indireto\n'
        '2 - Recursivo\n'
        '3 - Interno\n'
        '4 - Adaptivo\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 2:
            acertos += 1
            Jmodelagem['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('D) Quando se modela um banco de dados, para evitar a redundância dos dados nas tabelas devem-se eliminar as '
          'tabelas aninhadas, a dependência funcional parcial de atributos e a dependência funcional transitiva de '
          'atributos. Para conseguir isso utiliza-se um processo conhecido como\n'
          '\n1 - Encapsulamento\n'
          '2 - Agregação\n'
          '3 - Especialização\n'
          '4 - Normalização\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 4:
            acertos += 1
            Jmodelagem['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print(
        'E) Na Modelagem de Banco de Dados com o MER, Modelo Entidade Relacionamento, os atributos são características'
        ' que definem as entidades, e uma entidade é um objeto de interesse do usuário final. Os atributos podem ser '
        'classificados em simples e compostos, monovalorados, multivalorados e derivados. O atributo derivado pode ser'
        ' armazenado ou não armazenado e, em ambos os casos, apresentam vantagens e desvantagens. Assinale a '
        'alternativa que apresenta uma desvantagem do atributo derivado armazenado.\n'
        '\n1 - Exige manutenção constante para garantir que o valor seja atual, especialmente se qualquer valor '
        'utilizado na computação se alterar\n'
        '2 - Utiliza ciclos de processamento da CPU\n'
        '3 - Aumenta o tempo de acesso aos dados\n'
        '4 - Adiciona complexidade de codificação das consultas\n')

    try:
        escolha = int(input('Sua resposta: '))

        if escolha == 1:
            acertos += 1
            Jmodelagem['Pontos: '] += 20
            print(mensagem_acerto())
        elif escolha not in range(1, 5):
            print('\033[31mNúmero de resposta não existe, portanto será contado como erro!!! :(\033[m')
        else:
            print(mensagem_erro())
    except ValueError:
        print('Isso não é um número!!!')

    if Jmodelagem['Pontos: '] >= 1:
        print('Parabéns {}!!! Você acertou {}/5 pergunta(s) e marcou {} pontos!{}'.format(Jmodelagem['Nome: '], acertos,
                                                                                          Jmodelagem['Pontos: '],
                                                                                          cores['Limpar']))
    else:
        print('Ooooh não!!! Você acertou {}/5 perguntas e não marcou nenhum ponto'.format(acertos,
                                                                                          Jmodelagem['Pontos: ']))

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
