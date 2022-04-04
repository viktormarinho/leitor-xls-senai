import pandas as pd
import tkinter as tk
from tkinter import filedialog
import datetime
import json

WEEK_DAYS = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "\033[31mSábado", "\033[31mDomingo")
MAT_1DS = ("HARE", "SOP", "FPOO", "FPOO", "LIMA", "\033[31mERRO!!!", "\033[31mERRO!!!")


array_escolhido = MAT_1DS
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


leitor = pd.read_excel(file_path)
leitor.to_csv(r'output.csv', index=None, header=True)

csv = pd.read_csv(r'output.csv')

dados = {
    'nome': [],
    'faltas': [],
    'falta_por_aula': [],
}

row = 0
faltas_aluno = []
datas = []
first = True
nome_aluno = ''
total_faltas = 0
alunos = -1

while True:
    try:
        linha = csv.loc[row]
        nome_atual = linha.NomeAluno
        if first:
            nome_aluno = nome_atual
            dados['nome'].append(nome_aluno)
            alunos += 1
            aulas_dict = {}
            for i in range(5):
                aulas_dict[array_escolhido[i]] = 0
            dados['falta_por_aula'].append(aulas_dict.copy())
            aulas_dict.clear()

            first = False
        if nome_atual == nome_aluno:
            faltas_aluno.append(linha.NumeroFaltas)
            datastring = linha.DataAula
            datastring = datastring.replace('/', '')
            dia = int(datastring[0:2])
            mes = int(datastring[2:4])
            ano = int(datastring[4:])
            dataobj = datetime.date(ano, mes, dia)
            diasemana = dataobj.weekday()
            diasemanastr = array_escolhido[diasemana]

            dados['falta_por_aula'][alunos][diasemanastr] += linha.NumeroFaltas
        else:
            dados['faltas'].append(sum(faltas_aluno))
            datas.clear()
            faltas_aluno.clear()
            total_faltas = 0
            nome_aluno = nome_atual
            dados['nome'].append(nome_aluno)
            alunos += 1
            aulas_dict = {}
            for i in range(5):
                aulas_dict[array_escolhido[i]] = 0
            dados['falta_por_aula'].append(aulas_dict.copy())
            aulas_dict.clear()
            faltas_aluno.append(linha.NumeroFaltas)
            datastring = linha.DataAula
            datastring = datastring.replace('/', '')
            dia = int(datastring[0:2])
            mes = int(datastring[2:4])
            ano = int(datastring[4:])
            dataobj = datetime.date(ano, mes, dia)
            diasemana = dataobj.weekday()
            diasemanastr = array_escolhido[diasemana]

            dados['falta_por_aula'][alunos][diasemanastr] += linha.NumeroFaltas

        row += 1
    except KeyError:
        dados['faltas'].append(sum(faltas_aluno))

        break

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
tabela = pd.DataFrame(dados)


#tabela = pd.DataFrame.from_dict(dados, orient='index')
#tabela = tabela.transpose()

print(tabela)
