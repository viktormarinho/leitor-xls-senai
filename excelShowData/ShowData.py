from PySimpleGUI import PySimpleGUI as g

class ShowData:

    def showData(self):
        g.theme('Default')

        show_Data = [
            [g.Text('CLICA', key='-DATA-', enable_events=True)],
            [g.Text('', key='new_txt')]
        ]

        layout = [
            [g.Frame("Dados dos Alunos", layout=show_Data, key='container', size=(450, 450))]
        ]

        window = g.Window('Mostragem dos Dados',layout=layout, size=(500,500), element_justification='c', finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break

            elif event == '-DATA-':
                print("salve")
                value['new_txt'].set_text('fuck')