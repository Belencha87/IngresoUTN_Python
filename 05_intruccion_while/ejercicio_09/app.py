import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Belen Chacon
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        bandera_continuar= True
        numero_maximo = None
        numero_minimo = None
        
        
        while(bandera_continuar == True):
            num_txt = prompt(title="", prompt=" Ingreso un número:")
            if( num_txt == None):
                bandera_continuar = False
            else:
                num_int = int (num_txt)
                if (numero_maximo == None or num_int > numero_maximo ):
                    numero_maximo = num_int 
                else:
                    (numero_minimo == None or num_int < numero_minimo )
                    numero_minimo = num_int 
                    
        
        self.txt_minimo.delete(0,100) 
        self.txt_minimo.insert(0,numero_minimo)
        self.txt_maximo.delete(0,100)
        self.txt_maximo.insert(0,numero_maximo)
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
