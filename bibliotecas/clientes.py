from bibliotecas.geral import *
import re
from bibliotecas.procedimentos import *

def modulo_clientes():
    os.system("clear")
    menu_clientes()
    while True:
        try:
            resp = int(input("Digite a opção desejada do Módulo Clientes: "))
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números!")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_clientes()
            continue 
        if resp == 0:
            return #volta pro menu principal
        
        elif resp == 1:
            os.system("clear")
            print("=== Essa opção é responsável por cadastrar um cliente no sistema ===")
            cadastrar_cliente()
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_clientes()

        elif resp == 2:
            os.system("clear")
            print("=== Essa opção é responsável por buscar um cliente no sistema. ===")
            cpf = input("Informe o CPF do cliente: ")
            cpf_formatado = processar_cpf(cpf)
            cliente = buscar_cliente(cpf_formatado)
            print(f"Buscando cliente com CPF {cpf}...")
            exibir_cliente(cliente)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_clientes()

        elif resp == 3:
            os.system("clear")
            print("=== Essa opção é responsável por editar as informações de um cliente no sistema. ===")
            cpf = input("Informe o CPF do cliente que deseja editar: ")
            editar_cliente(cpf)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_clientes()

        elif resp == 4:
            os.system("clear")
            print("=== Essa opção é responsável por excluir um cliente do sistema. ===")
            cpf = input("Informe o CPF do cliente que deseja excluir: ")
            excluir_cliente(cpf)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_clientes()

        elif resp == 5:
            os.system("clear")
            print("=== Essa opção é responsável por desativar um cliente do sistema. ===")
            cpf = input("Informe o CPF do cliente que deseja desativar: ")
            desativar_cliente(cpf)
            input("Pressione ENTER para continuar...")
            os.system("clear")
            menu_clientes()

        else:
            print("⚠️ Opção inválida! Escolha um número que esteja no menu.")
            input("Pressione ENTER para tentar novamente...")
            os.system("clear")
            menu_clientes()
            
def buscar_cliente(cpf):
    return buscar_objeto("clientes.txt",cpf)

def exibir_cliente(cliente):
    if cliente:
        status_emoji = "✅" if cliente[6] == "Ativo" else "🚨"
        print(f"""
        🪪 CPF: {cliente[0]}
        👤 Nome: {cliente[1]}
        📞 Telefone: {cliente[2]}
        📧 Email: {cliente[3]}
        📍 Cidade: {cliente[4]}
        📅 Data de Nascimento: {cliente[5]}
        {status_emoji} Status do Cliente: {cliente[6]}

        """)
    else:
        print(f"❌ Cliente não encontrado.")

def validar_email(email):
    formato = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(formato, email))

def validar_tel(telefone):
    numeros = "".join(caractere for caractere in telefone if caractere.isdigit())
    if len(numeros) == 10 or len(numeros) == 11:
        return numeros  #telefone limpo, só com números
    return False  

