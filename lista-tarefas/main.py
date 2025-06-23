import FreeSimpleGUI as sg

# Popup de boas vindas
sg.popup('Bem-vindo(a)')

# Criando Layout
def criar_janela_inicial():
    sg.theme('DarkBlue14')

    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]

    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Lista de Tarefas',layout=layout, finalize=True)

# Criar a Janela
janela = criar_janela_inicial()

# Criar as regras da janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()