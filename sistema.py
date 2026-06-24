
import os
from bibliotecas.procedimentos import *
from bibliotecas.veiculos import *
from bibliotecas.clientes import *
from bibliotecas.vendas import *
from bibliotecas.relatorios import *

boas_vindas()

while True:
    os.system("clear")
    menu()
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
            print("❌ Erro: Por favor, digite apenas números!")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu()
            continue 
    if opcao == 0:
        print("A sua sessão foi encerrada. Obrigada por usar a Success Car! 🚗💨")
        break
    elif opcao == 1:
        modulo_veiculos()
    elif opcao == 2:
        modulo_clientes()
    elif opcao == 3:
        modulo_vendas()
    elif opcao == 4:
       modulo_relatorios()
    elif opcao == 5:
        os.system("clear")
        menu_info()
        input("Pressione ENTER para continuar...")
        os.system("clear")
    else:
        print("⚠️ Opção inválida! Escolha um número que esteja no menu.")
        input("Pressione ENTER para tentar novamente...")
        os.system("clear")
        menu()
    