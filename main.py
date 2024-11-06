from tkinter import *

# Estrutura da aplicação
class Application:
    def __init__(self, master=None):
        self.master = master # Faz a passagem da variável "root"

        self.label = Label(self.master) # Cria uma Label
        self.label["text"] = "Olá, mundo!" # Define o texto a ser exibido
        self.label["font"] = ("Arial", 12, "bold") # Altera a fonte do texto
        self.label["bg"] = "black" # Define a cor de fundo
        self.label["fg"] = "white" # Define a cor do texto
        self.label["width"] = 20 # Define a largura (unid. de texto ou pixels p/ imagens)
        self.label["height"] = 5 # Define a altura (unid. de texto ou pixels p/ imagens)
        self.label["padx"] = 10 # Define um espaçamento interno na horizontal
        self.label["pady"] = 10 # Define um espaçamento interno na vertical
        #image = PhotoImage(file="image.png") # Carrega uma imagem
        #self.label["image"] = image # Define uma imagem a ser exibida
        self.label.pack() # Posiciona o Label na janela (forma simples)

        self.button = Button(self.master) # Cria um Button
        self.button["text"] = "Clique Aqui!"
        self.button["command"] = self.on_click # Função a ser chamada quando clicado
        self.button["state"] = "normal" # Define o estado do botão ('normal', 'disabled' e 'active')
        self.button["bg"] = "lightgreen"
        self.button["fg"] = "darkgray"
        self.button["width"] = 10
        self.button["height"] = 1
        self.button["font"] = ("Helvetica", 14)
        self.button["borderwidth"] = 3 # Define a espessura da borda
        self.button["relief"] = "raised" # Define o estilo da borda ('flat', 'raised', 'sunken', 'groove' e 'ridge')
        self.button["padx"] = 5
        self.button["pady"] = 5
        #img = PhotoImage(file="img.png")
        #self.button["image"] = img
        self.button.pack()

        # Criando um container para posicionar os widgets com grid()
        self.container_entry = Frame(self.master)
        self.container_entry.pack()

        """ Campo de entrada de texto com linha única """
        self.login_entry = Entry(self.container_entry) #  Cria um Entry
        self.login_entry["width"] = 15
        self.login_entry["bg"] = "lightgray"
        self.login_entry["fg"] = "blue"
        self.login_entry["font"] = ("Helvetica", 12, "italic")
        self.login_entry.insert(0, "Usuário") # Define um texto inicial
        self.login_entry["state"] = "normal" # ('disabled', 'normal' e 'readonly')
        self.login_entry.grid(row=0, column=0) # Posiciona por linha e coluna na janela

        self.key_entry = Entry(self.container_entry)
        self.key_entry["show"] = "*" # Substitui o texto digitado por um caractere específico
        self.key_entry["width"] = 15
        self.key_entry["font"] = ("Helvetica", 12)
        self.key_entry.insert(0, "Senha")
        self.key_entry.grid(row=1, column=0)

        self.key_button = Button(self.container_entry, text="Mostar Senha", command=self.key_show)
        self.key_button.grid(row=1, column=1)

        self.login_button = Button(self.container_entry, text="Entrar", command=self.authenticate, padx=40)
        self.login_button.grid(row=2, columnspan=2)

        self.status_con = StringVar() # Variável para texto dinâmico

        self.status_entry = Entry(self.container_entry)
        self.status_entry["textvariable"] = self.status_con
        self.status_entry["width"] = 37
        self.status_entry["state"] = "readonly" # Apenas leitura
        self.status_entry.grid(row=3, columnspan=2)

    # Função a ser executada ao clicar no botão
    def on_click(self):
        print("Botão pressionado!")
        self.label.config(text="Obrigado!") # Altera o texto da Label
        self.button.config(text="Clicado!") # Altera o texto do Button
        self.button.config(bg="gray") # Altera a cor de fundo do Button
        self.button.config(state="disabled") # Altera o estado do Button

    # Função para exibir e ocultar senha
    def key_show(self):
        if self.key_entry["show"] == "*":
            self.key_entry.config(show="")
            self.key_button.config(text="Ocultar Senha")
        else:
            self.key_entry.config(show="*")
            self.key_button.config(text="Mostar Senha")

    # Função para TESTES de autenticação
    def authenticate(self):
        login = self.login_entry.get()
        key = self.key_entry.get()
        print(f"Usuário: '{login}'")
        if (login == "Derik") and (key == "12345"):
            print("Conexão bem sucedida!")
            self.status_con.set("Conectado!") # Atualiza a variável
            self.login_entry.delete(0, "end") # Remove o texto do campo
            self.login_entry.insert(0, "Usuário")
            self.key_entry.delete(0, "end")
            self.key_entry.insert(0, "Senha")
        else:
            print("Falha de conexão!")
            self.status_con.set("Usuário e/ou senha incorretos!")

# Estrutura de execução
if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()