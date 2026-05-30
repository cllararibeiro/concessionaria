import os

print("""
=========================================================
                BEM VINDO A SUCESS CAR 💫🚘
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

while opcao != 0:
    print(menu)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        os.system("clear")
        print(menu_veiculos)
        while resp!= 0:
            resp = int(input("Digite a opção desejada do Módulo Veículos: "))
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
                print("""
                    
                    🚘 Marca: Toyota
                    🚗 Modelo: Corolla
                    📅 Ano: 2022
                    🎨 Cor: Prata
                    🔖 Placa: ABC-1234
                    💰 Valor: R$ 125.000,00
                    📌 Status: Disponível
                    ℹ️ Tipo: Novo
                    
                    """)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)


            elif resp == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar as informações de um veículo no sistema. ===")
                placa = input("Informe a placa do veículo que deseja editar: ")
                alt_placa = input("altere a placa: ")
                alt_marca = input("altere a marca: ")
                alt_modelo = input("altere o modelo: ")
                alt_ano = int(input("altere o ano: "))
                alt_cor = input("altere a cor: ")
                alt_km = float(input("altere a quilometragem: "))
                alt_valor = float(input("altere o valor: "))
                alt_tipo = input("Novo ou Usado? ")
                print(f"""
                    
                    Veículo atualizado com Sucesso!
                {alt_marca}-{alt_modelo}-({alt_ano})-{alt_cor} 
                Placa: {alt_placa}]
                KM: {alt_km}
                Valor:R${alt_valor:.2f}
                Tipo: {alt_tipo}

                    """)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)
            
            elif resp == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um veículo do sistema. ===")
                placa = input("Informe a placa do veículo que deseja excluir: ")
                print(f"Veículo com placa {placa} excluído com Sucesso!")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_veiculos)
    elif opcao == 2:
        os.system("clear")
        print(menu_clientes)
        while resp_cli!= 0:
            resp_cli = int(input("Digite a opção desejada do Módulo Clientes: "))
            if resp_cli == 1:
                os.system("clear")
                print("=== Essa opção é responsável pelo cadastro do cliente ===")
                nome = input("Informe o nome: ")
                cpf = input("Informe o CPF: ")
                telefone = input("Informe o telefone: ")
                email = input("Informe o email: ")
                cidade = input("Informe a cidade: ")
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
                print("""
                    
                    👤 Nome: João Silva
                    🪪 CPF: 123.456.789-00
                    📞 Telefone: (11) 98765-4321
                    📧 Email: user@gmail.com """)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)
            elif resp_cli == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar as informações de um cliente no sistema. ===")
                cpf = input("Informe o CPF do cliente que deseja editar: ")
                alt_nome = input("altere o nome: ")
                alt_cpf = input("altere o CPF: ")
                alt_telefone = input("altere o telefone: ")
                alt_email = input("altere o email: ")
                alt_cidade = input("altere a cidade: ")
                print(f"""
                    
                    Cliente atualizado com Sucesso!
                👤 Nome: {alt_nome}
                🪪 CPF: {alt_cpf}
                📞 Telefone: {alt_telefone}
                📧 Email: {alt_email}
                📍 Cidade: {alt_cidade}

                    """)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)
            elif resp_cli == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um cliente do sistema. ===")
                cpf = input("Informe o CPF do cliente que deseja excluir: ")
                print(f"Cliente com CPF {cpf} excluído com Sucesso!")
                input("Pressione ENTER para continuar...")
                os.system("clear")
                print(menu_clientes)
    elif opcao == 3:
        os.system("clear")
        print(menu_vendas)
        while resp_venda!= 0:
            resp_venda = int(input("Digite a opção desejada do Módulo Vendas: "))
            print(aviso)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            print(menu_vendas)
    elif opcao == 4:
        os.system("clear")
        print(menu_relatorios)
        while resp_relatorio!= 0:
            resp_relatorio = int(input("Digite a opção desejada do Módulo Relatórios: "))
            print(aviso)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            print(menu_relatorios)
    elif opcao == 5:
        os.system("clear")
        print(menu_info)
        input("Pressione ENTER para continuar...")
        os.system("clear")
print("A sua sessão foi encerrada. Obrigada por usar a Sucess Car! 🚗💨")
print(aviso)
        

        
