from funcionario import cadastra_funcionario,listar_funcionario,excluir_funcionario
from escala import cadastrar_escala


sair_do_sistema=False

def apresenta_menu():
    print("=========================================")
    print("     SISTEMA DE GESTÃO DE ESCALAS")
    print("=========================================")
    print("")
    print("1. Cadastrar funcionário👤")
    print("2. Listar funcionário 👥")
    print("3. Excluir funcionário 🗑️")
    print("4. Cadastrar Escala 👥📅")
    print("0. Sair ❌")

    print("")
    opçao_menu=input("Escolha uma opção: ")
    return opçao_menu
        
def Sair():
    print("saindo do sistema de gestão de escala 👋")    
#=============================================================
while not sair_do_sistema:
    
    opçao_menu=apresenta_menu()

    match opçao_menu:
        case "1":
            cadastra_funcionario()
        case "2":
            listar_funcionario()
        case "3":
            excluir_funcionario()
        case "4":
            cadastrar_escala()
        case "0":
            Sair()
            break
        case _:
            # O '_' 
            print("Opção Inválida!")
        
            
