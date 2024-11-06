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

    # Função a ser executada ao clicar no botão
    def on_click(self):
        print("Botão pressionado!")
        self.label.config(text="Obrigado!") # Altera o texto da Label
        self.button.config(text="Clicado!") # Altera o texto do Button
        self.button.config(bg="gray") # Altera a cor de fundo do Button
        self.button.config(state="disabled") # Altera o estado do Button

# Estrutura de execução
if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()