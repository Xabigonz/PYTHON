import tkinter as tk

#CREAR ELEMENTOS NECESARIOS PARA LA APLICACIÓN:

frame = tk.Tk()
panel = tk.Frame(frame)
bot = tk.Button(panel, text="CLICKAME", background="red")


#EL PACK ES EL LAYOUT POR DEFECTO DE PYTHON, hay más: grid y demás.
panel.grid()
bot.grid(row=2,column=2,pady=14)


#TAMAÑO Y VISUALIZAR:


frame.title("Menú")
frame.geometry("400x400")


frame.mainloop()
