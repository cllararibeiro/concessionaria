# Relatório aniversariante do mês
# mês com mais vendas de cada ano
# relatorio veiculos por categoria, faixa de preco

import csv
import os
import  datetime

print("""
=========================================================
                BEM VINDO A SUCCESS CAR 💫🚘
=========================================================""")
print("""

      """)
input("Pressione ENTER para continuar...")
os.system("clear")

aviso ="""
=========================================================
                     AVISO DO SISTEMA
=========================================================

Algumas funcionalidades  ainda não foram implementadas.
O sistema está em fase de desenvolvimento, em breve 
estará completo.

            🚀 Aguarde futuras atualizações!

=========================================================
"""

menu = """
================================================
    🚗 SISTEMA DE GESTÃO - CONCESSIONÁRIA 🚗
================================================

   [1]  🚘 Módulo Veículos
   [2]  👥 Módulo Clientes
   [3]  💰 Módulo Vendas
   [4]  📊 Módulo Relatórios
   [5]  ℹ️ Informações do Sistema

   [0]  ❌ Sair

================================================
"""

menu_veiculos = """
================================================
             🚘 MÓDULO VEÍCULOS 🚘
================================================

   [1]  ➕ Cadastrar Veículo
   [2]  🔍 Buscar Veículo
   [3]  ✏️ Editar Veículo
   [4]  🗑️ Excluir Veículo

   [0]  ↩️ Voltar ao Menu Principal

================================================
"""

menu_clientes = """
================================================
            👥 MÓDULO CLIENTES 👥
================================================

   [1]  ➕ Cadastrar Cliente
   [2]  🔍 Buscar Cliente
   [3]  ✏️ Editar Cliente
   [4]  🗑️ Excluir Cliente

   [0]  ↩️ Voltar ao Menu Principal

================================================
"""

menu_vendas = """
================================================
              💰 MÓDULO VENDAS 💰
================================================

   [1]  🛒 Cadastrar Venda
   [2]  🔍 Buscar Venda
   [3]  ✏️ Editar Venda
   [4]  🗑️ Excluir Venda

   [0]  ↩️ Voltar ao Menu Principal

================================================
"""

menu_relatorios = """
================================================
            📊 MÓDULO RELATÓRIOS 📊
================================================

   [1]  🚘 Relatório de Veículos
   [2]  👥 Relatório de Clientes
   [3]  💰 Relatório de Vendas

   [0]  ↩️ Voltar ao Menu Principal

================================================
"""

menu_info = """
==================================================
                ℹ️ INFORMAÇÕES ℹ️
==================================================
                🚗 Sucess Car 🚗
Sistema de gestão para concessionárias de veículos

   👩‍💻 Equipe de desenvolvimento:
   • Maria Clara

   🐍 Linguagem:
   • Python

   📜 Licença Pública Geral GNU
   🌐 www.gnu.org/licenses/gpl.html

   © 2026 - Todos os direitos reservados

   [0] ↩️ Voltar ao Menu Principal

==================================================
"""
opcao = -1

