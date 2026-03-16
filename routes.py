from main import app
from flask import render_template, request, redirect
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017")

db = cliente["presenca"]

colection = db["alunos"]

@app.route('/')
def home():
    return render_template("homepage.html")

def adicionar():
    if request.mothod == 'post':
        novo_aluno = {
            "nome": request.form.get("nome"),
            "telefone": request.form.get("telefone"),
            "turma": request.form.get("turma"),
            "faltas": 0
        }