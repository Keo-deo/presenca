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
            "consultar informacoes de um aluno",
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
        print(lista_informacoes)

    elif escolha == "encerrar programa":
        break
    #elif escolha == "marcar presenca":

