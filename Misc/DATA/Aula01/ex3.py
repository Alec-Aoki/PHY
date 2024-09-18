#NÃO TERMINADO

turmas = {
    "Turma A":[
        {"nome":"Aluno1", "idade":17, "ID":1},
        {"nome":"Aluno2", "idade":17, "ID":2},
        {"nome":"Aluno3", "idade":18, "ID": 3}
    ],
    "Turma B":[
        {"nome":"Aluno1", "idade":15, "ID":4},
        {"nome":"Aluno2", "idade":15, "ID":5},
        {"nome":"Aluno3", "idade":16, "ID": 6}
    ]
}

print(type(turmas))
print(type(turmas["Turma A"]))

novoAluno = {"nome":"Aluno4", "idade":17, "ID": 7}

turmas["Turma A"].append(novoAluno)

print(turmas)