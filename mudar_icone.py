import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Função para selecionar a pasta
def selecionar_pasta():
    pasta = filedialog.askdirectory(initialdir=os.getcwd(), title="Selecione a pasta de aulas")
    return pasta

# Função para selecionar o ícone
def selecionar_icone():
    arquivo_ico = filedialog.askopenfilename(
        initialdir=os.path.join(os.getcwd(), "icons"),
        title="Selecione um ícone",
        filetypes=[("Icon files", "*.ico")]
    )
    return arquivo_ico

# Função para mudar o ícone da pasta
def mudar_icone(pasta, icone):
    desktop_ini = os.path.join(pasta, "desktop.ini")
    with open(desktop_ini, "w") as ini_file:
        ini_file.write("[.ShellClassInfo]\n")
        ini_file.write(f"IconResource={icone},0\n")

    # Definir atributos do arquivo desktop.ini e da pasta como Sistema e Oculto
    os.system(f'attrib +s +h "{desktop_ini}"')
    os.system(f'attrib +s "{pasta}"')

# Função para exibir mensagem de sucesso
def mostrar_sucesso():
    messagebox.showinfo("Sucesso", "Ícone da pasta alterado com sucesso!")

# Função para exibir mensagem de erro
def mostrar_erro(mensagem):
    messagebox.showerror("Erro", mensagem)

# Criar a pasta de ícones, se não existir
if not os.path.exists("icons"):
    os.makedirs("icons")

# Janela principal do tkinter
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

try:
    # Seleciona a pasta e o ícone
    pasta_selecionada = selecionar_pasta()
    icone_selecionado = selecionar_icone()

    # Verifica se ambos foram selecionados
    if pasta_selecionada and icone_selecionado:
        mudar_icone(pasta_selecionada, icone_selecionado)
        mostrar_sucesso()
    else:
        mostrar_erro("Nenhuma pasta ou ícone foi selecionado.")
except Exception as e:
    mostrar_erro(f"Ocorreu um erro: {e}")

root.destroy()  # Fecha a janela principal
