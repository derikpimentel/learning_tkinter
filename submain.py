from tkinter import *

class Subapplication:
    def __init__(self, master=None):
        self.master = master

        # Criando um LabelFrame (Contêiner com texto)
        self.frame = LabelFrame(self.master, padx=10, pady=10)
        self.frame["text"] = "Opções de Configuração"
        self.frame["bg"] = "lightblue"
        self.frame["fg"] = "red"
        self.frame["font"] = ("Arial", 12, "bold")
        self.frame["labelanchor"] = "s" # Define a posição do título
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)
        """
        fill='both' e expand=True fazem com que o LabelFrame ocupe todo o espaço 
        disponível no contêiner pai
        """

        Label(self.frame, text="Opção 1").pack(anchor="w")
        # anchor='w' posiciona o conteúdo ao leste (à esquerda)
        Label(self.frame, text="Opção 2").pack(anchor="w")

        self.container = Frame(self.frame)
        self.container.pack(padx=50, pady=50)

        Label(self.container, text="Nome").grid(row=0, column=0, sticky="w")
        # sticky='w' alinha o conteúdo ao leste (à esquerda)
        Entry(self.container).grid(row=0, column=1)
        Label(self.container, text="Idade").grid(row=1, column=0, sticky="w")
        Entry(self.container).grid(row=1, column=1)
        Button(self.container, text="Salvar").grid(row=2, column=0, columnspan=2)