while opcao != 0:
    print(menu)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        resp = ""
        os.system("clear")
        print(menu_veiculos)
        while resp!= 0:
            resp = int(input("Digite a opção desejada do Módulo Veículos: "))
            print("resposta: ", resp)
            input("Pressione ENTER para continuar...")
            if resp == 1:
                os.system("clear")
                print("=== Essa opção é responsável por cadastrar um novo veículo no sistema. ===")
                categoria = input("""Informe a categoria do veículo
                                Digite:
                                1 para Carro
                                2 para Moto
                                3 para Caminhão
                                """)
                if categoria == "1":
                    categoria = "Carro"
                elif categoria == "2":
                    categoria = "Moto"
                elif categoria == "3":
                    categoria = "Caminhão"
                marca = input("Informe a marca: ")
                modelo = input("Informe o modelo: ")
                ano = int(input("Informe o ano: "))
                cor = input("Informe a cor: ")
                placa = input("Informe a placa: ")
                km = float(input("Informe a quilometragem: "))
                valor = float(input("Informe o valor: "))
                tipo = input("Novo ou Usado? ")
                placa_existe = False
                precisa_cabecalho = False
                  # Criamos essa caixinha para nos ajudar

                # Tenta abrir para ler. Se der erro porque o arquivo não existe,
                # o Python pula direto para o 'except'
                try:
                    with open("veiculos.txt", "r") as arquivo:
                        for linha in arquivo:
                            dados = linha.strip().split(";")
                            if dados[0] == placa:
                                placa_existe = True
                except FileNotFoundError:
                    # Se caiu aqui, é porque o arquivo ainda não existe!
                    # Então, com certeza vamos precisar criar o cabeçalho mais abaixo.
                    precisa_cabecalho = True

                if placa_existe:
                    print(f"Veículo com placa {placa} já existe no sistema. Cadastro cancelado.")
                else:     
                    with open("veiculos.txt", "a") as arquivo:
                        # Se a nossa caixinha for True, escreve o cabeçalho primeiro
                        if precisa_cabecalho:
                            arquivo.write("placa;categoria;marca;modelo;ano;cor;km;valor;tipo\n")
                        # Depois escreve os dados do veículo normalmente
                        arquivo.write(
                            f"{placa};{categoria};{marca};{modelo};"
                            f"{ano};{cor};{km};{valor};{tipo}\n"
                        )
                    print(f"""
                    Veículo cadastrado com Sucesso!
                    📜 Categoria: {categoria}
                    🚘 Marca: {marca}
                    🚗 Modelo: {modelo}
                    📅 Ano: {ano}
                    🎨 Cor: {cor}
                    🔖 Placa: {placa}
                    💰 Valor: R$ {valor:.2f}
                    📌 Tipo: {tipo}
                    """)

                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)

            elif resp == 2:
                os.system("clear")
                print("=== Essa opção é responsável por buscar um veículo no sistema. ===")

                placa = input("Informe a placa do veículo: ")
                print(f"Buscando veículo com placa {placa}...")

                veiculo = None

                try:
                    with open("veiculos.txt", "r") as arquivo:
                        for linha in arquivo:
                            dados = linha.strip().split(";")
                            if dados[0] == placa:
                                veiculo = dados
                except FileNotFoundError:
                    # Se o arquivo não existir, o 'veiculo' continuará sendo None,
                    # o que vai direto para a mensagem de "não encontrado" lá embaixo.
                    pass

                if veiculo:
                    print(f"""
                    📜 Categoria: {veiculo[1]}
                    🚘 Marca: {veiculo[2]}
                    🚗 Modelo: {veiculo[3]}
                    📅 Ano: {veiculo[4]}
                    🎨 Cor: {veiculo[5]}
                    🔖 Placa: {veiculo[0]}
                    ℹ️ KM: {veiculo[6]}
                    💰 Valor: R$ {float(veiculo[7]):.2f}
                    📌 Tipo: {veiculo[8]}
                    """)
                else:
                    print(f"Veículo com placa {placa} não encontrado.")

                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)


            elif resp == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar as informações de um veículo no sistema. ===")
                placa = input("Informe a placa do veículo que deseja editar: ")
                veiculo = None
                linhas = []
                # Protegemos a leitura inicial caso o arquivo não exista
                try:
                    with open("veiculos.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                except FileNotFoundError:
                    # Se o arquivo não existir, 'linhas' continua vazia e o 'veiculo' será None
                    pass    

                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == placa:
                        veiculo = dados

                if veiculo:
                    print(f"""
                    🔖 Placa: {veiculo[0]}
                    🚘 Marca: {veiculo[2]}
                    🚗 Modelo: {veiculo[3]}
                    📅 Ano: {veiculo[4]}
                    🎨 Cor: {veiculo[5]}
                    ℹ️ KM: {veiculo[6]}
                    💰 Valor: R$ {float(veiculo[7]):.2f}
                    📌 Tipo: {veiculo[8]}
                    """)

                    editc = -1
                    placa_original = placa

                    while editc != 0:
                        editc = int(input("""
                        Qual informação deseja editar?

                        [1] Marca
                        [2] Modelo
                        [3] Ano
                        [4] Cor
                        [5] Placa
                        [6] Quilometragem
                        [7] Valor
                        [8] Tipo
                        [9] Categoria

                        [0] Finalizar edição
                        """))

                        if editc == 1:
                            veiculo[2] = input("Altere a marca: ")
                        elif editc == 2:
                            veiculo[3] = input("Altere o modelo: ")
                        elif editc == 3:
                            veiculo[4] = input("Altere o ano: ")
                        elif editc == 4:
                            veiculo[5] = input("Altere a cor: ")
                        elif editc == 5:
                            nova_placa = input("Altere a placa: ")
                            # Evita que o usuário tente mudar a placa de um carro para a palavra "placa"
                            if nova_placa == "placa":
                                print("Nome inválido! 'placa' é uma palavra reservada do sistema.")
                            elif nova_placa == placa_original:
                                veiculo[0] = nova_placa
                            else:
                                placa_existe = False
                                with open("veiculos.txt", "r") as arquivo:
                                    for linha in arquivo:
                                        dados = linha.strip().split(";")
                                        if dados[0] == nova_placa:
                                            placa_existe = True
                                if placa_existe:
                                    print("Já existe um veículo com essa placa!")
                                else:
                                    veiculo[0] = nova_placa
                        elif editc == 6:
                            veiculo[6] = input("Altere a quilometragem: ")
                        elif editc == 7:
                            veiculo[7] = input("Altere o valor: ")
                        elif editc == 8:
                            veiculo[8] = input("Novo ou Usado? ")
                        elif editc == 9:
                            veiculo[1] = input("Altere a categoria: ")

                    for i in range(len(linhas)):
                        dados = linhas[i].strip().split(";")
                        if dados[0] == placa_original:
                            linhas[i] = ";".join(veiculo) + "\n"
                
                    # Salva o arquivo de volta (o cabeçalho que já estava na lista 'linhas' é mantido!)
                    with open("veiculos.txt", "w") as arquivo:
                        arquivo.writelines(linhas)
                    print("Veículo atualizado com sucesso!")
                else:
                    print(f"Veículo com placa {placa} não encontrado.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)

            elif resp == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um veículo do sistema. ===")
                placa = input("Informe a placa do veículo que deseja excluir: ")
                
                linhas = []
                # Protegemos a leitura caso o arquivo ainda não exista no sistema
                try:
                    with open("veiculos.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                except FileNotFoundError:
                    # Se o arquivo não existir, 'linhas' fica vazia
                    pass

                veiculo_encontrado = False
                novas_linhas = []

                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == placa:
                        veiculo_encontrado = True
                    else:
                        # O cabeçalho entra aqui automaticamente, pois a palavra
                        # "placa" nunca será igual à placa digitada pelo usuário!
                        novas_linhas.append(linha)

                if veiculo_encontrado:
                    with open("veiculos.txt", "w") as arquivo:
                        arquivo.writelines(novas_linhas)
                    print(f"Veículo com placa {placa} excluído com sucesso!")
                else:
                    print(f"Veículo com placa {placa} não encontrado.")

                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)

    elif opcao == 2:
        resp_cli = -1
        os.system("clear")
        print(menu_clientes)
        while resp_cli!= 0:
            resp_cli = int(input("Digite a opção desejada do Módulo Clientes: "))
            if resp_cli == 1:
                os.system("clear")
                print("=== Essa opção é responsável pelo cadastro do cliente ===")

                nome = input("Informe o nome: ")
                cpf = input("Informe o CPF: ")
                datanasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
                telefone = input("Informe o telefone: ")
                email = input("Informe o email: ")
                cidade = input("Informe a cidade: ")

                cpf_existe = False
                precisa_cabecalho = False

                try:
                    with open("clientes.txt", "r") as arquivo:
                        for linha in arquivo:
                            dados = linha.strip().split(";")
                            if dados[0] == cpf:
                                cpf_existe = True
                except FileNotFoundError:
                    precisa_cabecalho = True
                if cpf_existe:
                    print(f"Cliente com CPF {cpf} já existe no sistema. Cadastro cancelado.")
                else:
                    with open("clientes.txt", "a") as arquivo:
                        if precisa_cabecalho:
                            arquivo.write("cpf;nome;telefone;email;cidade;datanasc\n")
                        arquivo.write(
                            f"{cpf};{nome};{telefone};"
                            f"{email};{cidade};{datanasc}\n"
                        )

                    print(f"""
                    ✅ Cliente cadastrado com sucesso!

                    👤 Nome: {nome}
                    🪪 CPF: {cpf}
                    📞 Telefone: {telefone}
                    📧 Email: {email}
                    📍 Cidade: {cidade}
                    📅 Data de Nascimento: {datanasc}
                    """)

                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)
            elif resp_cli == 2:
                os.system("clear")
                print("=== Essa opção é responsável por buscar um cliente no sistema. ===")
                cpf = input("Informe o CPF do cliente: ")
                print(f"Buscando cliente com CPF {cpf}...")

                cliente = None
                try:
                    with open("clientes.txt", "r") as arquivo:
                        for linha in arquivo:
                            dados = linha.strip().split(";")
                            if dados[0] == cpf:
                                cliente = dados
                except FileNotFoundError:
                    # Se o arquivo não existir, 'cliente' continua sendo None,
                    # o que vai direto para a mensagem de "não encontrado" lá embaixo.
                    pass
                if cliente:
                    print(f"""
                    👤 Nome: {cliente[1]}
                    🪪 CPF: {cliente[0]}
                    📞 Telefone: {cliente[2]}
                    📧 Email: {cliente[3]}
                    📍 Cidade: {cliente[4]}
                    📅 Data de Nascimento: {cliente[5]}
                    """)
                else:
                    print(f"Cliente com CPF {cpf} não encontrado.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)

            elif resp_cli == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar as informações de um cliente no sistema. ===")
                cpf = input("Informe o CPF do cliente que deseja editar: ")
                cliente = None
                linhas = []
                try:
                    with open("clientes.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                except FileNotFoundError:
                    # Se o arquivo não existir, 'linhas' continua vazia e o 'cliente' será None
                    pass
                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == cpf:
                        cliente = dados
                if cliente:
                    print(f"""
                    👤 Nome: {cliente[1]}
                    🪪 CPF: {cliente[0]}
                    📞 Telefone: {cliente[2]}
                    📧 Email: {cliente[3]}
                    📍 Cidade: {cliente[4]}
                    📅 Data de Nascimento: {cliente[5]}
                            """)
                    
                    edit = -1
                    cpf_original = cpf

                    while edit !=0:
                        edit = int(input("""
                        Qual informação deseja editar?
                        [1] Nome
                        [2] CPF
                        [3] Telefone
                        [4] Email
                        [5] Cidade
                        [6] Data de Nascimento
                                         
                        [0] Finalizar edição
                        """))
                        if edit == 1:
                            cliente[1] = input("altere o nome: ")
                        elif edit == 2:
                            novo_cpf = input("altere o CPF: ")
                            if novo_cpf == "cpf":
                                print("Nome inválido! 'cpf' é uma palavra reservada do sistema.")
                            elif novo_cpf == cpf_original:
                                cliente[0] = novo_cpf
                            else:   
                                cpf_existe = False
                                with open("clientes.txt", "r") as arquivo:
                                    for linha in arquivo:
                                        dados = linha.strip().split(";")
                                        if dados[0] == novo_cpf:
                                            cpf_existe = True
                                if cpf_existe:
                                    print("Já existe um cliente com esse CPF!")
                                else:
                                    cliente[0] = novo_cpf
                        elif edit == 3:
                            cliente[2] = input("altere o telefone: ")
                        elif edit == 4:
                            cliente[3] = input("altere o email: ")
                        elif edit == 5:
                            cliente[4] = input("altere a cidade: ")
                        elif edit == 6:
                            cliente[5] = input("altere a data de nascimento (DD/MM/AAAA): ")
                    for i in range(len(linhas)):
                        dados = linhas[i].strip().split(";")
                        if dados[0] == cpf_original:
                            linhas[i] = ";".join(cliente) + "\n"
                    with open("clientes.txt", "w") as arquivo:
                        arquivo.writelines(linhas)

                    print(f"""
                        Cliente atualizado com Sucesso!
                    👤 Nome: {cliente[1]}
                    🪪 CPF: {cliente[0]}
                    📞 Telefone: {cliente[3]}
                    📧 Email: {cliente[4]}
                    📍 Cidade: {cliente[5]}
                    📅 Data de Nascimento: {cliente[2]}
                        """)
                else:
                    print(f"Cliente com CPF {cpf} não encontrado.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)

            elif resp_cli == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um cliente do sistema. ===")
                cpf = input("Informe o CPF do cliente que deseja excluir: ")
                linhas = []
                try:
                    with open("clientes.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                except FileNotFoundError:
                    # Se o arquivo não existir, 'linhas' fica vazia
                    pass
                cliente_encontrado = False
                novas_linhas = []
                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == cpf:
                        cliente_encontrado = True
                    else:
                        novas_linhas.append(linha)
                if cliente_encontrado:
                    with open("clientes.txt", "w") as arquivo:
                        arquivo.writelines(novas_linhas)
                    print(f"Cliente com CPF {cpf} excluído com Sucesso!")
                else:
                    print(f"Cliente com CPF {cpf} não encontrado.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)

    elif opcao == 3:
        resp_venda = -1
        os.system("clear")
        print(menu_vendas)
        while resp_venda!= 0:
            resp_venda = int(input("Digite a opção desejada do Módulo Vendas: "))
            if resp_venda == 1:
                os.system("clear")
                print("=== Essa opção é responsável pelo cadastro de uma venda ===")
                cpf_cli = input("Informe o CPF do cliente: ")
                placa_pro = input("Informe a placa do veículo: ")
                data = input("Informe a data da venda (DD/MM/AAAA): ")
                cliente_existe = False
                veiculo_existe = False
                veiculo_ja_vendido = False

                # === PASSO 1: Checar se o cliente existe ===
                try:
                    with open("clientes.txt", "r") as arquivo_cli:
                        for linha in arquivo_cli:
                            dados_cli = linha.strip().split(";")
                            if dados_cli[0] == cpf_cli:
                                cliente_existe = True
                except FileNotFoundError:
                    pass
                # === PASSO 2: Checar se o veículo existe ===
                try:
                    with open("veiculos.txt", "r") as arquivo_vei:
                        for linha in arquivo_vei:
                            dados_vei = linha.strip().split(";")
                            if dados_vei[0] == placa_pro:
                                veiculo_existe = True
                except FileNotFoundError:
                    pass

                try:
                    with open("vendas.txt", "r") as arquivo_ven:
                        for linha in arquivo_ven:
                            dados_ven = linha.strip().split(";")
                            if dados_ven[3] == placa_pro:
                                veiculo_ja_vendido = True
                except FileNotFoundError:
                    # Se o arquivo de vendas não existir, significa que nenhuma venda foi feita ainda
                    pass
                # === PASSO 3: Validar as checagens ===
                if not cliente_existe:
                    print(f"❌ Erro: O cliente com CPF {cpf_cli} não está cadastrado no sistema!")
                elif not veiculo_existe:
                    print(f"❌ Erro: O veículo com placa {placa_pro} não está cadastrado no sistema!")
                elif veiculo_ja_vendido:
                    print(f"❌ Erro: O veículo com placa {placa_pro} já foi vendido anteriormente! Cadastro cancelado.")
                else:
                    # Se ambos existirem, o sistema segue o fluxo normal do cadastro da venda
                    precisa_cabecalho = False
                    linhas_existentes = 0
                    # Tentar ler o arquivo de vendas para descobrir o próximo ID
                    try:
                        with open("vendas.txt", "r") as arquivo:
                            for linha in arquivo:
                                linhas_existentes += 1
                    except FileNotFoundError:
                        precisa_cabecalho = True
                    if precisa_cabecalho:
                        venda_id = "1"
                    else:
                        venda_id = str(linhas_existentes)
                    with open("vendas.txt", "a") as arquivo:
                        if precisa_cabecalho:
                            arquivo.write("id;data;cliente;veiculo\n")
                        arquivo.write(f"{venda_id};{data};{cpf_cli};{placa_pro}\n")

                    print(f"""
                    ✅ Venda cadastrada com sucesso!
                    🪪 ID: {venda_id}
                    🕒 Data: {data}
                    👤 Cliente: {cpf_cli}
                    🚗 Veículo: {placa_pro}
                    """)
    
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_vendas)

            elif resp_venda == 2:
                os.system("clear")
                print("=== Essa opção é responsável por buscar uma venda no sistema. ===")
                id = input("Informe o ID da venda: ")
                print(f"Buscando venda com ID {id}...")
                venda = None
                cliente = None
                veiculo = None

                try:
                    with open("vendas.txt", "r") as arquivo:
                        for linha in arquivo:
                            dados = linha.strip().split(";")
                            if dados[0] == id:
                                venda = dados
                except FileNotFoundError:
                    pass

                if venda:
                    data_venda = venda[1]
                    cpf_venda = venda[2]
                    placa_venda = venda[3]

                    # === PASSO 2: Buscar o Cliente e o Veículo pelo cpf e placa ===
                    try:
                        with open("clientes.txt", "r") as arquivo_clientes:
                            for linha in arquivo_clientes:
                                dados_cli = linha.strip().split(";")
                                if dados_cli[0] == cpf_venda:
                                    cliente = dados_cli
                    except FileNotFoundError:
                        pass
                    try:
                        with open("veiculos.txt", "r") as arquivo_veiculos:
                            for linha in arquivo_veiculos:
                                dados_vei = linha.strip().split(";")
                                if dados_vei[0] == placa_venda:
                                    veiculo = dados_vei
                    except FileNotFoundError:
                        pass
                    if cliente and veiculo:
                        print(f"""
                        🪪 ID: {id}
                        🕒 Data: {data_venda}

                        === CLIENTE ===
                        👤 Nome: {cliente[1]}
                        🪪 CPF: {cliente[0]}
                        📅 Data de Nascimento: {cliente[5]}
                        📞 Telefone: {cliente[2]}
                        📧 Email: {cliente[3]}
                        📍 Cidade: {cliente[4]}

                        === VEÍCULO ===
                        🔖 Placa: {veiculo[0]}
                        📜 Categoria: {veiculo[1]}
                        🚗 Marca: {veiculo[2]}
                        🚘 Modelo: {veiculo[3]}
                        📅 Ano: {veiculo[4]}
                        🎨 Cor: {veiculo[5]}
                        📏 KM: {veiculo[6]}
                        💰 Valor: R$ {float(veiculo[7]):.2f}
                        🚘 Tipo: {veiculo[8]}
                        """)
                else:
                    print(f"Venda com ID {id} não encontrada.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_vendas)

            elif resp_venda == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar as informações de uma venda no sistema. ===")
                id = input("Informe o ID da venda que deseja editar: ")
                venda = None
                linhas = []
                try:
                    with open("vendas.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                except FileNotFoundError:
                    pass
                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == id:
                        venda = dados
                if venda:
                    print(f"""
                    🪪 ID: {id}
                    🕒 Data: {venda[1]}
                    👤 Cliente: {venda[2]}
                    print(f"🚗 Veículo: {venda[3]} """)
                    
                    editv = -1
                    while editv != 0:
                        editv = int(input("""
                        Qual informação deseja editar?
                        [1] Data
                        [2] CPF do cliente
                        [3] Placa do veículo
                        [0] Finalizar edição
                        """))
                        if editv == 1:
                            venda[1] = input("altere a data: ")
                        if editv == 1:
                            venda[1] = input("Altere a data: ")
                            
                        elif editv == 2:
                            alt_cpf_cli = input("Altere o CPF do cliente: ")
                            cliente_existe = False 
                            try:
                                with open("clientes.txt", "r") as arq_cli:
                                    for linha in arq_cli:
                                        if linha.strip().split(";")[0] == alt_cpf_cli:
                                            cliente_existe = True
                            except FileNotFoundError:
                                pass
                            if cliente_existe:
                                venda[2] = alt_cpf_cli
                                print("CPF do cliente alterado na venda!")
                            else:
                                print("❌ Erro: Cliente não encontrado no sistema!")
                        elif editv == 3:
                            alt_placa_pro = input("Altere a placa do veículo: ")
                            veiculo_existe = False
                            veiculo_ja_vendido = False
                            try:
                                with open("veiculos.txt", "r") as arq_vei:
                                    for linha in arq_vei:
                                        if linha.strip().split(";")[0] == alt_placa_pro:
                                            veiculo_existe = True
                            except FileNotFoundError:
                                pass    
                            try:
                                with open("vendas.txt", "r") as arq_ven:
                                    for linha in arq_ven:
                                        dados_ven = linha.strip().split(";")
                                        # Se a placa está em outra venda (e não é a placa que já estava nessa venda)
                                        if dados_ven[3] == alt_placa_pro and alt_placa_pro != placa_original:
                                            veiculo_ja_vendido = True
                            except FileNotFoundError:
                                pass
                                
                            if not veiculo_existe:
                                print("❌ Erro: Veículo não encontrado no sistema!")
                            elif veiculo_ja_vendido:
                                print("❌ Erro: Esse veículo já foi vendido")
                            else:
                                venda[3] = alt_placa_pro
                                print("Placa do veículo alterada na venda!")
                    print(f"""
                    Venda atualizada com Sucesso!
                    🪪 ID: {id}
                    🕒 Data: {venda[1]}
                    👤 Cliente: {venda[2]}
                    🚗 Veículo: {venda[3]}
                    """)
                else:
                    print(f"Venda com ID {id} não encontrada.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_vendas)

            elif resp_venda == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir uma venda do sistema. ===")
                id = input("Informe o ID da venda que deseja excluir: ")
                linhas = []
                try:
                    with open("vendas.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                except FileNotFoundError:
                    pass
                venda_encontrada = False
                novas_linhas = []
                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == id:
                        venda_encontrada = True
                    else:
                        novas_linhas.append(linha)

                if venda_encontrada:
                    with open("vendas.txt", "w") as arquivo:
                        arquivo.writelines(novas_linhas)
                    print(f"Venda com ID {id} excluída com Sucesso!")
                else:
                    print(f"Venda com ID {id} não encontrada.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_vendas)
    elif opcao == 4:
        resp_relatorio = -1
        os.system("clear")
        print(menu_relatorios)
        while resp_relatorio != 0:
            resp_relatorio = int(input("Digite a opção desejada do Módulo Relatórios: "))
            if resp_relatorio == 1:
                os.system("clear")
                print("=== Essa opção é responsável por gerar um relatório de veículos. ===")
                print("🚘 Relatório de Veículos 🚘")
                
                try:
                    with open("veiculos.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                    for i in range(1, len(linhas)):
                        info = linhas[i].strip().split(";")
                        print(f"""
                          Placa: {info[0]} - Marca: {info[2]} - Modelo: {info[3]} -
                          Ano: {info[4]} - Valor: R$ {float(info[7]):.2f} - Categoria: {info[1]}""")
                except FileNotFoundError:
                    print("Nenhum veículo cadastrado no sistema ainda.")

                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_relatorios)
                
            elif resp_relatorio == 2:
                os.system("clear")
                print("=== Essa opção é responsável por gerar um relatório de clientes. ===")
                print("👥 Relatório de Clientes 👥")
                
                try:
                    with open("clientes.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                    for i in range(1, len(linhas)):
                        info = linhas[i].strip().split(";")
                        print(f"""
                          CPF: {info[0]} - Nome: {info[1]} - Telefone: {info[3]} -
                          Email: {info[4]} - Cidade: {info[5]} - Data de Nascimento: {info[2]}""")
                except FileNotFoundError:
                    print("Nenhum cliente cadastrado no sistema ainda.")
                    
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_relatorios)
                
            elif resp_relatorio == 3:
                os.system("clear")
                print("=== Essa opção é responsável por gerar um relatório de vendas. ===")
                print("💰 Relatório de Vendas 💰")
    
                try:
                    with open("vendas.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                    for i in range(1, len(linhas)):
                        info = linhas[i].strip().split(";")
                        print(f"""
                        ID: {info[0]} - Data: {info[1]} - Cliente (CPF): {info[2]}
                        Veículo (Placa): {info[3]}
                        ------------------------------------------------------------""")
                except FileNotFoundError:
                    print("Nenhuma venda cadastrada no sistema ainda.")
                    
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_relatorios)
    elif opcao == 5:
        os.system("clear")
        print(menu_info)
        input("Pressione ENTER para continuar...")
        os.system("clear")
print("A sua sessão foi encerrada. Obrigada por usar a Success Car! 🚗💨")
print(aviso)
        

        
