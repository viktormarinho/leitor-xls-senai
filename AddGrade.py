import json

from PySimpleGUI import PySimpleGUI as g


class AddGrade:
    def ShowAddGradeWindow(self, Grades):
        g.theme('Default')

        show_Data = [
            [g.Text("Preencha os campos para adicionar uma grade", key='-DATA-', enable_events=True)],
            [g.Text("Nome da Grade"), g.InputText(key='-NOME-')],
            [g.Text("Aula Segunda"), g.InputText(key='-SEG-')],
            [g.Text("Aula Terça"), g.InputText(key='-TER-')],
            [g.Text("Aula Quarta"), g.InputText(key='-QUA-')],
            [g.Text("Aula Quinta"), g.InputText(key='-QUI-')],
            [g.Text("Aula Sexta"), g.InputText(key='-SEX-')],
            [g.Button("Adicionar", key="-ADD-", size=(20, 2))]
        ]

        layout = [
            [g.Frame("Edição de Grades", layout=show_Data, key='-CONTAINER-', size=(450, 450))]
        ]

        window = g.Window('Mostragem dos Dados', layout=layout, size=(500, 500), element_justification='c',
                          finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break

            elif event == '-ADD-':
                aulas_dia = [
                    value['-SEG-'],
                    value['-TER-'],
                    value['-QUA-'],
                    value['-QUI-'],
                    value['-SEX-'],
                ]
                Grades[value['-NOME-']] = aulas_dia
                with open('grades.json', 'w', encoding="utf-8") as f:
                    json.dump(Grades, f)

                window.close()