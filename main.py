
def apresenta_menu():
    print("=========================================")
    print("     SISTEMA DE GESTÃO DE ESCALAS")
    print("=========================================")
    print("")
    print("1. Cadastrar funcionário👤")
    print("2. Listar funcionário 👥")
    print("0. Sair ❌")
    print("")
    opçao_menu=input("Escolha uma opção: ")
    return opçao_menu

def cadastra_funcionario():
    funcionários=input("digite o nome do funcionário: ")
    print(f"o nome cadastrado foi: {funcionários} ")
    
def listar_funcinario():
    print("Listando funcionários") 

def Sair():
    print("saindo do sistema de gestão de escala 👋")    
#=============================================================
    
opçao_menu=apresenta_menu()

match opçao_menu:
    case "1":
        cadastra_funcionario()
    case "2":
        listar_funcinario()
    case "0":
        print("❌ Saindo do sistema...")
    case _:
        # O '_' 
        print("Opção Inválida!")