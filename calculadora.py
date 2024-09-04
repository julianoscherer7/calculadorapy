import tkinter as tk

class Display:
    def __init__(self, parent):
        self.display_var = tk.StringVar()
        self.display = tk.Entry(parent, textvariable=self.display_var, font=("Arial", 18), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

    def atualizar(self, texto):
        self.display_var.set(texto)

    def obter(self):
        return self.display_var.get()

    def limpar(self):
        self.display_var.set("")

class Botao:
    def __init__(self, parent, texto, linha, coluna, comando=None):
        self.botao = tk.Button(parent, text=texto, padx=20, pady=20, font=("Arial", 18), command=comando)
        self.botao.grid(row=linha, column=coluna)

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.display = Display(root)
        self.historico = ""

        self.criar_botoes()

    def criar_botoes(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (texto, linha, coluna) in botoes:
            comando = lambda t=texto: self.botao_click(t)
            Botao(self.root, texto, linha, coluna, comando)

    def botao_click(self, texto):
        if texto == "C":
            self.display.limpar()
            self.historico = ""
        elif texto == "=":
            try:
                resultado = str(eval(self.historico))
                self.display.atualizar(resultado)
                self.historico = resultado
            except Exception as e:
                self.display.atualizar("Erro")
                self.historico = ""
        else:
            self.historico += texto
            self.display.atualizar(self.historico)

    def rodar(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    calculadora.rodar()

