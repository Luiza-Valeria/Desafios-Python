agenda = {}

# Criando um Menu
while True:
    print("""
            === MENU DA AGENDA ===
            1 - Adicionar Contato
            2 - Remover Contato
            3 - Buscar Contato
            4 - Listar Contato
            5 - Sair
""")
    escolha = int(input("Escolha uma opção: "))

    # Adicionando um contato na agenda

    if escolha == 1:
        nome = str(input("Digite o nome do contato: ")).upper().strip()
        print("O nome adicionado foi {} ".format(nome))
        telefone = str(input("Digite o número deo contato: "))

        #Verificando se o valor digitado é um numero e tem 9 digitos

        if telefone.isdigit() and len(telefone) == 9:
            print("O número {} foi adicionadp".format(telefone))
            agenda[nome] = telefone
            print("Contato Adicionado com sucesso!!!")
            break
        else:
            print("Erro: O número deve conter exatamente 9 dígitos.")


    # Deletando um contato da agenda

    elif escolha == 2:
        nome = str(input("Digite o nome do contato para remover: "))
        print("Voce irá remover {} dos seus contatos".format(nome))
        del agenda[nome]
        print("Contato removido com sucesso")

    # Buscando um conato na agenda
    elif escolha == 3:
        nome = str(input("Digite o nome do contato para buscar"))
        if nome in agenda:
            print("Nome: ",nome, "Telefone: ",agenda[nome])
        else:
            print("Contato não encontrado!")
    # Mostrando a Agenda completa

    elif escolha == 4:
        if agenda :
            print("=== Lista de Contato ===")
            for nome,telefone in agenda.items():
                print(nome, " - ", telefone)
        else:
            print("A agenda está Vazia")

    # Sainda da Agenda

    elif escolha == 5:
        print("Sainda da Agenda...")
        break

    else:
        print("Opção Inválida! Tente Novamente")

