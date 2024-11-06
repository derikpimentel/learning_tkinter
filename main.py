from tkinter import *

# Estrutura da aplicação
class Application:
    def __init__(self, master=None):
        self.master = master # Faz a passagem da variável "root"

        label = Label(self.master) # Cria uma Label
        label["text"] = "Olá, mundo!" # Define o texto a ser exibido
        label["font"] = ("Arial", 12, "bold") # Altera a fonte do texto
        label["bg"] = "black" # Define a cor de fundo
        label["fg"] = "white" # Define a cor do texto
        label["width"] = 20 # Define a largura (unid. de texto ou pixels p/ imagens)
        label["height"] = 5 # Define a altura (unid. de texto ou pixels p/ imagens)
        label["padx"] = 10 # Define um espaçamento interno na horizontal
        label["pady"] = 10 # Define um espaçamento interno na vertical
        #image = PhotoImage(file="image.png") # Carrega uma imagem
        #label["image"] = image # Define uma imagem a ser exibida
        label.pack() # Posiciona o Label na janela (forma simples)

# Estrutura de execução
if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()