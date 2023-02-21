import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''

Belén Chacón
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

#corregido enviar
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_suma_acumulada = customtkinter.CTkEntry(
            master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(
            master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,columnspan=2, sticky="nsew")

        """self.btn_cancelar = customtkinter.CTkButton(master=self, text="Cancelar", command=self.btn_cancelar_on_click)
        self.btn_cancelar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")"""

    def btn_comenzar_ingreso_on_click(self):
        flag_continuar = True # en este caso es igual  1 + 1 
        acumulador_general = 0
        contador_numeros_ingresados = 0

        while (flag_continuar == True): #en este caso es iguala poner 2
            numero_txt = prompt(title="Numero", prompt="Ingrese el número")
            if (numero_txt == None):
                flag_continuar +=1
            else:
                numero_int = int(numero_txt)
                acumulador_general = acumulador_general + numero_int     # contador_numeros_asignados + numero_int
                contador_numeros_ingresados = contador_numeros_ingresados +  1  #contador_numeros_ingresados = flag_continuar + 1
            if contador_numeros_ingresados != 0: #por si se cancela en primer intento
                promedio_numero_ingresados = acumulador_general / contador_numeros_ingresados
            else:
                promedio_numero_ingresados = 0

        self.txt_suma_acumulada.delete(0,100) 
        self.txt_suma_acumulada.insert(0,acumulador_general)
        self.txt_promedio.delete(0,100)
        self.txt_promedio.insert(0,promedio_numero_ingresados)



if __name__ == "__main__":
    app = App()
    app.mainloop()
