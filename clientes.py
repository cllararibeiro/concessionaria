from geral import *

def buscar_cliente(cpf):
    return buscar_objeto("clientes.txt",cpf)

def exibir_cliente(cliente):
    if cliente:
        print(f"""
        🪪 CPF: {cliente[0]}
        👤 Nome: {cliente[1]}
        📞 Telefone: {cliente[2]}
        📧 Email: {cliente[3]}
        📍 Cidade: {cliente[4]}
        📅 Data de Nascimento: {cliente[5]}
        """)
    else:
        print(f"❌ Cliente não encontrado.")

def processar_cpf(cpf_bruto):
    cpf = cpf_bruto.replace(".", "").replace("-", "").strip()
    if len(cpf) != 11 or not cpf.isdigit():
        return None 
    cpf_formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
    return cpf_formatado

def cadastrar_cliente():
    print("=== Cadastro de Cliente ===")
    cpf = input("Informe o CPF (apenas números): ")
    cpf_formatado = processar_cpf(cpf)
    
    if not cpf_formatado:
        print("❌ Erro: CPF inválido! Deve conter exatamente 11 números.")
        return
    cpf_existe = buscar_cliente(cpf_formatado)
    if cpf_existe:
        print(f"❌ Cliente com CPF {cpf_formatado} já existe no sistema. Cadastro cancelado.")
        return
    
    nome = input("Informe o nome: ")
    telefone = input("Informe o telefone: ")
    email = input("Informe o email: ")
    cidade = input("Informe a cidade: ")
    datanasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
    datanasc_valida = processar_data(datanasc)
    if not datanasc_valida:
        print("❌ Erro: Data de nascimento inválida! Digite no formato correto (ex: 25/12/1995).")
        return
    
    
    print("✨ Cliente cadastrado com Sucesso! ✨")
    cliente = buscar_objeto("clientes.txt", cpf_formatado)
    exibir_cliente(cliente)

def menu_edicaoc(cliente, cpf_original):
    edit = -1
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
            novo_cpf_formatado = processar_cpf(novo_cpf)
            if not novo_cpf_formatado:
                print("❌ Erro: CPF inválido! Deve conter exatamente 11 números.")
            elif novo_cpf_formatado == "cpf": 
                print("Nome inválido! 'cpf' é uma palavra reservada do sistema.")
            elif novo_cpf_formatado == cpf_original:
                cliente[0] = novo_cpf_formatado
            else:
                if buscar_cliente(novo_cpf_formatado):
                    print("❌ Já existe um cliente com esse CPF!")
                else:
                    cliente[0] = novo_cpf_formatado
        elif edit == 3:
            cliente[2] = input("altere o telefone: ")
        elif edit == 4:
            cliente[3] = input("altere o email: ")
        elif edit == 5:
            cliente[4] = input("altere a cidade: ")
        elif edit == 6:
            datanasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
            datanasc_valida = processar_data(datanasc)
            if not datanasc_valida:
                print("❌ Erro: Data de nascimento inválida! Digite no formato correto (ex: 25/12/1995).")
                continue
            cliente[5] = datanasc_valida

def editar_cliente(cpf):
    cpf_formatado = processar_cpf(cpf)

    if not cpf_formatado:
        print("❌ Erro: CPF digitado para busca é inválido.")
        return
    cliente = buscar_cliente(cpf_formatado)
    if cliente:
        exibir_cliente(cliente)
        cpf_original = cpf_formatado
        menu_edicaoc(cliente, cpf_original)
        linhas = ler_arquivo("clientes.txt")
        linhas_atualizadas = atualizar_linha(linhas, cpf_formatado, cliente)
        salvar_arquivo("clientes.txt", linhas_atualizadas)
        print("✅ Cliente atualizado com sucesso!")
    else:
        print(f"❌ Cliente com CPF: {cpf_formatado} não encontrado")
    cliente = buscar_cliente(cpf)

def excluir_cliente(cpf):
    if buscar_cliente(cpf):
        linhas_atuais = ler_arquivo("clientes.txt")
        novas_linhas = obter_linhas(linhas_atuais,cpf)
        salvar_arquivo("clientes.txt",novas_linhas)
        print(f"Cliente com CPF {cpf} excluído com sucesso!")
    else:
        print(f"Cliente com CPF {cpf}  não encontrado.")