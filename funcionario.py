from pathlib import Path

path_bd=Path("sincro_escala/BD") / "funcionario_bd.txt"
funcionarios=[]

def cadastra_funcionario():  
    funcionario=input("digite o nome do funcionario: ")
    with open(path_bd, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{funcionario}\n")
    funcionarios.append(funcionario)
    print(f"o nome cadastrado foi: {funcionario} ")
    print("=========================================")
    print("Você gostaria de adicionar um novo funcionario?")
    print("1. sim✅ ")
    print("2. não❌")
    seguir_cadastro=input("Escolha uma opção: ")
    print("=========================================")
    if seguir_cadastro=="1":
        cadastra_funcionario()
    if seguir_cadastro=="2":
        print("cadastro concluido")
        
def listar_funcionario():
    with open(path_bd, "r",encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())
                     
def excluir_funcionario():
    listar_funcionario()
    funcionario=input("Qual funcionário você deseja deletar: ")
    with open(path_bd, "r",encoding="utf-8") as arquivo:
        nomes=arquivo.readline()
    with open(path_bd, "w",encoding="utf-8") as arquivo:
        for linha in nomes:
            if linha.strip()==funcionario:
                linha=""
            arquivo.write(linha)