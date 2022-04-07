from PySimpleGUI import PySimpleGUI as g
from excelShowData.ShowData import ShowData as s

class ChooseFile:

    def WindowChooseFile(self):
        values = [0, 1, 2, 3, 4, 5]
        g.theme('Default')

        choose_File = [
            [g.FileBrowse("Procurar Arquivo", target="-FILE-", size=(25, 2))],
            [g.Text("NOME DO ARQUIVO", key="-FILE-", text_color="#595959")],
            [g.Combo(values, size=(25,0), default_value="Escolha a Grade", readonly=True)],
            [g.Button("Gerenciar Grade", key="-MANAGE-", size=(8,2)), g.Button("Confirmar", key="-CONFIRM-", size=(8,2))]
        ]

        # Panel para o menu de gerenciamento das grades
        # manageGrade = [
        #
        # ]

        layout = [
            [g.Frame("Escolha o arquivo Excel", layout=choose_File, key="container", size=(300, 200), element_justification="c")]
        ]

        window = g.Window("Escolha", layout=layout, size=(500,500), element_justification="c", finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED or event == "OK":
                break

            elif event == "-CONFIRM-":
                s.showData(0)

if __name__ == '__main__':
    c = ChooseFile()
    c.WindowChooseFile()