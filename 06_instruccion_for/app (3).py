import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        flag_continuar = True
        contador = 0
        while(flag_continuar):
            print("Hola")
            contador = contador + 1 
            if(contador == 2):
                flag_continuar = False

        while(contador < 3):
            print("Hola")
            contador = contador + 1
            #if(flag):
            #    break

        precio = 1230
        lista_precios = [123,555,999,1234,99]
        lista_precios.append(23568)

        print(lista_precios[5])
        lista_precios[0] = 33

        cantidad_elementos = len(lista_precios) # 6 elementos
        indice = 0 # desde 0 hasta 5
        while(indice < cantidad_elementos):
            print(lista_precios[indice])
            indice = indice + 1
            
        #lista_numeros = range(10)

        for un_precio in lista_precios:
            print(un_precio)
            if(un_precio < 10):
                break

        cantidad_elementos = len(lista_precios) 
        for indice in range(cantidad_elementos):
            print(indice)            







        


    
if __name__ == "__main__":
    app = App()
    app.mainloop()