def formatar_tel(telefone):
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    return telefone

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
    if not validar_tel(telefone):
        print("❌ Erro:Telefone inválido!")
        return
    tel_formatado = formatar_tel(telefone)
    email = input("Informe o email: ")
    if not validar_email(email):
        print("❌ Erro: Email inválido!")
        return
    cidade = input("Informe a cidade: ")
    datanasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
    datanasc_valida = processar_data(datanasc)
    if not datanasc_valida:
        print("❌ Erro: Data de nascimento inválida! Digite no formato correto (ex: 25/12/1995).")
        return
    
    linhas_clientes = ler_arquivo("clientes.txt")
    if len(linhas_clientes) == 0:
        adicionar_linha("clientes.txt", "cpf;nome;telefone;email;cidade;data_nascimento;status\n")
    
    nova_linha = f"{cpf_formatado};{nome};{tel_formatado};{email};{cidade};{datanasc_valida};Ativo\n"
    
    adicionar_linha("clientes.txt", nova_linha)
    
    print("✨ Cliente cadastrado com Sucesso! ✨")
    
    cliente_atual = [cpf_formatado, nome, tel_formatado, email, cidade, datanasc_valida, "Ativo"]
    exibir_cliente(cliente_atual)


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
            print("✅ nome atualizado com sucesso!")
        elif edit == 2:
            novo_cpf = input("altere o CPF: ")
            novo_cpf_formatado = processar_cpf(novo_cpf)
            if not novo_cpf_formatado:
                print("❌ Erro: CPF inválido! Deve conter exatamente 11 números.")
            elif novo_cpf_formatado == cpf_original:
                cliente[0] = novo_cpf_formatado
            else:
                if buscar_cliente(novo_cpf_formatado):
                    print("❌ Já existe um cliente com esse CPF!")
                else:
                    cliente[0] = novo_cpf_formatado
                    print("✅ CPF atualizado com sucesso!")
        elif edit == 3:
            novo_tel = input("altere o telefone: ")
            if not validar_tel(novo_tel):
                print("❌ Erro:Telefone inválido!")
            else:
                novo_tel_formatado = formatar_tel(novo_tel)
                cliente[2] = novo_tel_formatado
                print("✅ Telefone atualizado com sucesso!")
        elif edit == 4:
            novo_email = input("Informe o novo email: ")
            if not validar_email(novo_email):
                print("❌ Erro: Email inválido! O e-mail não foi alterado.")
            else:
                cliente[3] = novo_email
                print("✅ E-mail atualizado com sucesso!")
        elif edit == 5:
            cliente[4] = input("altere a cidade: ")
        elif edit == 6:
            datanasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
            datanasc_valida = processar_data(datanasc)
            if not datanasc_valida:
                print("❌ Erro: Data de nascimento inválida! Digite no formato correto (ex: 25/12/1995).")
            else:
                cliente[5] = datanasc_valida
                print("✅ Data atualizada com sucesso!")

def editar_cliente(cpf):
    cpf_formatado = processar_cpf(cpf)

    if not cpf_formatado:
        print("❌ Erro: CPF digitado para busca é inválido.")
        return
    cliente = buscar_cliente(cpf_formatado)
    if cliente:
        status_cliente = cliente[6].strip()
        if status_cliente == "Ativo":
            exibir_cliente(cliente)
            cpf_original = cpf_formatado
            menu_edicaoc(cliente, cpf_original)
            linhas = ler_arquivo("clientes.txt")
            linhas_atualizadas = atualizar_linha(linhas, cpf_formatado, cliente)
            salvar_arquivo("clientes.txt", linhas_atualizadas)
            print("✅ Cliente atualizado com sucesso!")
        elif status_cliente == "Desativado":
            print(f"""O cliente de CPF {cpf_formatado} está DESATIVADO do sistema.
                  Não é possível editar informações.""")
    else:
        print(f"❌ Cliente com CPF: {cpf_formatado} não encontrado")
    cliente = buscar_cliente(cpf)

def excluir_cliente(cpf):
    cpf_formatado = processar_cpf(cpf)
    cliente = buscar_cliente(cpf_formatado)
    if cliente:
        linhas_atuais = ler_arquivo("clientes.txt")
        novas_linhas = obter_linhas(linhas_atuais,cpf_formatado)
        salvar_arquivo("clientes.txt",novas_linhas)
        print(f"Cliente com CPF {cpf_formatado} excluído com sucesso!")
    else:
        print(f"Cliente com CPF {cpf_formatado}  não encontrado.")

def desativar_cliente(cpf):
    print("=== Desativar Cliente ===")
    cpf_formatado = processar_cpf(cpf)
    cliente = buscar_cliente(cpf_formatado)
    if not cliente:
        print(f"❌ Cliente com CPF {cpf_formatado} não encontrado.")
        return

    if cliente[6] == "Desativado":
        print("⚠️ Este cliente já se encontra Desativado no sistema.")
        return

    confirmacao = input(f"Deseja realmente desativar o(a) cliente {cliente[1]}? (S/N): ").strip().upper()
    if confirmacao == "S":
        cliente[6] = "Desativado"
        linhas = ler_arquivo("clientes.txt")
        linhas_atualizadas = atualizar_linha(linhas, cpf_formatado, cliente)
        salvar_arquivo("clientes.txt", linhas_atualizadas)
        
        print(f"✅ Cliente {cliente[1]} excluído com sucesso (Status: Inativo)!")
    else:
        print("Operação de exclusão abortada.")