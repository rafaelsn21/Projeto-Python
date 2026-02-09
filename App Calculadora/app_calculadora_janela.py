import tkinter as tk
from tkinter import messagebox
from app_calculadora_logica import soma, multiplicacao, divisao 

# Funções
def executar_soma():
    try:
        a = float(n1.get())
        b = float(n2.get())
        label_resultado.config(text=f"Resultado: {soma(a, b)}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números.")

def executar_multiplicacao():
    try:
        a = float(n1.get())
        b = float(n2.get())
        label_resultado.config(text=f"Resultado: {multiplicacao(a, b)}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números.")

def executar_divisao():
    try:
        a = float(n1.get())
        b = float(n2.get())
        label_resultado.config(text=f"Resultado: {divisao(a, b)}")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não é permi tida.")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números.")

# Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x400")
janela.configure(bg="#0088ff")
janela.resizable(False, False)

# Configuração do grid (centraliza tudo)
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)

# Labels
tk.Label(
    janela,
    text="Digite um número:",
    font=("Garamond", 12, "bold"),
    bg="#0088ff",
    fg="white"
).grid(row=0, column=0, columnspan=2, pady=(40, 5))

tk.Label(
    janela,
    text="Digite outro número:",
    font=("Garamond", 12, "bold"),
    bg="#0088ff",
    fg="white"
).grid(row=2, column=0, columnspan=2, pady=(20, 5))

# Entradas
n1 = tk.Entry(janela)
n1.grid(row=1, column=0, columnspan=2)

n2 = tk.Entry(janela)
n2.grid(row=3, column=0, columnspan=2)

# Botões
tk.Button(
    janela, text="+", font=("Garamond", 12, "bold"),
    command=executar_soma, width=3,
    bg="#783415", fg="#f0f0f0"
).grid(row=4, column=0, pady=20)

tk.Button(
    janela, text="x", font=("Garamond", 12, "bold"),
    command=executar_multiplicacao, width=3,
    bg="#783415", fg="#f0f0f0"
).grid(row=4, column=1, pady=20)

tk.Button(
    janela, text="÷", font=("Garamond", 12, "bold"),
    command=executar_divisao, width=3,
    bg="#783415", fg="#f0f0f0"
).grid(row=4, column=0, columnspan=2)

# Resultado
label_resultado = tk.Label(
    janela,
    text="Resultado:",
    font=("Garamond", 12, "bold"),
    bg="#0088ff",
    fg="white"
)
label_resultado.grid(row=6, column=0, columnspan=2, pady=30)

janela.mainloop()
