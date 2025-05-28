import tkinter as tk
from random import randint

class Jogo:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Adivinhe o Número")
        self.numero_secreto = randint(1, 100)
        self.tentativas = 0

        self.label = tk.Label(self.janela, text="Adivinhe o número entre 1 e 100")
        self.label.pack()

        self.entry = tk.Entry(self.janela)
        self.entry.pack()

        self.botao = tk.Button(self.janela, text="Chutar", command=self.verificar_chute)
        self.botao.pack()

        self.resultado = tk.Label(self.janela, text="")
        self.resultado.pack()

    def verificar_chute(self):
        try:
            chute = int(self.entry.get())
        except ValueError:
            self.resultado['text'] = "Por favor, digite um número!"
            return

        self.tentativas += 1

        if chute < self.numero_secreto:
            self.resultado['text'] = "Seu chute é muito baixo!"
        elif chute > self.numero_secreto:
            self.resultado['text'] = "Seu chute é muito alto!"
        else:
            self.resultado['text'] = f"Parabéns! Você acertou o número secreto em {self.tentativas} tentativas!"
            self.botao['state'] = 'disabled'

    def iniciar(self):
        self.janela.mainloop()

jogo = Jogo()
jogo.iniciar()

