import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


leitor = pd.read_excel(file_path)
leitor.to_csv(r'output.csv', index=None, header=True)

csv = pd.read_csv(r'output.csv')

dados = {
    'nome': [],
    'faltas': []
}

row = 0
faltas_aluno = []
first = True
nome_aluno = ''
total_faltas = 0

while True:
    try:
        linha = csv.loc[row]
        nome_atual = linha.NomeAluno
        if first:
            nome_aluno = nome_atual
            dados['nome'].append(nome_aluno)
            first = False
        if nome_atual == nome_aluno:
            faltas_aluno.append(linha.NumeroFaltas)
        else:
            dados['faltas'].append(sum(faltas_aluno))
            faltas_aluno.clear()
            total_faltas = 0
            first = True

        row += 1
    except KeyError:
        dados['faltas'].append(sum(faltas_aluno))
        break

tabela = pd.DataFrame(dados)
#tabela = pd.DataFrame.from_dict(dados, orient='index')
#tabela = tabela.transpose()

print(tabela)