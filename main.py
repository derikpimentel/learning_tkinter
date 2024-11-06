from tkinter import *

# Estrutura da aplicação
class Application:
    def __init__(self, master=None):
        self.master = master # Faz a passagem da variável "root"

# Estrutura de execução
if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()