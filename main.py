#from pymongo import MongoClient
import questionary

#cliente = MongoClient("mongodb://localhost:27017/")

#db = cliente["presensa"]

#colection = db["alunos"]


lista_informacoes = []

while True:
    escolha = questionary.select(
        "Opções:",
        choices=[
            "adicionar aluno",
            "marcar presenca",
            "exibir informações",
            "consultar as informacoes de um aluno",
            "atualizar as informacoes de um aluno",
            "deletar um aluno do cadastro",
            "encerrar programa"
        ]
    ).ask()

    if escolha == "adicionar aluno":
        nome = input("digite o nome do aluno: ")
        turma = input("digite a turma do aluno: ")
        curso = input("digite o curso do aluno: ")

        informacoes = {
            "nome"  : nome,
            "turma" : turma,
            "curso" : curso
            }

        lista_informacoes.append(informacoes)

    elif escolha == "exibir informações":
        num = 0
        for aluno in lista_informacoes:
            num = num+1
            print(f"\033[1mAluno {num}\033[0m")
            print(f"Nome: {aluno["nome"]}")
            print(f"Turma: {aluno["turma"]}")
            print(f"Curso: {aluno["curso"]}\n")

    elif escolha == "consultar as informacoes de um aluno":
        nome = input("digite o nome do aluno que deseja consultar: ")
        for aluno in lista_informacoes:
            if aluno["nome"] == nome:
                print(f"\nNome: {aluno["nome"]}")
                print(f"Turma: {aluno["turma"]}")
                print(f"Curso: {aluno["curso"]}\n")

    elif escolha == "atualizar as informacoes de um aluno":
        nome = input("Digite o nome do aluno que voce de seja atualizar: ")
        n_nome = input("Digite o novo nome do aluno: ")
        n_turma = input("Digite a nova turma do aluno: ")
        n_curso = input("Digite o novo curso do aluno: ")

        informacoes = {
            "nome"  : n_nome,
            "turma" : n_turma,
            "curso" : n_curso
            }
        lista_informacoes.append(informacoes)

        print("informacoes atualizadas!")

    elif escolha == "deletar um aluno do cadastro":
            nome = input("""Digite o nome do aluno que voce
deseja deletar do cadastro: """)
            for aluno in lista_informacoes:
               if aluno["nome"] == nome:
                    lista_informacoes.remove(aluno)
                    print(f"{nome} removido com sucesso!")

    elif escolha == "encerrar programa":
        break
    #elif escolha == "marcar presenca":

