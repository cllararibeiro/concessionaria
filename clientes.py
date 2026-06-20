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

def cadastrar_cliente():
    cpf = input("Informe o CPF: ")
    cpf_existe = buscar_cliente(cpf)
    if cpf_existe:
        print(f"Cliente com CPF {cpf} já existe no sistema. Cadastro cancelado.")
        return
    
    nome = input("Informe o nome: ")
    telefone = input("Informe o telefone: ")
    email = input("Informe o email: ")
    cidade = input("Informe a cidade: ")
    datanasc = input("Informe a data de nascimento (DD/MM/AAAA): ")

    linhas = ler_arquivo("clientes.txt")
    precisa_cabecalho = (len(linhas) == 0)

    with open("clientes.txt", "a") as arquivo:
            if precisa_cabecalho:
                arquivo.write("cpf;nome;telefone;email;cidade;datanasc\n")
            arquivo.write(
                f"{cpf};{nome};{telefone};"
                f"{email};{cidade};{datanasc}\n"
            )
    print("✨ Cliente cadastrado com Sucesso! ✨")
    cliente = buscar_cliente(cpf)
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
            if novo_cpf == "cpf":
                print("Nome inválido! 'cpf' é uma palavra reservada do sistema.")
            elif novo_cpf == cpf_original:
                cliente[0] = novo_cpf
            else:
                if buscar_cliente(novo_cpf):
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

def editar_cliente(cpf):
    cliente = buscar_cliente(cpf)
    if cliente:
        exibir_cliente(cliente)
        cpf_original = cpf
        menu_edicaoc(cliente, cpf_original)

        linhas = ler_arquivo("clientes.txt")
        linhas_atualizadas = atualizar_linha(linhas,cpf, cliente)
        salvar_arquivo("clientes.txt",linhas_atualizadas)
        print("Cliente atualizado com sucesso!")
    else:
        print(f"Cliente com CPF: {cpf} não encontrado")

def excluir_cliente(cpf):
    if buscar_cliente(cpf):
        linhas_atuais = ler_arquivo("clientes.txt")
        novas_linhas = obter_linhas(linhas_atuais,cpf)
        salvar_arquivo("clientes.txt",novas_linhas)
        print(f"Cliente com CPF {cpf} excluído com sucesso!")
    else:
        print(f"Cliente com CPF {cpf}  não encontrado.")