from datetime import datetime

#obtem linhas sem o item que foi excluido para atualizar o arquivo sem ele
def obter_linhas(linhas_do_arquivo, termo):
    novas_linhas = []
    for linha in linhas_do_arquivo:
        dados = linha.strip().split(";")
        if dados[0] != termo:
            novas_linhas.append(linha)
    return novas_linhas

#para obter linhas de qualquer arquivo e fazer checagem
def ler_arquivo(nome_arquivo):
    linhas = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        pass
    return linhas

#Escreve a lista de linhas atualizada de volta no arquivo, geralmente usada após a obter linhas/em exclusões
def salvar_arquivo(nome_arquivo, linhas):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.writelines(linhas)

#Para edições, troca a linha antiga pela atualizada
def atualizar_linha(arquivo, termo, novos_dados):
    for i in range(len(arquivo)):
        dados = arquivo[i].strip().split(";")
        if dados[0] == termo:
            arquivo[i] = ";".join(novos_dados) + "\n"
            break
    return arquivo

#Usada para buscar qualquer objeto
def buscar_objeto(arquivo, termo):
    linhas = ler_arquivo(arquivo)
    for linha in linhas:
        dados = linha.strip().split(";")
        if dados[0] == termo:
            return dados    
    return None

#Adiciona uma nova linha no final do arquivo
def adicionar_linha(nome_arquivo, nova_linha):
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(nova_linha)


def processar_data(data_bruta):
    data_limpa = data_bruta.strip()
    try:
        data_objeto = datetime.strptime(data_limpa, "%d/%m/%Y")
        ano_atual = datetime.now().year
        if data_objeto.year < 1900 or data_objeto.year > ano_atual:
            return None
        return data_limpa
    except ValueError:
        return None


def processar_ano(ano_bruto):
    ano_limpo = ano_bruto.strip()
    if not ano_limpo.isdigit() or len(ano_limpo) != 4:
        return None   
    ano_int = int(ano_limpo)
    ano_atual = datetime.now().year
    if ano_int < 1886 or ano_int > ano_atual + 1:
        return None
    return ano_limpo