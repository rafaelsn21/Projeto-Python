import tkinter as tk
from tkinter import messagebox

#Criação da janela
root = tk.Tk()
root.title("Login")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg = "#0086ce")

#Rótulo "Usuário"
label = tk.Label(root, text = "Usuário:", font = ("Times New Roman", 12, "bold"), fg = "#f0f0f0", bg ="#0086ce")
label.place(relx=0.5, y=80, anchor="center")

#Campo "Usuário"
usuario = tk.Entry(root)
usuario.place(relx=0.5, y=100, anchor="center")

#Rótulo "Senha"
label = tk.Label(root, text = "Senha:", font = ("Times New Roman", 12, "bold"), fg = "#f0f0f0", bg ="#0086ce")
label.place(relx=0.5, y=130, anchor="center")

#Campo "Senha"
senha = tk.Entry(root)
senha.place(relx=0.5, y=150, anchor="center")

#Função para mensagem de login
def mensagem():
    nome = usuario.get()
    pswd = senha.get()

    if nome.strip() and pswd.strip():
        mensagem_label.configure(text = f"Olá, {nome}! Seja bem-vindo!", fg = "#17AE00AC") 
    
    else:
        mensagem_label.configure(text = f"Insira um nome ou senha válidos.", fg = "#f00000")

#Botão
botao = tk.Button(root, text = "Entrar", font = ("Times New Roman", 12, "bold"), cursor = "hand2", bg = "#ffe95a", fg = "#0086ce", width = "5", command=mensagem)
botao.place(relx=0.5, y=200, anchor="center")

#Campo para mensagem de login
mensagem_label = tk.Label(root, text = "", font = ("Times New Roman", 14), bg = "#0086ce")
mensagem_label.place(relx=0.5, y=240, anchor="center")


root.mainloop()
