from bibliotecas.veiculos import buscar_veiculo, status_veiculo
from bibliotecas.clientes import buscar_cliente, processar_cpf
from bibliotecas.geral import *
from bibliotecas.procedimentos import *

def modulo_vendas():
    os.system("clear")
    menu_vendas()
    while True:
        try:
            resp = int(input("Digite a opção desejada do Módulo Vendas: "))
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números!")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_vendas()
            continue 
        if resp == 0:
            return #volta pro menu principal
        if resp == 1:
            os.system("clear")
            cadastrar_venda()
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_vendas()

        elif resp == 2:
            os.system("clear")
            print("=== Essa opção é responsável por buscar uma venda no sistema. ===")
            id = input("Informe o ID da venda: ")
            venda = buscar_venda(id)
            print(f"Buscando venda com ID {id}...")
            exibir_venda(venda,"completa")
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_vendas()

        elif resp == 3:
            os.system("clear")
            editar_venda()
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_vendas()

        elif resp == 4:
            os.system("clear")
            print("=== Essa opção é responsável por cancelar uma venda do sistema. ===")
            id = input("Informe o ID da venda que deseja cancelar: ")
            cancelar_venda(id)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_vendas()
        
        elif resp == 5:
            os.system("clear")
            print("=== Essa opção é responsável por excluir uma venda do sistema. ===")
            id = input("Informe o ID da venda que deseja excluir: ")
            excluir_venda(id)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_vendas()

        else:
            print("⚠️ Opção inválida! Escolha um número que esteja no menu.")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_vendas()

def exibir_venda(venda,modulo=""):
    if venda is None:
        print("❌ Venda não encontrada.")
        return
    cliente = buscar_cliente(venda[2])
    veiculo = buscar_veiculo(venda[3])
    status_venda = venda[5]
    if status_venda == "Concluída":
        if modulo =="completa":
            print(f"""
                    === RECIBO ===
                    🪪 ID da Venda: {venda[0]}
                    🕒 Data: {venda[1]}
                    💰 Valor: R$ {float(veiculo[7]):.2f}
                    💳 Forma de Pagamento: {venda[4]}
                    ✅ Status da Venda: {status_venda}
                    === DADOS ===
                    👤 Cliente: {cliente[1]}
                    🚘 Veículo: {veiculo[1]} - {veiculo[2]} - {veiculo[3]}
            """)
        else:
            print(f"""
                    === RECIBO ===
                    🪪 ID da Venda: {venda[0]}
                    🕒 Data: {venda[1]}
                    👤 Cliente: {cliente[0]}
                    🚘 Veículo: {veiculo[0]} 
                    💰 Valor: R$ {float(veiculo[7]):.2f}
                    💳 Forma de Pagamento: {venda[4]}""")

def buscar_venda(id):
    return buscar_objeto("vendas.txt", id)

def menu_edicao_venda(venda, placa_original):
    if venda[5] == "Cancelada":
        print("❌ Não é possível editar uma venda que já foi CANCELADA.")
        return

    editven = -1
    while editven != 0:
        editven = int(input("""
        Qual informação deseja editar?
        [1] Data
        [2] CPF do cliente
        [3] Placa do veículo
        [4] Forma de pagamento
        
        [0] Finalizar edição
        > """))

        if editven == 1:
            data = processar_data(input("Informe a data da venda (DD/MM/AAAA): "))
            if not data:
                print("❌ Erro: Data inválida! Digite no formato correto (ex: 25/12/2025).")
                continue
            venda[1] = data
            print("Data alterada!")
        
        elif editven == 2:
            alt_cpf = input("Altere o CPF do cliente: ")
            alt_cpf_formatado = processar_cpf(alt_cpf)
            
            if not alt_cpf_formatado:
                print("❌ Erro: CPF inválido! Deve conter exatamente 11 números.")
            else:
                cliente_encontrado = buscar_cliente(alt_cpf_formatado)
                if cliente_encontrado: 
                    status_cliente = cliente_encontrado[6].strip()
                    if status_cliente == "Ativo":
                        venda[2] = alt_cpf_formatado
                        print("✅ CPF do cliente alterado na venda!")
                    else:
                        print("❌ Erro: Este cliente está DESATIVADO no sistema!")
                else:
                    print("❌ Erro: Cliente não encontrado no sistema!")
                
        elif editven == 3:
            alt_placa_pro = input("Altere a placa do veículo: ")
            veiculo = buscar_veiculo(alt_placa_pro)
            if not veiculo:
                print("❌ Erro: Veículo não encontrado no sistema!")
            elif alt_placa_pro == placa_original:
                venda[3] = alt_placa_pro
                print("A placa permanece a mesma.")
            elif veiculo[9].strip().lower() == "vendido":
                print("❌ Erro: Esse veículo já foi vendido!")
            else:
                status_veiculo(placa_original, "Disponível")
                status_veiculo(alt_placa_pro, "Vendido")
                
                venda[3] = alt_placa_pro
                print("Placa do veículo alterada na venda!")
                
        elif editven == 4:
            print("\nSelecione a nova forma de pagamento:")
            print("[1] Dinheiro\n[2] Pix\n[3] Cartão de Crédito\n[4] Financiamento")
            opc_pagto = input("> ")
            formas = {"1": "Dinheiro", "2": "Pix", "3": "Cartão de Crédito", "4": "Financiamento"}
            
            if opc_pagto in formas:
                venda[4] = formas[opc_pagto]
                print(f"✅ Forma de pagamento alterada para: {formas[opc_pagto]}!")
            else:
                print("❌ Opção inválida!")

