
#obtem linhas sem o item que foi excluido para atualizar o arquivo sem ele
def obter_linhas(linhas_do_arquivo, termo):
    novas_linhas = []
    for linha in linhas_do_arquivo:
        dados = linha.strip().split(";")
        if dados[0] != termo:
            novas_linhas.append(linha)
    return novas_linhas

#para obter linhas de qualquer arquivo
def ler_arquivo(nome_arquivo):
    linhas = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        pass
    return linhas

#Escreve a lista de linhas atualizada de volta no arquivo
def salvar_arquivo(nome_arquivo, linhas):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.writelines(linhas)

#Para edições
def atualizar_linha(arquivo, termo, novos_dados):
    for i in range(len(arquivo)):
        dados = arquivo[i].strip().split(";")
        if dados[0] == termo:
            arquivo[i] = ";".join(novos_dados) + "\n"
            break
    return arquivo

#buscar qualquer coisa
def buscar_objeto(arquivo, termo):
    linhas = ler_arquivo(arquivo)
    for linha in linhas:
        dados = linha.strip().split(";")
        if dados[0] == termo:
            return dados    
    return None