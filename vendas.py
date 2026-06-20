from veiculos import buscar_veiculo, status_veiculo
from clientes import buscar_cliente
from geral import *

def exibir_venda(venda):
    if venda is None:
        print("❌ Venda não encontrada.")
        return
    cliente = buscar_cliente(venda[2])
    veiculo = buscar_veiculo(venda[3])

    print(f"""
            === RECIBO ===
            🪪 ID da Venda: {venda[0]}
            🕒 Data: {venda[1]}

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

def buscar_venda(id):
    return buscar_objeto("vendas.txt", id)

def menu_edicao_venda(venda, placa_original):
    editven = -1
    while editven != 0:
        editven = int(input("""
        Qual informação deseja editar?
        [1] Data
        [2] CPF do cliente
        [3] Placa do veículo
        
        [0] Finalizar edição
        > """))

        if editven == 1:
            venda[1] = input("Altere a data (DD/MM/AAAA): ")
            print("Data alterada!")
            
        elif editven == 2:
            alt_cpf_cli = input("Altere o CPF do cliente: ")
            if buscar_cliente(alt_cpf_cli): 
                venda[2] = alt_cpf_cli
                print("CPF do cliente alterado na venda!")
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

def editar_venda():
    print("=== Essa opção é responsável por editar as informações de uma venda no sistema. ===")
    id = input("Informe o ID da venda que deseja editar: ")
    venda = buscar_venda(id)
    
    if venda:
        placa_original = venda[3]
        menu_edicao_venda(venda, placa_original)
        linhas = ler_arquivo("vendas.txt")
        linhas_atualizadas = atualizar_linha(linhas, id, venda, coluna_id=0)
        salvar_arquivo("vendas.txt",linhas_atualizadas)
        print("✅ Venda atualizada com sucesso!")
        exibir_venda(venda)
    else:
        print(f"❌ Venda com ID {id} não encontrada.")


def cadastrar_venda():
    print("=== Essa opção é responsável pelo cadastro de uma venda ===")
    cpf_cli = input("Informe o CPF do cliente: ")
    placa_pro = input("Informe a placa do veículo: ")
    data = input("Informe a data da venda (DD/MM/AAAA): ")
    cliente = buscar_cliente(cpf_cli)
    veiculo = buscar_veiculo(placa_pro)

    if not cliente:
        print(f"❌ Erro: O cliente com CPF {cpf_cli} não está cadastrado no sistema!")
    elif not veiculo:
        print(f"❌ Erro: O veículo com placa {placa_pro} não está cadastrado no sistema!")
    elif veiculo[9].strip().lower() == "vendido":
        print(f"❌ Erro: O veículo com placa {placa_pro} já consta como VENDIDO no sistema!")
        
    else:
        linhas_vendas = ler_arquivo("vendas.txt")
        precisa_cabecalho = (len(linhas_vendas) == 0)
        venda_id = "1" if precisa_cabecalho else str(len(linhas_vendas))

        with open("vendas.txt", "a") as arquivo:
            if precisa_cabecalho:
                arquivo.write("id;data;cliente;veiculo\n")
            arquivo.write(f"{venda_id};{data};{cpf_cli};{placa_pro}\n")

        status_veiculo(placa_pro, "Vendido")

        venda_atual = [venda_id, data, cpf_cli, placa_pro]
        exibir_venda(venda_atual)

def excluir_venda(id):
    venda = buscar_venda(id)
    
    if venda:
        placa_veiculo = venda[3]
        linhas_atuais = ler_arquivo("vendas.txt")
        novas_linhas = obter_linhas(linhas_atuais, id)
        salvar_arquivo("vendas.txt",novas_linhas)
        status_veiculo(placa_veiculo, "Disponível")
        
        print(f"Venda com ID {id} excluída com sucesso!")
        print(f"🚗 O veículo de placa {placa_veiculo} voltou a ficar Disponível.")
    else:
        print(f"Venda com ID {id} não encontrada.")
