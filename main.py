import pandas as pd
import tkinter as tk
from tkinter import filedialog
import datetime
import json

array_escolhido = []


def main():
    global array_escolhido
    dia = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

    print("***" * 15)
    escolhas = []
    with open('grades.json', 'r', encoding='utf-8') as f:
        grades_json = json.load(f)
        for grade in grades_json.keys():
            escolhas.append(grade)
    count = 0
    for gr_nome, gr_lista in grades_json.items():
        print(f'{count} - {gr_nome}: {gr_lista}')
        count += 1
    cod = int(input("codigo (-1 adiciona): "))
    if cod == -1:
        nome = input("Nome da grade: ")
        materias = [input(f"Materia do dia {dia[i]}:") for i in range(5)]
        materias.append("ERRO!!!")
        materias.append("ERRO!!!")
        grades_json[nome] = materias
        with open('grades.json', 'w', encoding='utf-8') as f:
            json.dump(grades_json, f)
        main()
    else:
        array_escolhido = grades_json[escolhas[cod]]
        start()


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
alunos = -1


def computar_linha(linha):
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


def novo_aluno(aluno_nome):
    global alunos
    dados['nome'].append(aluno_nome)
    alunos += 1
    aulas_dict = {}
    for j in range(5):
        aulas_dict[array_escolhido[j]] = 0
    dados['falta_por_aula'].append(aulas_dict.copy())
    aulas_dict.clear()


def start():
    global row, first, nome_aluno
    while True:
        try:
            linha = csv.loc[row]
            nome_atual = linha.NomeAluno
            if first:
                nome_aluno = nome_atual
                novo_aluno(nome_aluno)
                first = False
            if nome_atual == nome_aluno:

                computar_linha(linha)
            else:
                dados['faltas'].append(sum(faltas_aluno))
                datas.clear()
                faltas_aluno.clear()
                nome_aluno = nome_atual

                novo_aluno(nome_aluno)

                computar_linha(linha)

            row += 1
        except KeyError:
            # ACHO QUE TEM COISA ERRADA AQUI QSE CERTEZA, CONFERIR RACIOCINIO
            # Checar mexendo nas últimas linhas do csv para ver se ele computa as últimas faltas.
            dados['faltas'].append(sum(faltas_aluno))

            break

    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    tabela = pd.DataFrame(dados)


    #tabela = pd.DataFrame.from_dict(dados, orient='index')
    #tabela = tabela.transpose()

    print(tabela)


if __name__ == '__main__':
    main()
