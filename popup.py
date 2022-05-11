from PySimpleGUI import PySimpleGUI as g
import json

class Popup:
    def showPopup(self, grade_nome, Grades):
        g.theme("Reddit")

        show_Data = [
            [g.Text(f"Deseja mesmo deletar a grade {grade_nome}?", font=("Arial", 12, "bold"))],
            [g.Button("SIM", key="-YES-", size=(28, 2)), g.Button("NÃO", key="-NO-", size=(28, 2))]
        ]

        window = g.Window('Confirme', layout=show_Data, size=(500, 130), element_justification='c',
                          finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break

            elif event == "-NO-":
                window.close()

            elif event == '-YES-':
                for k, v in Grades.items():
                    if k == grade_nome:
                        del Grades[grade_nome]
                        break

                with open(r"grades.json", "w", encoding="utf-8") as f:
                    json.dump(Grades, f)

                window.close()
