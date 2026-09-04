from pathlib import Path


path_bd=Path("sincro_escala/BD") / "escala_bd.txt"
escalas=[]

def cadastrar_escala():
    escala=input("digite o nome da escala: ")
    with open(path_bd, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{escala}\n")
    escalas.append(escala)
    print(f"o nome cadastrado foi: {escala} ")
    print("=========================================")
    print("Você gostaria de adiocionar uma nova Escala?")
    print("1. sim✅ ")
    print("2. não❌")
    seguir_cadastro=input("Escolha uma opção: ")
    print("=========================================")
    if seguir_cadastro=="1":
        cadastrar_escala()
    if seguir_cadastro=="2":
        print("cadastro concluido")