def editar_venda():
    print("=== Essa opção é responsável por editar as informações de uma venda no sistema. ===")
    id = input("Informe o ID da venda que deseja editar: ")
    venda = buscar_venda(id)
    
    if venda:
        exibir_venda(venda)
        placa_original = venda[3]
        menu_edicao_venda(venda, placa_original)
        linhas = ler_arquivo("vendas.txt")
        linhas_atualizadas = atualizar_linha(linhas, id, venda)
        salvar_arquivo("vendas.txt", linhas_atualizadas)
        print("✅ Venda atualizada com sucesso!")
        exibir_venda(venda)
    else:
        print(f"❌ Venda com ID {id} não encontrada.")


def cadastrar_venda():
    print("=== Essa opção é responsável pelo cadastro de uma venda ===")
    cpf = input("Informe o CPF do cliente: ")
    cpf_formatado = processar_cpf(cpf)
    if not cpf_formatado:
        print("❌ Erro: CPF inválido! Deve conter exatamente 11 números.")
        return
    placa_pro = input("Informe a placa do veículo: ")
    data = processar_data(input("Informe a data da venda (DD/MM/AAAA): "))
    if not data:
        print("❌ Erro: Data da venda inválida! Use o formato DD/MM/AAAA.")
        return
    
    cliente = buscar_cliente(cpf_formatado)
    veiculo = buscar_veiculo(placa_pro)

    if not cliente:
        print(f"❌ Erro: O cliente com CPF {cpf_formatado} não está cadastrado no sistema!")
    elif not veiculo:
        print(f"❌ Erro: O veículo com placa {placa_pro} não está cadastrado no sistema!")
    elif veiculo[9].strip().lower() == "vendido":
        print(f"❌ Erro: O veículo com placa {placa_pro} já consta como VENDIDO no sistema!")
        
    else:
        print("\n=== FORMA DE PAGAMENTO ===")
        print("[1] Dinheiro\n[2] Pix\n[3] Cartão de Crédito\n[4] Financiamento")
        opc_pagto = input("Escolha a opção desejada: ")
        formas = {"1": "Dinheiro", "2": "Pix", "3": "Cartão", "4": "Financiamento"}
        
        forma_pagamento = formas.get(opc_pagto, "Outro")
        status_venda = "Concluída" 

        linhas_vendas = ler_arquivo("vendas.txt")
        if len(linhas_vendas) == 0:
            adicionar_linha("vendas.txt", "id;data;cliente;veiculo;forma_pagamento;status\n")
            venda_id = "1"
        else:
            venda_id = str(len(linhas_vendas))

        nova_linha = f"{venda_id};{data};{cpf_formatado};{placa_pro};{forma_pagamento};{status_venda}\n"
        adicionar_linha("vendas.txt", nova_linha)
        status_veiculo(placa_pro, "Vendido")

        venda_atual = [venda_id, data, cpf_formatado, placa_pro, forma_pagamento, status_venda]
        exibir_venda(venda_atual,"completa")

def cancelar_venda(id):
    print("=== Cancelamento de Venda ===")
    venda = buscar_venda(id)
    
    if not venda:
        print(f"❌ Venda com ID {id} não encontrada.")
        return

    if venda[5] == "Cancelada":
        print("⚠️ Esta venda já se encontra cancelada no sistema.")
        return

    confirmacao = input(f"Tem certeza que deseja CANCELAR a venda ID {id}? (S/N): ").strip().upper()
    if confirmacao == "S":
        placa_veiculo = venda[3]
        venda[5] = "Cancelada"
        linhas = ler_arquivo("vendas.txt")
        linhas_atualizadas = atualizar_linha(linhas, id, venda)
        salvar_arquivo("vendas.txt", linhas_atualizadas)
        
        status_veiculo(placa_veiculo, "Disponível")
        
        print(f"🚨 Venda com ID {id} CANCELADA com sucesso!")
        print(f"🚗 O veículo de placa {placa_veiculo} voltou a ficar Disponível para venda.")
    else:
        print("Operação de cancelamento abortada.")

def excluir_venda(id):
    venda = buscar_venda(id)
    
    if venda:
        placa_veiculo = venda[3]
        linhas_atuais = ler_arquivo("vendas.txt")
        novas_linhas = obter_linhas(linhas_atuais, id)
        salvar_arquivo("vendas.txt", novas_linhas)
        
        # Só libera o carro se a venda excluída não estivesse cancelada antes (evita redundância)
        if venda[5] != "Cancelada":
            status_veiculo(placa_veiculo, "Disponível")
        
        print(f"💥 Venda com ID {id} EXCLUÍDA FISICAMENTE do arquivo!")
        print(f"🚗 O veículo de placa {placa_veiculo} está Disponível.")
    else:
        print(f"Venda com ID {id} não encontrada.")