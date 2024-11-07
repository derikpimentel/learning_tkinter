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

        self.container_text = Frame(self.master)
        self.container_text.pack()

        self.message = Text(self.container_text, width=30, height=10)
        self.message["wrap"] = "word" # Controla como o texto será quebrado ('char', 'word' e 'none')
        self.message.insert("1.0", "Escreva sua mensagem...") # '1.0' representa a primeira linha e primeira coluna
        self.message.config(state="disabled")
        self.message.tag_config("bold", font=("Arial", 12, "bold")) # Criando TAG para negrito
        self.message.grid(row=0, column=0, rowspan=5, sticky="nsew")
        """
        Expande o Text nas direções 'n' norte, 's' sul, 'e' leste e 'w' oeste.
        """
        #img = PhotoImage(file="img.png")
        #self.message.image_create("insert", image=img) # Insere imagem na posição do cursor

        # Cria uma barra de rolagem para associar a caixa de mensagem
        self.scrollbar = Scrollbar(self.container_text, command=self.message.yview)
        self.scrollbar.grid(row=0, column=1, rowspan=5, sticky="ns")
        """
        Expande o Scrollbar nas direções norte e sul
        """

        self.message.config(yscrollcommand=self.scrollbar.set) # Integra a Scrollbar na Text

        # Ajustando o redimensionamento das colunas e linhas
        self.container_text.grid_rowconfigure(0, weight=1) # Permite expandir a linha 0
        self.container_text.grid_columnconfigure(0, weight=1) # Permite expandir a coluna 0

        self.delete_button = Button(
            self.container_text, 
            text="Apagar Mensagem", 
            command=self.delete_message,
            state="disabled",
            width=15
        )
        self.delete_button.grid(row=1, column=2)

        self.send_button = Button(
            self.container_text, 
            text="Enviar Mensagem", 
            command=self.send_message,
            state="disabled",
            width=15
        )
        self.send_button.grid(row=2, column=2)

        self.cursor_button = Button(
            self.container_text,
            text="Ir para o Início",
            command=self.position_cursor,
            state="disabled",
            width=15
        )
        self.cursor_button.grid(row=3, column=2)

        self.bold_button = Button(
            self.container_text,
            text="Negrito",
            command=self.bold_text,
            state="disabled",
            width=15
        )
        self.bold_button.grid(row=4, column=2)

        self.container_check = Frame(self.master)
        self.container_check.pack()

        self.int_option = IntVar() # Variável Integer dinâmica

        self.option_one = Checkbutton(self.container_check)
        self.option_one["text"] = "Opção 1"
        self.option_one["variable"] = self.int_option
        self.option_one["command"] = self.check_states
        self.option_one["bg"] = "light blue"
        self.option_one["fg"] = "red"
        self.option_one.grid(row=0, column=0)

        self.bool_option = BooleanVar() # Variável Boolean dinâmica

        self.option_two = Checkbutton(self.container_check)
        self.option_two["text"] = "Opção 2"
        self.option_two["variable"] = self.bool_option
        self.option_two["command"] = self.check_states
        self.option_two["font"] = ("Arial", 8, "bold")
        self.option_two.grid(row=0, column=1)

        self.str_option = StringVar() # Inicializa uma string VAZIA

        self.option_three = Checkbutton(self.container_check)
        self.option_three["text"] = "Opção 3"
        self.option_three["variable"] = self.str_option
        self.option_three["onvalue"] = "Ativado" # Valor quando marcado
        self.option_three["offvalue"] = "Desativado" # Valor quando desmarcado
        self.option_three["command"] = self.check_states
        self.option_three.deselect() # Desmarca o Checkbutton
        """
        A string VAZIA (por padrão) marca o checkbutton. A menos que a 'offvalue' seja definida também como VAZIA ''.
        """
        self.option_three.grid(row=0, column=2)

        self.allcheck_button = Button(self.container_check)
        self.allcheck_button["text"] = "Marcar Todos"
        self.allcheck_button["command"] = self.toggle_all_checks_together
        self.allcheck_button["width"] = 15
        self.allcheck_button.grid(row=1, column=0, columnspan=3)

        self.togglecheck_button = Button(self.container_check)
        self.togglecheck_button["text"] = "Alternar Marcadores"
        self.togglecheck_button["command"] = self.toggle_all_checks
        self.togglecheck_button["width"] = 15
        self.togglecheck_button.grid(row=2, column=0, columnspan=3)

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
            self.message.config(state="normal")
            self.delete_button.config(state="normal")
            self.send_button.config(state="normal")
            self.cursor_button.config(state="normal")
            self.bold_button.config(state="normal")
        else:
            print("Falha de conexão!")
            self.status_con.set("Usuário e/ou senha incorretos!")
            self.message.config(state="disabled")
            self.delete_button.config(state="disabled")
            self.send_button.config(state="disabled")
            self.cursor_button.config(state="disabled")
            self.bold_button.config(state="disabled")

    # Função para deletar a mensagem
    def delete_message(self):
        self.message.delete("1.0", "end") # Remove o texto do início ao fim
        self.message.insert("1.0", "Escreva sua mensagem...")

    # Função para TESTAR um envio de mensagem
    def send_message(self):
        message = self.message.get("1.0", "end") # Pega o texto do início ao fim
        print(f"A mensagem enviado foi:\n''\n    {message}''")

    # Função que alterna o posicionamento do cursor
    def position_cursor(self):
        if self.cursor_button["text"] == "Ir para o Início":
            self.message.mark_set("insert", "1.0")
            self.cursor_button.config(text="Ir para o Final")
        else:
            self.message.mark_set("insert", "end")
            self.cursor_button.config(text="Ir para o Início")

    # Função que alterna o estilo do texto
    def bold_text(self):
        if self.bold_button["text"] == "Negrito":
            self.message.tag_add("bold", "1.0", "1.end")
            self.bold_button.config(text="Normal")
        else:
            self.message.tag_remove("bold", "1.0", "1.end")
            self.bold_button.config(text="Negrito")

    # Função que mostra os valores das variáveis dos checkbuttons
    def check_states(self):
        print(f"Opção 1: {self.int_option.get()}")
        print(f"Opção 2: {self.bool_option.get()}")
        print(f"Opção 3: {self.str_option.get()}")

    # Função que marca\desmarca todos o checkbuttons
    def toggle_all_checks_together(self):
        if self.allcheck_button["text"] == "Marcar Todos":
            self.option_one.select() # Marca o Checkbutton
            self.option_two.select()
            self.option_three.select()
            self.allcheck_button.config(text="Desmarcar Todos")
        else:
            self.option_one.deselect()
            self.option_two.deselect()
            self.option_three.deselect()
            self.allcheck_button.config(text="Marcar Todos")

    # Função que alterna os marcadores
    def toggle_all_checks(self):
        self.option_one.toggle() # Alterna entre marcado\desmarcado
        self.option_two.toggle()
        self.option_three.toggle()

# Estrutura de execução
if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()