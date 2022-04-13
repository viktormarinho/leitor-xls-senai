from PySimpleGUI import PySimpleGUI as g
from excelShowData.ShowData import ShowData as s
import json
class ChooseFile:

    def chooseFileWindow(self):
        dict_json = self.gradesList()

        g.theme('Default')

        choose_File = [
            [g.FileBrowse("Procurar Arquivo", target="-FILE-", size=(25, 2))],
            [g.Text("NOME DO ARQUIVO", key="-FILE-", text_color="#595959")],
            [g.Combo(dict_json, size=(25,0), default_value="Escolha a Grade", readonly=True)],
            [g.Button("Gerenciar Grade", key="-MANAGE-", size=(8,2)), g.Button("Confirmar", key="-CONFIRM-", size=(8,2))]
        ]

        # Panel para o menu de gerenciamento das grades. Deve ser oculto e so aparecer quando chamado
        # manageGrade = []

        layout = [
            [g.Frame("Escolha o arquivo Excel", layout=choose_File, key="-CONTAINER-", size=(300, 200), element_justification="c")]
        ]

        window = g.Window("Escolha", layout=layout, size=(500,500), element_justification="c", finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break

            elif event == "-CONFIRM-":
                s.showDataWindow(0)


    # Retornar as chaves do JSON para uma lista, indo para as opcoes do select
    def gradesList(self):
        with open('../grades.json', 'r') as read_json:
            dict_json = json.load(read_json)

        keys_list = []
        for k,v in dict_json.items():
            keys_list.append(k)

        return keys_list

if __name__ == '__main__':
    c = ChooseFile()
    c.chooseFileWindow()