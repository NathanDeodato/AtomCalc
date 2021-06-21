# LIBS
import PySimpleGUI as sg
from time import sleep

# START
def AtomCalc():
    sg.theme("DarkTeal10")

    layout = [
        [sg.Text(" " * 16), sg.Text("-> ⚛ <-")],
        
        [sg.Text("-" * 50)],

        [sg.Text("1° Num" * 1), sg.Input(size=(19, 0), key="Num1", border_width=(4))],
        [sg.Text("2° Num" * 1), sg.Input(size=(19, 0), key="Num2", border_width=(4))],

        [sg.Text("-" * 50)],

        [sg.Button("1", size=(2, 0)), sg.Button("2", size=(2, 0)), sg.Button("3", size=(2, 0)), sg.Button("×", size=(2, 0))], 
        [sg.Button("4", size=(2, 0)), sg.Button("5", size=(2, 0)), sg.Button("6", size=(2, 0)), sg.Button("÷", size=(2, 0))], 
        [sg.Button("7", size=(2, 0)), sg.Button("8", size=(2, 0)), sg.Button("9", size=(2, 0)), sg.Button("+", size=(2, 0))], 
        [sg.Button("0", size=(2, 0)), sg.Button("⚛", size=(2, 0)), sg.Button("^", size=(2, 0)), sg.Button("-", size=(2, 0))],

        [sg.Output(size=(18, 4), font="Bodoni")],

        [sg.Text(" " * 16), sg.Text("(c) NT", border_width=(2))]
    ]
    return sg.Window("⚛ AtomCalc", layout=layout)


window = AtomCalc()

while True:
    event, values = window.Read()

    ## CLOSE WINDOW
    if event == sg.WIN_CLOSED:
        break

    #if event == "Go!":
    ## CALCS MOOD ONE
    n1 = int(values["Num1"])
    n2 = int(values["Num2"])

        # Calc mood one
    if n1 and n2 != "":

        if event == "+":
            cal = n1 + n2
            
            print("-" * 30)
            print((" "*10) + f"{n1} + {n2} = {cal}")
            print("-" * 30)
        
        elif event == "-":
            cal = n1 - n2
            
            print("-" * 30)
            print((" "*10) + f"{n1} - {n2} = {cal}")
            print("-" * 30)

        elif event == "×":
            cal = n1 * n2
            
            print("-" * 30)
            print((" "*10) + f"{n1} × {n2} = {cal}")
            print("-" * 30)

        elif event == "÷":
            cal = n1 / n2

            print("-" * 30)
            print((" "*10) + f"{n1} ÷ {n2} = {cal}")
            print("-" * 30)

        elif event == "^":
            cal = n1 ** n2

            print("-" * 30)
            print((" "*10) + f"{n1}^{n2} = {cal}")
            print("-" * 30)

    else:
        ## calc mod two
        n1 = str()
        n2 = str()

        ## counter nuns
        counter = 1

        ## operation
        operation = ""

        ## added nuns
        if event == "1":
            if counter == 1:
                n1 += "1"
            elif counter == 2:
                n2 += "1"            

        elif event == "2":
            if counter == 1:
                n1 += "2"
            elif counter == 2:
                n2 += "2"

        elif event == "3":
            if counter == 1:
                n1 += "3"
            elif counter == 2:
                n2 += "3"

        elif event == "4":
            if counter == 1:
                n1 += "4"
            elif counter == 2:
                n2 += "5"

        elif event == "5":
            if counter == 1:
                n1 += "5"
            elif counter == 2:
                n2 += "5"
                
        elif event == "6":
            if counter == 1:
                n1 += "6"
            elif counter == 2:
                n2 += "6"

        elif event == "7":
            if counter == 1:
                n1 += "7"
            elif counter == 2:
                n2 += "7"

        elif event == "8":
            if counter == 1:
                n1 += "8"
            elif counter == 2:
                n2 += "8"

        elif event == "9":
            if counter == 1:
                n1 += "9"
            elif counter == 2:
                n2 += "9"

        ## counter info one
        if event == "+":
            counter ++ 1
            operation = "+"
        elif event == "-":
            counter ++ 1
            operation = "-"
        elif event == "×":
            counter ++ 1
            operation = "×"
        elif event == "÷":
            counter ++ 1
            operation = "÷"
        elif event == "^":
            counter ++ 1
            operation = "^"
        
        ## counter info two
        if event == "⚛":
            n1 = int()
            n2 = int()
            if operation == "+":
                soma = n1 + n2
                print(f"{n1} + {n2} = {soma}")
            elif operation == "-":
                subt = n1 - n2
                print(f"{n1} - {n2} = {subt}")
            elif operation == "×":
                mult = n1 * n2
                print(f"{n1} × {n2} = {mult}")
            elif operation == "÷":
                divi = n1 / n2
                print(f"{n1} ÷ {n2} = {divi}")
            elif operation == "^":
                pote = n1 ** n2
                print(f"{n1} ^ {n2} = {pote}")

# Ainda preciso fazer os testes, mas está quase finalizado.

