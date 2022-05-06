from PySimpleGUI import PySimpleGUI as g
from AddGrade import AddGrade as a


class Manage:
    def ShowManageWindow(self, Grades):
        g.theme('Default')

        show_Data = [
            [g.Text("Selecione uma grade para editar", key='-DATA-', enable_events=True)],
            [g.Combo(list(Grades.keys()), size=(25, 0), default_value="Selecione aqui", readonly=True), g.Button("Adicionar Grade", key="-ADD-", size=(20, 2))]
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
                a.ShowAddGradeWindow(0, Grades)
