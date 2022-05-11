from PySimpleGUI import PySimpleGUI as g
from AddGrade import AddGrade as a
from EditGrade import EditGradeWindow as e
from popup import Popup as p


class Manage:
    def ShowManageWindow(self, Grades):
        g.theme('Reddit')

        show_Data = [
            [g.Text("Selecione uma grade para editar", key='-DATA-', enable_events=True)],
            [g.Combo(list(Grades.keys()), size=(25, 0), default_value="Selecione aqui", readonly=True), g.Button("Adicionar Grade", key="-ADD-", size=(20, 2))],
            [g.Button("Editar Grade", key="-EDIT-", size=(28, 2)), g.Button("Deletar Grade", key="-DEL-", size=(28, 2))]
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

            elif event == '-EDIT-':
                grade_selecionada = Grades[value[0]]
                grade_nome = ""
                for k, v in Grades.items():
                    if v == grade_selecionada:
                        grade_nome = k
                        break
                e.ShowEditGradeWindow(0, grade_selecionada, Grades, grade_nome)

            elif event == '-DEL-':
                grade_selecionada = Grades[value[0]]
                grade_nome = ""
                for k, v in Grades.items():
                    if v == grade_selecionada:
                        grade_nome = k
                        break
                p.showPopup(0, grade_nome, Grades)

            elif event == '-ADD-':
                a.ShowAddGradeWindow(0, Grades)
