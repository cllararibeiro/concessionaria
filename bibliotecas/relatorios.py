import os
from bibliotecas.geral import *
from bibliotecas.clientes  import *
from bibliotecas.vendas import *
from bibliotecas.veiculos import *
from bibliotecas.procedimentos import *

def modulo_relatorios():
    while True:
        os.system("clear")
        menu_relatorios()
        try:
            resp = int(input("Digite a opção desejada do Módulo Relatórios: "))
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números!")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_relatorios()
            continue 
        if resp == 0:
            return
        if resp == 1:
            gerenciar_veiculos()   
        elif resp  == 2:
            gerenciar_clientes()   
        elif resp == 3:
            gerenciar_vendas()
        else:
            print("⚠️ Opção inválida! Escolha um número que esteja no menu.")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_relatorios()

#encontra os respectivos dados desejados através do indice
def filtrar_dados(arquivo, indice, termo_busca, funcao):
    linhas = ler_arquivo(arquivo)
    resultados = False
    
    for i in range(1, len(linhas)):
        dados = linhas[i].strip().split(";")
        if termo_busca.lower() == "todos":
            funcao(dados)
            print("-" * 50)
            resultados = True
        else:
            coluna = dados[indice].strip().lower()
            if coluna == termo_busca.lower():
                funcao(dados)
                print("-" * 50)
                resultados = True

    return resultados


def exibir_relatorio_veiculos():
    os.system("clear")
    print("=== 🚘 Relatório de Todos Veículos 🚘 ===")
    achou = filtrar_dados("veiculos.txt", 0, "todos", exibir_veiculo)
    if not achou:
        print("Nenhum veículo cadastrado no sistema ainda.")
    input("\nPressione ENTER para continuar...")

def exibir_relatorio_clientes():
    os.system("clear")
    print("=== 👥 Relatório de Todos os Clientes 👥 ===")
    achou = filtrar_dados("clientes.txt", 6, "Ativo", exibir_cliente)
    if not achou:
        print("Nenhum cliente cadastrado no sistema ainda.")    
    input("\nPressione ENTER para continuar...")

def exibir_relatorio_vendas():
    os.system("clear")
    print("💰 Relatório de Vendas 💰")
    achou = filtrar_dados("vendas.txt", 0, "todos", exibir_venda)
    if not achou:
        print("Nenhuma venda cadastrada no sistema ainda.")
    input("\nPressione ENTER para continuar...")


def relatorio_aniversariantes_mes():
    os.system("clear")
    print("=== 🎂 Aniversariantes do Mês 🎂 ===")
    mes = input("Digite o número do mês (01 a 12): ").strip()
    if len(mes) == 1: 
        mes = "0" + mes
    linhas = ler_arquivo("clientes.txt")
    resultados = False
    
    for i in range(1, len(linhas)):
        cliente = linhas[i].strip().split(";")
        data_nasc = cliente[5] 
        if data_nasc[3:5] == mes:  
            if cliente[6] != "Desativado":
                exibir_cliente(cliente)
                print("-" * 50)
                resultados = True
                
    if not resultados: 
        print("Nenhum aniversariante neste mês.")
    input("\nPressione ENTER para continuar...")

def exibir_cliente_ativo(cliente):
    if not (len(cliente) > 6 and cliente[6] == "Desativado"):
        exibir_cliente(cliente)
        print("-" * 50)


def relatorio_clientes_por_cidade():
    os.system("clear")
    print("=== 🏙️ Filtro de Clientes por Cidade ===")
    cidade = input("Digite a cidade: ").strip()
    achou = filtrar_dados("clientes.txt", 4, cidade, exibir_cliente_ativo)
    
    if not achou:
        print(f"❌ Nenhum cliente encontrado na cidade: {cidade}")
    input("\nPressione ENTER para continuar...")


def relatorio_clientes_por_cidade():
    os.system("clear")
    print("=== 🏙️ Filtro de Clientes por Cidade ===")
    cidade_buscada = input("Digite a cidade: ").strip().lower()
    linhas = ler_arquivo("clientes.txt")
    resultados = False
    for i in range(1, len(linhas)):
        cliente = linhas[i].strip().split(";")
        if len(cliente) > 6 and cliente[6] == "Desativado":
            continue   
        cidade_cliente = cliente[4].strip().lower()
        if cidade_cliente == cidade_buscada:
            exibir_cliente(cliente)
            print("-" * 50)
            resultados = True
            
    if not resultados:
        print(f"❌ Nenhum cliente ativo encontrado na cidade: {cidade_buscada.capitalize()}")
    input("\nPressione ENTER para continuar...")

