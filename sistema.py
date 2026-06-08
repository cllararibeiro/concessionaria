
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

opcao = ""
resp = ""
resp_cli = ""
resp_venda = ""
resp_relatorio = ""

#Armazenamento de dados
veiculos = {"ABC-1234": {"marca": "Toyota", "modelo": "Corolla", 
                         "ano": 2022, "cor": "Prata", "km": 15000, 
                         "valor": 125000.00, "tipo": "Novo"},
            "DEF-5678": {"marca": "Honda", "modelo": "Civic", 
                         "ano": 2021, "cor": "Preto", "km": 30000, 
                         "valor": 110000.00, "tipo": "Usado"}}

clientes = {"123.456.789-00": {"nome": "João Silva", "telefone": "(11) 98765-4321", 
                            "email": "joao.silva@email.com", "cidade":"São Fernando"},
            "145.677.890-00": {"nome": "Maria Oliveira", "telefone": "(21) 91234-5678", 
                               "email": "maria.oliveira@email.com", "cidade": "Caicó"}}

vendas = {"1": {"data": "01/01/2024", "cliente": "123.456.789-00", "veiculo": "ABC-1234"},
         "2": {"data": "15/02/2024", "cliente": "145.677.890-00", "veiculo": "DEF-5678"}}


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
                marca = input("Informe a marca: ")
                modelo = input("Informe o modelo: ")
                ano = int(input("Informe o ano: "))
                cor = input("Informe a cor: ")
                placa = input("Informe a placa: ")
                km = float(input("Informe a quilometragem: "))
                valor = float(input("Informe o valor: "))
                tipo = input("Novo ou Usado? ")

                veiculos[placa] = {"marca": marca,"modelo": modelo,
                "ano": ano,"cor": cor,"km": km,"valor": valor,"tipo": tipo}
                
                print(f"""
                Veículo cadastrado com Sucesso!
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
                if placa in veiculos:
                    v = veiculos[placa]
                    print(f"""
                    
                    🚘 Marca: {v['marca']}
                    🚗 Modelo: {v['modelo']}
                    📅 Ano: {v['ano']}
                    🎨 Cor: {v['cor']}
                    🔖 Placa: {placa}
                    💰 Valor: R$ {v['valor']:.2f}
                    📌 Status: Disponível
                    ℹ️ Tipo: {v['tipo']}
                    
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
                if placa in veiculos:
                    print(f"""
                    🔖 Placa: {placa}
                    🚘 Marca: {veiculos[placa]['marca']}
                    🚗 Modelo: {veiculos[placa]['modelo']}
                    📅 Ano: {veiculos[placa]['ano']}
                    🎨 Cor: {veiculos[placa]['cor']}
                    ℹ️ KM: {veiculos[placa]['km']}
                    💰 Valor: R$ {veiculos[placa]['valor']:.2f}
                    📌 Tipo: {veiculos[placa]['tipo']}
                    """)
                    editc = ""
                    while editc !=0:
                        editc = int(input("""
                        Qual informação deseja editar?
                        [1] Marca
                        [2] Modelo
                        [3] Ano
                        [4] Cor
                        [5] Placa
                        [6] Quilometragem
                        [7] Valor
                        [8] Tipo (Novo ou Usado)
                        [0] Finalizar edição
                        """))
                        if editc == 1:
                            alt_marca = input("altere a marca: ")
                            veiculos[placa]['marca'] = alt_marca
                        elif editc == 2:
                            alt_modelo = input("altere o modelo: ")
                            veiculos[placa]['modelo'] = alt_modelo
                        elif editc == 3:
                            alt_ano = int(input("altere o ano: "))
                            veiculos[placa]['ano'] = alt_ano
                        elif editc == 4:
                            alt_cor = input("altere a cor: ")
                            veiculos[placa]['cor'] = alt_cor
                        elif editc == 5:
                            alt_placa = input("altere a placa: ")
                            veiculos[alt_placa] = veiculos.pop(placa)
                            placa = alt_placa
                        elif editc == 6:
                            alt_km = float(input("altere a quilometragem: "))
                            veiculos[placa]['km'] = alt_km
                        elif editc == 7:
                            alt_valor = float(input("altere o valor: "))
                            veiculos[placa]['valor'] = alt_valor
                        elif editc == 8:
                            alt_tipo = input("Novo ou Usado? ")
                            veiculos[placa]['tipo'] = alt_tipo
                    print(f"""Veículo atualizado com Sucesso!
                           🔖 Placa: {placa}
                            🚘 Marca: {veiculos[placa]['marca']}
                            🚗 Modelo: {veiculos[placa]['modelo']}
                            📅 Ano: {veiculos[placa]['ano']}
                            🎨 Cor: {veiculos[placa]['cor']}
                            ℹ️ KM: {veiculos[placa]['km']}
                            💰 Valor: R$ {veiculos[placa]['valor']:.2f}
                            📌 Tipo: {veiculos[placa]['tipo']}""")
                else:
                    print(f"Veículo com placa {placa} não encontrado.")
               
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)
            
            elif resp == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um veículo do sistema. ===")
                placa = input("Informe a placa do veículo que deseja excluir: ")
                if placa in veiculos:
                    del veiculos[placa]
                    print(f"Veículo com placa {placa} excluído com Sucesso!")
                else:
                    print(f"Veículo com placa {placa} não encontrado.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)
    elif opcao == 2:
        os.system("clear")
        print(menu_clientes)
        while resp_cli!= 0:
            resp_cli = ""
            resp_cli = int(input("Digite a opção desejada do Módulo Clientes: "))
            if resp_cli == 1:
                os.system("clear")
                print("=== Essa opção é responsável pelo cadastro do cliente ===")
                nome = input("Informe o nome: ")
                cpf = input("Informe o CPF: ")
                telefone = input("Informe o telefone: ")
                email = input("Informe o email: ")
                cidade = input("Informe a cidade: ")
                clientes[cpf] = {"nome": nome, "telefone": telefone, "email": email, "cidade": cidade}
                print(f"""
                ✅ Cliente cadastrado com sucesso!

                👤 Nome: {nome}
                🪪 CPF: {cpf}
                📞 Telefone: {telefone}
                📧 Email: {email}
                📍 Cidade: {cidade}

                """)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)
            elif resp_cli == 2:
                os.system("clear")
                print("=== Essa opção é responsável por buscar um cliente no sistema. ===")
                cpf = input("Informe o CPF do cliente: ")
                print(f"Buscando cliente com CPF {cpf}...")
                if cpf in clientes:
                    cliente = clientes[cpf]
                    print(f"""
                        
                        👤 Nome: {cliente['nome']}
                        🪪 CPF: {cpf}
                        📞 Telefone: {cliente['telefone']}
                        📧 Email: {cliente['email']}
                        📍 Cidade: {cliente['cidade']}
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
                if cpf in clientes:
                    print(f"""
                            👤 Nome: {clientes[cpf]['nome']}
                            🪪 CPF: {cpf}
                            📞 Telefone: {clientes[cpf]['telefone']}
                            📧 Email: {clientes[cpf]['email']}
                            📍 Cidade: {clientes[cpf]['cidade']}
                            """)
                    edit = ""
                    while edit !=0:
                        edit = int(input("""
                        Qual informação deseja editar?
                        [1] Nome
                        [2] CPF
                        [3] Telefone
                        [4] Email
                        [5] Cidade
                        [0] Finalizar edição
                        """))
                        if edit == 1:
                            alt_nome = input("altere o nome: ")
                            clientes[cpf]['nome'] = alt_nome
                        elif edit == 2:
                            alt_cpf = input("altere o CPF: ")
                            clientes[alt_cpf] = clientes.pop(cpf)
                            cpf = alt_cpf 
                        elif edit == 3:
                            alt_telefone = input("altere o telefone: ")
                            clientes[cpf]['telefone'] = alt_telefone
                        elif edit == 4:
                            alt_email = input("altere o email: ")
                            clientes[cpf]['email'] = alt_email
                        elif edit == 5:
                            alt_cidade = input("altere a cidade: ")
                            clientes[cpf]['cidade'] = alt_cidade
                print(f"""
                    Cliente atualizado com Sucesso!
                👤 Nome: {clientes[cpf]['nome']}
                🪪 CPF: {cpf}
                📞 Telefone: {clientes[cpf]['telefone']}
                📧 Email: {clientes[cpf]['email']}
                📍 Cidade: {clientes[cpf]['cidade']}
                    """)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)
            elif resp_cli == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um cliente do sistema. ===")
                cpf = input("Informe o CPF do cliente que deseja excluir: ")
                if cpf in clientes:
                    del clientes[cpf]
                    print(f"Cliente com CPF {cpf} excluído com Sucesso!")
                else:
                    print(f"Cliente com CPF {cpf} não encontrado.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)
    elif opcao == 3:
        os.system("clear")
        print(menu_vendas)
        while resp_venda!= 0:
            resp_venda = ""
            resp_venda = int(input("Digite a opção desejada do Módulo Vendas: "))
            if resp_venda == 1:
                os.system("clear")
                print("=== Essa opção é responsável pelo cadastro de uma venda ===")
                cpf_cli = input("Informe o CPF do cliente: ")
                placa_pro = input("Informe a placa do veículo: ")
                data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                venda_id = str(len(vendas) + 1)
                vendas[venda_id] = {"data": data, "cliente": cpf_cli, "veiculo": placa_pro}
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
                if id in vendas:
                    venda = vendas[id]
                    cpf = venda["cliente"]
                    placa = venda["veiculo"]
                    print(f"""
                        🪪 ID: {id}
                        🕒 Data: {venda['data']}

                        === CLIENTE ===
                        👤 Nome: {clientes[cpf]['nome']}
                        🪪 CPF: {cpf}
                        📞 Telefone: {clientes[cpf]['telefone']}
                        📧 Email: {clientes[cpf]['email']}
                        📍 Cidade: {clientes[cpf]['cidade']}

                        === VEÍCULO ===
                        🚗 Marca: {veiculos[placa]['marca']}
                        🚘 Modelo: {veiculos[placa]['modelo']}
                        📅 Ano: {veiculos[placa]['ano']}
                        🎨 Cor: {veiculos[placa]['cor']}
                        📏 KM: {veiculos[placa]['km']}
                        💰 Valor: R$ {veiculos[placa]['valor']}
                        🔖 Placa: {placa}
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
                if id in vendas:
                    
                    print(f"""
                    🪪 ID: {id}
                    🕒 Data: {vendas[id]['data']}
                    👤 Cliente: {vendas[id]['cliente']}
                    🚗 Veículo: {vendas[id]['veiculo']}
                    """)
                    
                    editv = ""
                    while editv !=0:
                        editv = int(input("""
                        Qual informação deseja editar?
                        [1] Data
                        [2] CPF do cliente
                        [3] Placa do veículo
                        [0] Finalizar edição
                        """))
                        if editv == 1:
                            alt_data = input("altere a data: ")
                            vendas[id]['data'] = alt_data
                        elif editv == 2:
                            alt_cpf_cli = input("Altere o CPF do cliente: ")
                            if alt_cpf_cli in clientes:
                                vendas[id]['cliente'] = alt_cpf_cli
                            else:
                                print("Cliente não encontrado!")
                        elif editv == 3:
                            alt_placa_pro = input("Altere a placa do veículo: ")

                            if alt_placa_pro in veiculos:
                                vendas[id]['veiculo'] = alt_placa_pro
                            else:
                                print("Veículo não encontrado!")
    
                    print(f"""
                    Venda atualizada com Sucesso!
                    🪪 ID: {id}
                    🕒 Data: {vendas[id]['data']}
                    👤 Cliente: {vendas[id]['cliente']}
                    🚗 Veículo: {vendas[id]['veiculo']}
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
                if id in vendas:
                    del vendas[id]
                    print(f"Venda com ID {id} excluída com Sucesso!")
                else:
                    print(f"Venda com ID {id} não encontrada.")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_vendas)
    elif opcao == 4:
        os.system("clear")
        print(menu_relatorios)
        while resp_relatorio!= 0:
            resp_relatorio = ""
            resp_relatorio = int(input("Digite a opção desejada do Módulo Relatórios: "))
            if resp_relatorio == 1:
                os.system("clear")
                print("=== Essa opção é responsável por gerar um relatório de veículos. ===")
                print("🚘 Relatório de Veículos 🚘")
                for placa, info in veiculos.items():
                    print(f"""
                          Placa: {placa} - Marca: {info['marca']} - Modelo: {info['modelo']} -
                          Ano: {info['ano']} - Valor: R$ {info['valor']:.2f}""")

                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_relatorios)
            elif resp_relatorio == 2:
                os.system("clear")
                print("=== Essa opção é responsável por gerar um relatório de clientes. ===")
                print("👥 Relatório de Clientes 👥")
                for cpf, info in clientes.items():
                    print(f"""
                          CPF: {cpf} - Nome: {info['nome']} - Telefone: {info['telefone']} -
                          Email: {info['email']} - Cidade: {info['cidade']}""")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_relatorios)
            elif resp_relatorio == 3:
                os.system("clear")
                print("=== Essa opção é responsável por gerar um relatório de vendas. ===")
                print("💰 Relatório de Vendas 💰")
                for id, info in vendas.items():
                    print(f"""
                        ID: {id} - Data: {info['data']} - Cliente: {info['cliente']}
                        Veículo: {info['veiculo']}
                        """)
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
        

        
