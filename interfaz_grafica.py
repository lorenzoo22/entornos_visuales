import tkinter as tk
from tkinter import Frame,Label,Button

import Comprador                                      #me importo el modulo comprador
from Comprador import Comprador                       #me importo la clase comprador

import Vendedor                              #me importo el modulo vendedor f
from Vendedor import Vendedor                #me importo la clase Vendedor del modulo Vendedor
import psycopg2


root1 =tk.Tk()
root1.title("NFT´S")
global a                                           #me creo una variable global inicializada a 0 que luego será de uso en las funciones
a=0

#---------------------------funciones---------------------------#
def cambiapágina(a):
    if a==1:
        print("cambio")
        root1.destroy()
        comprador1 =Comprador()
        comprador1.VentanaNueva()
    if a==2:
        root1.destroy()
        vendedor1 =Vendedor()
        vendedor1.VentanaNueva2()
#---------------------------creacion del marco---------------------------#
marco = Frame(root1)
marco.pack(side="top",fill="x")
marco.config(bg="blue",width=800,height=180)

marco2 = Frame(root1)
marco2.pack(fill="both",expand=True)
marco2.config(bg="red")

#---------------------------Ventanas---------------------------#

ventana_ppal =Label(marco2,text="COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
ventana_ppal.place(x=150,y=170)

ventana_ppal2 =Label(marco2,text="VENDEDOR",font=("Comic Sans MS",40),fg="GREEN")
ventana_ppal2.place(x=950,y=170)

ventana_ppal3 =Label(marco,text="BIENVENIDO",font=("Comic Sans MS",40),fg="GREEN")
ventana_ppal3.place(x=500,y=0)

#---------------------------Botones---------------------------#

boton1=Button(marco2,text="¿quieres comprar?",command=lambda: cambiapágina(1),width=47)
boton1.place(x=150,y=270)

boton2=Button(marco2,text="¿quieres vender?",command=lambda: cambiapágina(2),width=41)
boton2.place(x=950,y=270)


#---------creacion de las tablas-------------#
conn = psycopg2.connect(
    host ="ec2-23-23-182-238.compute-1.amazonaws.com",
    database="d8jkpbdn8n5tau",
    user= "sfgectibhzlelp",
    password="e30184e8472a143402057f1b68c02afac1e0ffd8b3c504783772a6362b67fe3c",
    port="5432"
    )
# conn.database()
cursor = conn.cursor()
# query1= "SHOW TABLES"
# cursor.execute(query1)
query = '''CREATE TABLE IF NOT EXISTS tabla_contador (id SERIAL PRIMARY KEY, nombre TEXT,apellido TEXT,nft TEXT ,riesgo TEXT);'''
cursor.execute(query)
conn.commit()
conn.close()
print("se ha creado el registro")


root1.mainloop()