def gerenciar_clientes():
    opcao = -1
    while opcao != 0:
        os.system("clear")
        relatorios_clientes()
        opcao = int(input("Digite a opção desejada do Módulo Relatórios Clientes: "))
        if opcao == 1:
            exibir_relatorio_clientes()   
        elif opcao == 2:
            relatorio_aniversariantes_mes() 
        elif opcao == 3:
            relatorio_clientes_por_cidade()

def gerenciar_veiculos():
    opcao = -1
    while opcao != 0:
        os.system("clear")
        relatorios_veiculos() 
        opcao = int(input("Digite a opção desejada do Módulo Relatórios Veículos: "))
        
        if opcao == 1:exibir_relatorio_veiculos() 
        elif opcao == 2: veiculos_ano()
        elif opcao == 3: veiculos_cor()
        elif opcao == 4: veiculos_marca()
        elif opcao == 5: veiculos_categoria()
        elif opcao == 6: veiculos_tipo()
        elif opcao == 7: veiculos_estado()
        os.system("clear")

def gerenciar_vendas():
    opcao = -1
    while opcao != 0:
        os.system("clear")
        relatorios_vendas()
        opcao = int(input("Digite a opção desejada do Módulo Relatórios de Vendas: "))
        if opcao == 1: 
            exibir_relatorio_vendas()
        elif opcao == 2:
            intervalo_vendas()
        elif opcao == 3: 
            vendas_anual()
        elif opcao == 4: 
            filtro_pagamento()
        os.system("clear")

def intervalo_vendas():
    os.system("clear")
    print("=== 📅 Listar Vendas por Ano ===")
    ano = input("Digite o ano desejado (Ex: 2026): ").strip()

    ano_valido = processar_ano(ano)

    if ano_valido is None:
        print("\n⚠️ Ano inválido! Digite um ano real entre 1886 e o próximo ano.")
        input("\nPressione ENTER para tentar novamente...")
        return 

    linhas = ler_arquivo("vendas.txt")
    achou = False

    for i in range(1, len(linhas)):
        venda = linhas[i].strip().split(";")
        data_venda = venda[1]
        ano_venda = data_venda[6:10] 

        if ano_venda == ano_valido:
            exibir_venda(venda)
            print("-" * 50)
            achou = True

    if not achou:
        print(f"❌ Nenhuma venda realizada no ano de {ano_valido}.")
        
    input("\nPressione ENTER para continuar...")

def veiculos_ano():
    os.system("clear")
    print("=== 📅 Filtrar Veículos por Ano ===")
    ano = input("Digite o ano desejado (ex: 2026): ").strip()
    achou = filtrar_dados("veiculos.txt", 4, ano, exibir_veiculo)
    if not achou:
        print(f"❌ Nenhum veículo encontrado do ano {ano}.")
    input("\nPressione ENTER para continuar...")

def veiculos_cor():
    os.system("clear")
    print("=== 🎨 Filtrar Veículos por Cor ===")
    cor = input("Digite a cor desejada: ").strip().lower()
    achou = filtrar_dados("veiculos.txt", 5, cor, exibir_veiculo)
    if not achou:
        print("Nenhum veículo encontrado com esta cor.")
    input("\nPressione ENTER para continuar...")

def veiculos_marca():
    os.system("clear")
    print("=== 🏷️ Filtrar Veículos por Marca ===")
    marca = input("Digite a marca (ex: Fiat, Ford): ").strip().lower()
    achou = filtrar_dados("veiculos.txt", 2, marca, exibir_veiculo)
    if not achou:
        print("Nenhum veículo encontrado desta marca.")
    input("\nPressione ENTER para continuar...")


def veiculos_categoria():
    os.system("clear")
    print("=== 🗂️ Filtrar Veículos por Categoria ===")
    categoria = input("Digite a categoria (ex: Carro, Moto...): ").strip().lower()
    achou = filtrar_dados("veiculos.txt", 1, categoria, exibir_veiculo)
    if not achou:
        print("Nenhum veículo encontrado nesta categoria.")
    input("\nPressione ENTER para continuar...")

def veiculos_tipo():
    os.system("clear")
    print("=== 🚙 Filtrar Veículos por Tipo ===")
    tipo= input("Digite o tipo (Novo / Usado): ").strip().lower()
    achou = filtrar_dados("veiculos.txt", 8, tipo, exibir_veiculo)
    if not achou:
        print("Nenhum veículo encontrado deste tipo.")
    input("\nPressione ENTER para continuar...")

