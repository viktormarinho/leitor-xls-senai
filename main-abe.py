import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

root = tk.Tk()
root.withdraw()

# Obtem o caminho do arquivo excel e lê os dados
file_path = filedialog.askopenfilename()
# file_path = "/home/abe/ws/leitor-xls-senai-old/abe/alunos.xls"
pd.read_excel(file_path).to_csv(r"output.csv", index=None, header=True)
csv = pd.read_csv(
    r"output.csv",
    encoding="UTF-8",
    usecols=["NomeAluno", "DataAula", "TotalAulas", "NumeroFaltas", "NumeroAtrasos"],
)
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
mat_des = ["HARE", "SOP", "FPOO", "FPOO2", "LIMA"]
# print(csv['NomeAluno'][0:50])

while True:
    o = int(input("Selecione a grade que você quer usar: "))
    if o == 1:
        selected = semana
        break
    else:
        selected = mat_des
        break

# Cria tabela (dataframe) com os dados requisitados
data_format = {
    "Nome": [],
    "Faltas": [],
    f"Faltas {selected[0]}": [],
    f"Faltas {selected[1]}": [],
    f"Faltas {selected[2]}": [],
    f"Faltas {selected[3]}": [],
    f"Faltas {selected[4]}": [],
}
df = pd.DataFrame(data_format)

# Obtem a lista de alunos na Tabela
alunos = list(csv.drop_duplicates(subset=["NomeAluno"])["NomeAluno"])

for aluno in alunos:
    # Obtem todos os registros do aluno
    linha_aluno = csv.loc[csv["NomeAluno"] == aluno]
    print(linha_aluno)
    arr = list()
    dia = {"faltas": 0, "aulas": 0}
    for i in range(5):
        arr.append(dia.copy())
    for (
        index,
        row,
    ) in linha_aluno.iterrows():
        # print(row['DataAula'])
        date_obj = datetime.strptime(row["DataAula"], "%d/%m/%Y")
        date_week = date_obj.weekday()
        arr[date_week]["faltas"] += int(row["NumeroFaltas"])
        arr[date_week]["aulas"] += int(row["TotalAulas"])
        # print(date_obj.weekday())
        # print(row['DataAula'], row['TotalAulas'], row['NumeroFaltas'])

    total_faltas_aluno = linha_aluno.sum(axis=0, skipna=True)["NumeroFaltas"]
    total_aulas_aluno = linha_aluno.sum(axis=0, skipna=True)["TotalAulas"]

    appenddata = {
        "Nome": aluno,
        "Faltas": total_faltas_aluno,
        f"Faltas {selected[0]}": arr[0]["faltas"],
        f"Faltas {selected[1]}": arr[1]["faltas"],
        f"Faltas {selected[2]}": arr[2]["faltas"],
        f"Faltas {selected[3]}": arr[3]["faltas"],
        f"Faltas {selected[4]}": arr[4]["faltas"],
    }
    df = df.append(appenddata, ignore_index=True)

print(df)
