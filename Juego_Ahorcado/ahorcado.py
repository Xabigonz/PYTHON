import tkinter as tk


#CREAR ELEMENTOS NECESARIOS PARA LA APLICACIÓN:

framePanel = tk.Tk()

bot = tk.Button(framePanel, text="CLICKAME", background="red")


#EL PACK ES EL LAYOUT POR DEFECTO DE PYTHON, hay más: grid y demás.

bot.grid(pady=180, padx=172)

#Crear un boton:



#TAMAÑO Y VISUALIZAR:


framePanel.title("Menú")
framePanel.geometry("400x400")


framePanel.mainloop()
