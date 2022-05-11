import pandas as pd
from PySimpleGUI import PySimpleGUI as g
from ExactData import ExactData as e

ALUNOS = []


class ShowData:

    def showDataWindow(self, nome_arquivo, DATAFRAME: pd.DataFrame):
        g.theme('Default')

        show_Data = [
            [g.Text(f"Nome do aluno - Faltas Totais (Planilha {nome_arquivo})", key='-DATA-', enable_events=True, font=("Arial", 12, "bold"))]
        ]

        frame = [
            [g.Frame("Dados dos Alunos", layout=show_Data, key='-CONTAINER-', size=(450, 900))]
        ]

        layout = [
                [g.Column(frame, scrollable=True, vertical_scroll_only=True)]
        ]

        window = g.Window('Mostragem dos Dados', layout=layout, size=(500, 500), element_justification='c',
                          finalize=True)

        DATAFRAME.reset_index()
        for idx, row in DATAFRAME.iterrows():
            ALUNOS.append(row["Nome"])
            color = ""
            if row["Faltas"] > 50:
                color = "Red"
            elif row["Faltas"] > 25:
                color = "dark orange"
            elif row["Faltas"] > 0:
                color = "DarkGoldenRod3"
            else:
                color = "Green"
            window.extend_layout(window['-CONTAINER-'],
                                 [[g.Text(f'{row["Nome"]} - {row["Faltas"]}', text_color=color, key=str(row["Nome"]), enable_events=True)]])

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break

            elif event in ALUNOS:
                for idx, row in DATAFRAME.iterrows():
                    if event == row["Nome"]:
                        e.exactDataWindow(0, row)
