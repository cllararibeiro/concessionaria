from bibliotecas.geral import *
import os
from bibliotecas.procedimentos import *

def modulo_veiculos():
    os.system("clear")
    menu_veiculos()
    while True:
        try:
            resp = int(input("Digite a opção desejada do Módulo Veículos: "))
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números!")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_veiculos()
            continue 
        if resp == 0:
            return #volta pro menu principal

        elif resp == 1:
            os.system("clear")
            print("=== Essa opção é responsável por cadastrar um veículo no sistema ===")
            cadastrar_veiculo()
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_veiculos()

        elif resp == 2:
            os.system("clear")
            print("=== Essa opção é responsável por buscar um veículo no sistema ===")
            placa = input("Informe a placa do veículo que deseja buscar: ")
            veiculo = buscar_veiculo(placa)
            exibir_veiculo(veiculo)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_veiculos()

        elif resp == 3:
                os.system("clear")
                print("=== Essa opção é responsável por editar um veículo no sistema ===")
                placa = input("Informe a placa do veículo que deseja editar: ")
                editar_veiculo(placa)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_veiculos()

        elif resp == 4:
                os.system("clear")
                print("=== Essa opção é responsável por excluir um veículo do sistema ===")
                placa = input("Informe a placa do veículo que deseja excluir: ")
                excluir_veiculo(placa)
                input("Pressione ENTER para continuar...")
                os.system("clear")
                menu_veiculos()
        else:
            print("⚠️ Opção inválida! Escolha um número que esteja no menu.")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_veiculos()

def buscar_veiculo(placa):
    return buscar_objeto("veiculos.txt", placa)

def exibir_veiculo(veiculo):
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
        📋 Status: {veiculo[9]}
        """)
    else:
        print("❌ Veículo não encontrado.")


def cadastrar_veiculo():
    placa = input("Informe a placa: ")
    veiculo_existente = buscar_veiculo(placa)
    
    if veiculo_existente:
        print(f"Veículo com placa {placa} já existe no sistema. Cadastro cancelado.")
        return 
    
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
    ano = processar_ano(input("Informe o ano do veículo (AAAA): "))
    if not ano:
        print("❌  Erro: Ano inválido! Digite um ano com 4 dígitos reais.")
        return
    cor = input("Informe a cor: ")
    km = float(input("Informe a quilometragem: "))
    valor = float(input("Informe o valor: "))
    tipo = input("Novo ou Usado? ")
    status = "Disponível"

    linhas = ler_arquivo("veiculos.txt")
    if len(linhas) == 0:
        adicionar_linha("veiculos.txt", "placa;categoria;marca;modelo;ano;cor;km;valor;tipo;status\n")
    nova_linha = f"{placa};{categoria};{marca};{modelo};{ano};{cor};{km};{valor};{tipo};{status}\n"
    adicionar_linha("veiculos.txt", nova_linha)
    
    print("✨ Veículo cadastrado com Sucesso! ✨")
    veiculo = buscar_veiculo(placa)
    exibir_veiculo(veiculo)

def menu_edicaov(veiculo, placa_original):
    editv = -1
    while editv != 0:
        editv = int(input("""
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
        > """))

        if editv == 1:
            veiculo[2] = input("Altere a marca: ")
        elif editv == 2:
            veiculo[3] = input("Altere o modelo: ")
        elif editv == 3:
            ano = processar_ano(input("Informe o ano do veículo (AAAA): "))
            if not ano:
                print("❌  Erro: Ano inválido! Digite um ano com 4 dígitos reais.")
                continue
            veiculo[4] = ano
        elif editv == 4:
            veiculo[5] = input("Altere a cor: ")
        elif editv == 5:
            nova_placa = input("Altere a placa: ")
            if nova_placa == "placa":
                print("Nome inválido! 'placa' é uma palavra reservada do sistema.")
            elif nova_placa == placa_original:
                veiculo[0] = nova_placa
            else:
                if buscar_veiculo(nova_placa):
                    print("Já existe um veículo com essa placa!")
                else:
                    veiculo[0] = nova_placa
        elif editv == 6:
            veiculo[6] = input("Altere a quilometragem: ")
        elif editv == 7:
            veiculo[7] = input("Altere o valor: ")
        elif editv == 8:
            veiculo[8] = input("Novo ou Usado? ")
        elif editv == 9:
            veiculo[1] = input("Altere a categoria: ")

def editar_veiculo(placa):
    veiculo = buscar_veiculo(placa)

    if veiculo:
        exibir_veiculo(veiculo)
        placa_original = placa
        menu_edicaov(veiculo, placa_original)

        linhas = ler_arquivo("veiculos.txt")
        linhas_atualizadas = atualizar_linha(linhas, placa, veiculo)
        salvar_arquivo("veiculos.txt",linhas_atualizadas)
        print("Veículo atualizado com sucesso!")
    else:
        print(f"Veículo com placa {placa} não encontrado.")

def excluir_veiculo(placa):
    if buscar_veiculo(placa):
        linhas_atuais = ler_arquivo("veiculos.txt")
        novas_linhas = obter_linhas(linhas_atuais, placa)
        salvar_arquivo("veiculos.txt",novas_linhas)
        print(f"Veículo com placa {placa} excluído com sucesso!")
    else:
        print(f"Veículo com placa {placa} não encontrado.")

def status_veiculo(placa, novo_status):
    linhas = ler_arquivo("veiculos.txt")
    for i in range(len(linhas)):
        dados = linhas[i].strip().split(";")
        if dados[0] == placa:
            dados[9] = novo_status
            linhas[i] = ";".join(dados) + "\n"
    with open("dados/veiculos.txt", "w") as arquivo:
        arquivo.writelines(linhas)
        