import pandas as pd
from PySimpleGUI import PySimpleGUI as g
from ExactData import ExactData as e

ALUNOS = []
class ShowData:

    def showDataWindow(self, nome_arquivo, DATAFRAME: pd.DataFrame):
        g.theme('Default')

        show_Data = [
            [g.Text(nome_arquivo, key='-DATA-', enable_events=True)]
        ]

        layout = [
            [g.Frame("Dados dos Alunos", layout=show_Data, key='-CONTAINER-', size=(450, 450))]
        ]

        window = g.Window('Mostragem dos Dados',layout=layout, size=(500,500), element_justification='c', finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break

            elif event == '-DATA-':
                DATAFRAME.reset_index()
                for idx, row in DATAFRAME.iterrows():
                    ALUNOS.append(row["Nome"])
                    window.extend_layout(window['-CONTAINER-'], [[g.Text(row["Nome"], key=str(row["Nome"]), enable_events=True)]])

            elif event in ALUNOS:
                for idx, row in DATAFRAME.iterrows():
                    if event == row["Nome"]:
                        e.exactDataWindow(0, row)