import json

from PySimpleGUI import PySimpleGUI as g


class EditGradeWindow:
    def ShowEditGradeWindow(self, grade_selecionada, all_grades, grade_nome):
        g.theme('Reddit')

        show_Data = [
            [g.Text(f"Preencha os campos para substituir a grade {grade_nome}", key='-DATA-', enable_events=True)],
            [g.Text("Nome da Grade"), g.InputText(key='-NOME-', default_text=grade_nome)],
            [g.Text("Aula Segunda"), g.InputText(key='-SEG-', default_text=grade_selecionada[0])],
            [g.Text("Aula Terça"), g.InputText(key='-TER-', default_text=grade_selecionada[1])],
            [g.Text("Aula Quarta"), g.InputText(key='-QUA-', default_text=grade_selecionada[2])],
            [g.Text("Aula Quinta"), g.InputText(key='-QUI-', default_text=grade_selecionada[3])],
            [g.Text("Aula Sexta"), g.InputText(key='-SEX-', default_text=grade_selecionada[4])],
            [g.Button("Salvar Mudanças", key="-ADD-", size=(20, 2))]
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
                all_grades[value['-NOME-']] = aulas_dia
                with open('grades.json', 'w') as f:
                    json.dump(all_grades, f)

                window.close()