import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from unittest import case
import customtkinter

'''
Nombre:Belén
Apellido:Chacón

Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%.

		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 %
            y si es de otra marca el descuento es del 30%.

		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 %
            y si es de otra marca el descuento es del 20%.

		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas”
            se hace un descuento del 10 % y si es de otra marca un 5%.

		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=[
                                                        "ArgentinaLuz", "FelipeLamparas", "JeLuz", "HazIluminacion", "Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(
            master=self, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")

  #  def btn_calcular_on_click(self):#otro renglon \n
  #         marca = self.combobox_marca.get()
   #         cantidad_texto= self.combobox_cantidad.get()
   #         cantidad_numero = int (cantidad_texto)
   #         descuento=0
   #
   #         if(cantidad_numero >=6):
   #             descuento=50
   #         elif(cantidad_numero == 5):
   #             if(marca=="ArgentinaLuz"):
   #                 descuento=40
   #             else:
   #                 descuento=30
   #         elif(cantidad_numero == 4):
   #             if(marca=="ArgentinaLuz" or marca== "FelipeLamparas"):
   #                 descuento=25
   #             else:
   #                 descuento=20
   #         elif(cantidad_numero == 3):
   # if(marca =="ArgentinaLuz"):
   #                 descuento=15
   #             elif(marca =="FelipeLamparas"):
  #                 descuento=10
  #              else:
  #                  descuento=5

   #         sub_total=800 *cantidad_numero
   #         ahorro=sub_total * (descuento / 100)
   #         total_con_descuento= sub_total - ahorro
   #         ahorro_adicional=0
    #        if(total_con_descuento > 4000):
    #            ahorro_adicional=total_con_descuento * (5/100)
    #        total_a_pagar= total_con_descuento - ahorro_adicional

  #          mensaje= "La marca es {0} \n La cantidad es {1} \n El descuento es {2} \n TOTAL (s/desc) {3} \n El aahorro fue {4} \n Total {5} \n Ahorro AD (5%) {6} \n\n TOTAL A PAGAR {7} ".format(marca,cantidad_texto,descuento,sub_total,ahorro,total_con_descuento,ahorro_adicional,total_a_pagar)
#          alert(title="test", message=mensaje)

    def btn_calcular_on_click(self):  # otro renglon \n
        marca = self.combobox_marca.get()
        cantidad_texto = self.combobox_cantidad.get()
        cantidad_numero = int(cantidad_texto)
        descuento = 0

        match(cantidad_numero):
            case 1 | 2:
                descuento = 0
            case 3:
                match(marca):
                    case "ArgentinaLuz":
                        descuento = 15
                    case "FelipeLamparas":
                        descuento = 10
                    case _:
                        descuento = 5
            case 4:
                match(marca):
                    case "ArgentinaLuz" | "FelipeLamparas":
                        descuento = 25  
                    case _:
                        descuento = 20    
            case 5:
                match(marca):
                    case "ArgentinaLuz":
                        descuento = 40
                    case _:
                        descuento = 30 
            case _:
                    descuento = 50

        sub_total = 800 * cantidad_numero
        ahorro = sub_total * (descuento / 100)
        total_con_descuento = sub_total - ahorro
        
        ahorro_adicional = 0
        if (total_con_descuento > 4000):
            ahorro_adicional = total_con_descuento * (5/100)
        total_a_pagar = total_con_descuento - ahorro_adicional


        mensaje = "La marca es {0} \n La cantidad es {1} \n El descuento es {2} \n TOTAL (s/desc) {3} \n El aahorro fue {4} \n Total {5} \n Ahorro AD (5%) {6} \n\n TOTAL A PAGAR {7} ".format(marca,cantidad_texto,descuento,sub_total,ahorro,total_con_descuento,ahorro_adicional,total_a_pagar) 
        alert(title="test", message=mensaje)


if __name__ == "__main__":
    app = App()
    app.mainloop()