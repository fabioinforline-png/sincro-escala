from pathlib import Path

path_bd=Path("sincro_escala/BD") / "funcionario_bd.txt", "a"
funcionarios=[]
sair_do_sistema=False

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
    funcionario=input("digite o nome do funcionario: ")
    with open(path_bd, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{funcionario}\n")
    funcionarios.append(funcionario)
    print(f"o nome cadastrado foi: {funcionario} ")
    print("=========================================")
    print("Você gostaria de adiocionar um novo funcionario?")
    print("1. sim✅ ")
    print("2. não❌")
    seguir_cadastro=input("Escolha uma opção: ")
    print("=========================================")
    if seguir_cadastro=="1":
        cadastra_funcionario()
    if seguir_cadastro=="2":
        print("cadastro concluido")
           
def listar_funcinario():
    with open(path_bd, "r",encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())
        
def Sair():
    print("saindo do sistema de gestão de escala 👋")    
#=============================================================
while not sair_do_sistema:
    
    opçao_menu=apresenta_menu()

    match opçao_menu:
        case "1":
            cadastra_funcionario()
        case "2":
            listar_funcinario()
        case "0":
            Sair()
            break
        case _:
            # O '_' 
            print("Opção Inválida!")
        
            
