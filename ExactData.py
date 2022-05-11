from PySimpleGUI import PySimpleGUI as g
import pandas as pd

class ExactData:
    def exactDataWindow(self, ALUNO_INFO: pd.DataFrame):
        g.theme('Reddit')

        ALUNO_INFO: dict = ALUNO_INFO.to_dict()
        show_Data = []
        layout = [
            [g.Frame('Dados do Aluno', layout=show_Data, key='-CONTAINER-', size=(400,250))]
        ]

        window = g.Window('Mostragem dos Dados de um Aluno', layout=layout, size=(450,300), element_justification='c', finalize=True)

        for k, v in ALUNO_INFO.items():
            window.extend_layout(window['-CONTAINER-'],
                                [[g.Text(k, key='-DATA-', justification='l'), g.Text(v, justification='r')]])

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break