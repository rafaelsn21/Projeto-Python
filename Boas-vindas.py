import tkinter as tk
import random

#Criação da Janela
root = tk.Tk()
root.title("Boas-vindas")
root.geometry("600x400")
root.resizable(False, False)

#Função do botão
def mensagem():
    nome = usuario.get()
    tel = telefone.get()
    e_mail = email.get()

    if nome.strip() and tel.strip() and e_mail.strip():
        mensagem_label.config(text = f"Olá, {nome}! Seja bem-vindo(a)!", fg = "#7CFC98")
    
    elif not nome and not tel and not e_mail:
        mensagem_label.config(text = f"Insira um nome, telefone e e-mail válidos.", fg = "#ff6b6b")
    
    elif not tel and not e_mail:
         mensagem_label.config(text = f"Insira um telefone e e-mail válidos.", fg = "#ff6b6b")
    
    elif not e_mail:
         mensagem_label.config(text = f"Insira um e-mail válido.", fg = "#ff6b6b")

    else:
        mensagem_label.config(text = "Insira um nome", fg = "#ff6b6b")

#Função do campo "Usuário"
def on_enter(e):
    e.widget["background"] = "lightblue"
    e.widget["cursor"] = "hand2"
    e.widget["foreground"] = "black"

def on_leave(e):
    e.widget["background"] = "#0077ff"
    e.widget["cursor"] = ""

#Função para o background
def animar_estrelas():
    for estrela in estrelas:
        canvas.move(estrela, 0, 1)
        x1, y1, x2, y2 = canvas.coords(estrela)
        if y1 > 400:
            novo_x = random.randint(0, 600)
            canvas.coords(
                estrela,
                novo_x, 0,
                novo_x + TAMANHO_PIXEL, TAMANHO_PIXEL
            )
    root.after(50, animar_estrelas)

#Criação do background
canvas = tk.Canvas(root, width=600, height=400, bg="#000121", highlightthickness=0)
canvas.place(x=0, y=0)

NUM_ESTRELAS = 100
TAMANHO_PIXEL = 3
estrelas = []

for _ in range(NUM_ESTRELAS):
    x = random.randint(0, 600)
    y = random.randint(0, 400)
    estrela = canvas.create_rectangle(
        x, y,
        x + TAMANHO_PIXEL, y + TAMANHO_PIXEL,
        fill="white",
        outline=""
    )
    estrelas.append(estrela)

animar_estrelas()

#Criação do campo "Nome"
label = tk.Label(root, text="Nome:", font=("Times New Roman", 14, "bold"), bg="#000121", fg="#ffffff")
label.place(relx=0.5, y=110, anchor="center")

usuario = tk.Entry(root, width=20, font=("Times New Roman", 14), bg="#0077ff", fg = "#f0f0f0")
usuario.place(relx=0.5, y=140, anchor="center")

#Criação do campo "Telefone"
label = tk.Label(root, text = "Telefone:", font = ("Times New Roman", 14, "bold"), bg = "#000121", fg = "#ffffff")
label.place(relx=0.5, y=180, anchor="center")

telefone = tk.Entry(root, width=20, font=("Times New Roman", 14), bg="#0077ff", fg = "#f0f0f0")
telefone.place(relx=0.5, y=210, anchor="center")

#Criação do campo "E-mail"
label = tk.Label(root, text = "E-mail:", font = ("Times New Roman", 14, "bold"), bg = "#000121", fg = "#ffffff")
label.place(relx=0.5, y=250, anchor="center")

email = tk.Entry(root, width=20, font=("Times New Roman", 14), bg="#0077ff", fg = "#f0f0f0")
email.place(relx=0.5, y=280, anchor="center")

#Botão de boas-vindas
botao = tk.Button(root, text="Recado", font = ("times New Roman", 12, "bold"), command=mensagem, fg="#f0f0f0", bg="#895eff", cursor="hand2")
botao.place(relx=0.5, y=320, anchor="center")

mensagem_label = tk.Label(root, text = "", font = ("Times New Roman", 14), bg = "#000121",fg = "#ffffff")
mensagem_label.place(relx=0.5, y=380, anchor="center")

root.mainloop()