import os

def  boas_vindas():
    print("""
    =========================================================
                    BEM VINDO A SUCCESS CAR 💫🚘
    =========================================================""")
    print("""

        """)
    input("Pressione ENTER para continuar...")
    os.system("clear")

def aviso():
    print("""
    =========================================================
                        AVISO DO SISTEMA
    =========================================================

    Algumas funcionalidades  ainda não foram implementadas.
    O sistema está em fase de desenvolvimento, em breve 
    estará completo.

                🚀 Aguarde futuras atualizações!

    =========================================================
    """)

def menu():
    print("""
    ================================================
        🚗 SISTEMA DE GESTÃO - CONCESSIONÁRIA 🚗
    ================================================

    [1]  🚘 Módulo Veículos
    [2]  👥 Módulo Clientes
    [3]  💰 Módulo Vendas
    [4]  📊 Módulo Relatórios
    [5]  ℹ️ Informações do Sistema

    [0]  ❌ Sair

    ================================================
    """)

def menu_veiculos():
    print("""
    ================================================
                🚘 MÓDULO VEÍCULOS 🚘
    ================================================

    [1]  ➕ Cadastrar Veículo
    [2]  🔍 Buscar Veículo
    [3]  ✏️ Editar Veículo
    [4]  🗑️ Excluir Veículo

    [0]  ↩️ Voltar ao Menu Principal

    ================================================
    """)

def menu_clientes():
    print("""
    ================================================
                👥 MÓDULO CLIENTES 👥
    ================================================

    [1]  ➕ Cadastrar Cliente
    [2]  🔍 Buscar Cliente
    [3]  ✏️ Editar Cliente
    [4]  🗑️ Excluir Cliente
    [5]  🗑️ Desativar Cliente

    [0]  ↩️ Voltar ao Menu Principal

    ================================================
    """)

def menu_vendas():
    print("""
    ================================================
                💰 MÓDULO VENDAS 💰
    ================================================

    [1]  🛒 Cadastrar Venda
    [2]  🔍 Buscar Venda
    [3]  ✏️ Editar Venda
    [4]  ❌Cancelar venda
    [5]  🗑️ Excluir Venda

    [0]  ↩️ Voltar ao Menu Principal

    ================================================
    """
    )

def menu_relatorios():
    print("""
    ================================================
                📊 MÓDULO RELATÓRIOS 📊
    ================================================

    [1]  🚘 Relatório de Veículos
    [2]  👥 Relatório de Clientes
    [3]  💰 Relatório de Vendas

    [0]  ↩️ Voltar ao Menu Principal

    ================================================
    """)

def relatorios_clientes():
    print("""
    ================================================
            👥 MÓDULO RELATÓRIOS CLIENTES 👥
    ================================================

    [1]  📋 Listar todos os clientes
    [2]  🎂 Aniversariantes do mês
    [3]  🏙️ Listar clientes por cidade

    [0]  ↩️ Voltar ao Menu de Relatórios

    ================================================
    """)

def relatorios_veiculos():
    print("""
    ================================================
            🚘 MÓDULO RELATÓRIOS VEÍCULOS 🚘
    ================================================

    [1]  📋 Listar todos os veículos
    [2]  📅 Listar veículos por ano
    [3]  🎨 Listar veículos por cor
    [4]  🏷️ Listar veículos por marca
    [5]  🗂️ Listar veículos por categoria
    [6]  🚙 Listar veículos por tipo
    [7]  🚦 Listar veículos por status

    [0]  ↩️ Voltar ao Menu de Relatórios

    ================================================
    """)

def relatorios_vendas():
    print("""
    ================================================
            💰 MÓDULO RELATÓRIOS VENDAS 💰
    ================================================

    [1]  📋 Listar todas as vendas
    [2]  ⏳ Listar vendas por intervalo de tempo
    [3]  📈 Listar relatório geral anual
    [4]  📈 Listar vendas por forma de pagamento
   
    [0]  ↩️ Voltar ao Menu de Relatórios

    ================================================
    """)

def menu_info():
    print("""
    ==================================================
                    ℹ️ INFORMAÇÕES ℹ️
    ==================================================
                    🚗 Sucess Car 🚗
    Sistema de gestão para concessionárias de veículos

    👩‍💻 Equipe de desenvolvimento:
    • Maria Clara

    🐍 Linguagem:
    • Python

    📜 Licença Pública Geral GNU
    🌐 www.gnu.org/licenses/gpl.html

    © 2026 - Todos os direitos reservados

    [0] ↩️ Voltar ao Menu Principal

    ==================================================
    """)