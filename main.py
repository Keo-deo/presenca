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
            "consultar informações de um aluno",
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
        contador = 0
        for aluno in lista_informacoes:
            contador = contador+1
            print("\033[1m" + f"Aluno {contador}: " + "\033[0m")
            print(f"Nome: {aluno["nome"]}")
            print(f"Turma: {aluno["turma"]}")
            print(f"Curso: {aluno["curso"]}\n")

    elif escolha == "consultar informações de um aluno":
        nome = input("Digite o nome do aluno que voce quer achar: ")
        for aluno in lista_informacoes:
            if aluno["nome"] == nome:
                print("\033[1m" + f"aluno encontrado:" + "\033[0m")
                print(f"nome: {aluno}")

    elif escolha == "encerrar programa":
        break
    #elif escolha == "marcar presenca":

