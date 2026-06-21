# Relatório aniversariante do mês
# mês com mais vendas de cada ano
# relatorio veiculos por categoria, faixa de preco
# Adicionar um status de venda no veiculo
import os
from procedimentos import *
from veiculos import *
from clientes import *
from vendas import *
from relatorios import *

boas_vindas()

opcao = -1

while opcao != 0:
    menu()
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        resp = -1
        os.system("clear")
        menu_veiculos()
        while resp!= 0:
            resp = int(input("Digite a opção desejada do Módulo Veículos: "))
            print("resposta: ", resp)
            input("Pressione ENTER para continuar...")

            if resp == 1:
                os.system("clear")
                print("=== Essa opção é responsável por cadastrar um novo veículo no sistema. ===")
                cadastrar_veiculo()
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_veiculos()

            elif resp == 2:
                os.system("clear")
                print("=== Essa opção é responsável por buscar um veículo no sistema. ===")

                placa = input("Informe a placa do veículo: ")
                print(f"Buscando veículo com placa {placa}...\n")

                veiculo = buscar_veiculo(placa)
                exibir_veiculo(veiculo)

                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_veiculos()

            elif resp == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar as informações de um veículo no sistema. ===")
                placa = input("Informe a placa do veículo que deseja editar: ")
                editar_veiculo(placa)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_veiculos()

            elif resp == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um veículo do sistema. ===")
                placa = input("Informe a placa do veículo que deseja excluir: ")
                excluir_veiculo(placa)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_veiculos()

    elif opcao == 2:
        resp_cli = -1
        os.system("clear")
        menu_clientes()
        while resp_cli!= 0:
            resp_cli = int(input("Digite a opção desejada do Módulo Clientes: "))
            if resp_cli == 1:
                os.system("clear")
                print("=== Essa opção é responsável pelo cadastro do cliente ===")
                cadastrar_cliente()
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_clientes()

            elif resp_cli == 2:
                os.system("clear")
                print("=== Essa opção é responsável por buscar um cliente no sistema. ===")
                cpf = input("Informe o CPF do cliente: ")
                cliente = buscar_cliente(cpf)
                print(f"Buscando cliente com CPF {cpf}...")
                exibir_cliente(cliente)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_clientes()

            elif resp_cli == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar as informações de um cliente no sistema. ===")
                cpf = input("Informe o CPF do cliente que deseja editar: ")
                editar_cliente(cpf)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_clientes()

            elif resp_cli == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um cliente do sistema. ===")
                cpf = input("Informe o CPF do cliente que deseja excluir: ")
                excluir_cliente(cpf)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_clientes()

    elif opcao == 3:
        resp_venda = -1
        os.system("clear")
        menu_vendas()
        while resp_venda!= 0:
            resp_venda = int(input("Digite a opção desejada do Módulo Vendas: "))
            if resp_venda == 1:
                os.system("clear")
                cadastrar_venda()
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_vendas()

            elif resp_venda == 2:
                os.system("clear")
                print("=== Essa opção é responsável por buscar uma venda no sistema. ===")
                id = input("Informe o ID da venda: ")
                venda = buscar_venda(id)
                print(f"Buscando venda com ID {id}...")
                exibir_venda(venda)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_vendas()

            elif resp_venda == 3:
                os.system("clear")
                editar_venda()
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_vendas()

            elif resp_venda == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir uma venda do sistema. ===")
                id = input("Informe o ID da venda que deseja excluir: ")
                excluir_venda(id)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_vendas()
    elif opcao == 4:
       modulo_relatorios()
    elif opcao == 5:
        os.system("clear")
        menu_info()
        input("Pressione ENTER para continuar...")
        os.system("clear")
print("A sua sessão foi encerrada. Obrigada por usar a Success Car! 🚗💨")
aviso()
    