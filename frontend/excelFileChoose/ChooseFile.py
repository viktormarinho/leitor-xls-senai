from PySimpleGUI import PySimpleGUI as g
from ShowData import ShowData as s
from Manage import Manage as m
import json
import mainabe

FILE_PATH: str = ""

class ChooseFile:

    def chooseFileWindow(self):
        global FILE_PATH
        dict_json, Grades = self.gradesList()

        g.theme('Reddit')
        choose_File = [
            [g.FileBrowse("Procurar Arquivo", target="-FILE-", size=(25, 2))],
            [g.Text("NOME DO ARQUIVO", key="-FILE-", text_color="#595959")],
            [g.Combo(dict_json, size=(25,0), default_value="Escolha a Grade", readonly=True), g.Button("🔄", key="-REFRESH-", size=(1,1))],
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
                FILE_PATH = value["Procurar Arquivo"]
                filename = FILE_PATH.split("/")[-1]
                SELECTEDGRADE = value[0]
                DATAFRAME = mainabe.main(FILE_PATH, SELECTEDGRADE)
                s.showDataWindow(0, filename, DATAFRAME)

            elif event == "-MANAGE-":
                m.ShowManageWindow(0, Grades)

            elif event == "-REFRESH-":
                dict_json, Grades = self.gradesList()
                window.close()
                self.chooseFileWindow()

    # Retornar as chaves do JSON para uma lista, indo para as opcoes do select
    def gradesList(self):
        with open('grades.json', 'r') as read_json:
            dict_json = json.load(read_json)

        keys_list = []
        for k, v in dict_json.items():
            keys_list.append(k)

        return keys_list, dict_json


def getFILEPATH():
    return FILE_PATH

if __name__ == '__main__':
    c = ChooseFile()
    c.chooseFileWindow()