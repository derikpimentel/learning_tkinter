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

        # Cria um PanedWindow (Janela de painéis)
        self.h_paned = PanedWindow(self.master)
        self.h_paned["orient"] = "horizontal"
        self.h_paned.pack(fill="both", expand=True)

        self.v_paned = PanedWindow(self.h_paned, orient="vertical")
        self.h_paned.add(self.v_paned, minsize=100) # Acrescenta o painel com tamanho mínimo

        self.left_label = Label(self.v_paned)
        self.left_label["text"] = "Painel esquerdo superior"
        self.left_label["bg"] = "lightyellow"
        self.v_paned.add(self.left_label, minsize=100)

        self.v_paned.add(Label(self.v_paned, text="Painel esquerdo inferior"), minsize=100)

        self.center_label = Label(self.h_paned)
        self.center_label["text"] = "Painel central"
        self.center_label["bg"] = "lightblue"
        self.h_paned.add(self.center_label, minsize=100)
        self.h_paned.forget(self.center_label) # Remove o painel

        self.right_label = Label(self.h_paned)
        self.right_label["text"] = "Painel direito"
        self.right_label["bg"] = "lightgreen"
        self.h_paned.add(self.right_label, minsize=100)