def veiculos_estado():
    os.system("clear")
    print("=== 🚙 Filtrar Veículos por Status ===")
    status = input("Digite o status (Vendido / Disponível): ").strip().lower()
    achou = filtrar_dados("veiculos.txt", 9, status, exibir_veiculo)
    if not achou:
        print("Nenhum veículo encontrado")
    input("\nPressione ENTER para continuar...")

def dicionario_veiculos():
    linhas = ler_arquivo("veiculos.txt")
    veiculos = {}
    for i in range(1, len(linhas)):
        v = linhas[i].strip().split(";")
        placa = v[0].strip()
        veiculos[placa] = {
            "marca": v[2].strip().capitalize(),
            "cor": v[5].strip().capitalize(),
            "valor": float(v[7].strip())
        }
    return veiculos

def vendas_do_ano(ano, veiculos):
    linhas = ler_arquivo("vendas.txt")
    faturamento = 0.0
    marcas = {}
    cores = {}
    total_vendas = 0

    for i in range(1, len(linhas)):
        venda = linhas[i].strip().split(";")
        ano_venda = venda[1][6:10]

        if ano_venda == ano:
            placa = venda[3].strip()
            if placa in veiculos:
                total_vendas += 1
                faturamento += veiculos[placa]["valor"]
                marca = veiculos[placa]["marca"]
                if marca in marcas:
                    marcas[marca] += 1       
                else:
                    marcas[marca] = 1       
                
                cor = veiculos[placa]["cor"]
                if cor in cores:
                    cores[cor] += 1       
                else:
                    cores[cor] = 1        

    return total_vendas, faturamento, marcas, cores

def relatorio_anual_venda(ano, total_vendas, faturamento, marcas, cores):
    marca_campea = max(marcas, key=marcas.get)
    cor_campea = max(cores, key=cores.get)

    print(f"\n📊 BALANÇO GERAL DO ANO DE {ano}")
    print("=" * 50)
    print(f"💰 Total Arrecadado:      R$ {faturamento:.2f}")
    print(f"🚗 Quantidade de Vendas:  {total_vendas} veículo(s)")
    print(f"🏷️ Marca Mais Vendida:    {marca_campea} ({marcas[marca_campea]} vendas)")
    print(f"🎨 Cor Mais Vendida:      {cor_campea} ({cores[cor_campea]} vendas)")
    print("=" * 50)

def vendas_anual():
    os.system("clear")
    print("=== 📈 Relatório Geral Anual ===")
    ano = input("Digite o ano para o balanço (ex: 2026): ")

    ano_valido = processar_ano(ano)
    if ano_valido is None:
        print("\n⚠️ Ano inválido! Digite um ano real entre 1886 e o próximo ano.")
        input("\nPressione ENTER para voltar...")
        return

    veiculos = dicionario_veiculos()
    
    total_vendas, faturamento, marcas, cores = vendas_do_ano(ano_valido, veiculos)

    if total_vendas > 0:
        relatorio_anual_venda(ano_valido, total_vendas, faturamento, marcas, cores)
    else:
        print(f"\n❌ Não foram encontradas vendas registradas no ano {ano_valido}.")

    input("\nPressione ENTER para continuar...")

def mapear_pagamento():
    vendas = ler_arquivo("vendas.txt")
    mapa_pagamentos = {
        "Dinheiro": [],
        "Cartão": [],
        "Pix": [],
        "Financiamento":[]
    }

    for linha in vendas:
        venda = linha.strip().split(";")
        status = venda[5]
        forma_pgto = venda[4] 
        if status == "Concluída":
            mapa_pagamentos[forma_pgto].append(venda)
    return mapa_pagamentos

def filtro_pagamento():
    os.system("clear")
    vendas = mapear_pagamento()
    print("""
    === Filtrar Vendas por Forma de Pagamento ===
    [1] 💵 Dinheiro
    [2] 💳 Cartão de Crédito/Débito
    [3] 📱 Pix
    [4] 💰 Financiamento
    """)
    opcao = int(input("Escolha uma opção: "))
    chaves = {1: "Dinheiro", 2: "Cartao", 3: "Pix", 4: "Financiamento"}
    chave = chaves.get(opcao)

    if chave:
        lista_filtrada = vendas[chave]
        print(f"\n📋 === Vendas via {chave} ===")
        if not lista_filtrada:
            print("Nenhuma venda encontrada para esta forma de pagamento.")
        else:
            for venda in lista_filtrada:
                exibir_venda(venda)
        input("\nPressione ENTER para continuar...") 
        
    else:
        print("Opção inválida!")
        input("\nPressione ENTER para continuar...") # Também segura o aviso de opção inválida