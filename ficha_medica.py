from tkinter import *
from openpyxl import load_workbook

# Inicializa la ventana de Tkinter
ficha = Tk()
ficha.geometry("500x600")
ficha.configure(bg="dark blue")

# Carga el archivo de Excel y selecciona la hoja "ficha medica"
# ojo borra este comantario:puse una reta generica para la ruta cambiar a la ruta vieja "/ruta/del/archivo/EXCEL(BASE DE DATOS.T).xlsx"
workbook_path = "../EXCEL(BASE DE DATOS.T).xlsx"
workbook = load_workbook(workbook_path)
sheet = workbook["ficha medica"]

# Función para guardar los datos en Excel
def funcion_click():
    # Obtiene el índice de la celda C2 y lo incrementa
    index = sheet["C2"].value
    if index is None:
        index = 1
    else:
        index += 1
    sheet["C2"].value = index
    
    # Guarda los datos en las celdas correspondientes
    sheet[f"B{index}"] = entry_nombre.get()
    sheet[f"C{index}"] = entry_apellido.get()
    sheet[f"D{index}"] = entry_dni.get()
    sheet[f"E{index}"] = entry_alergias.get()
    sheet[f"F{index}"] = entry_cirugias.get()
    sheet[f"G{index}"] = entry_lesiones.get()
    
    # Guarda los cambios en el archivo de Excel
    workbook.save(workbook_path)
    print("Datos guardados en Excel.")

# Etiquetas y campos de entrada
Label(ficha, text="Información Deportiva", bg="dark blue", fg="white", font=("Lato", 13)).place(x=180, y=50)
Button(ficha, text="Guardar", command=funcion_click, bg="dark blue", fg="white", font=("Lato", 13)).place(x=180, y=350)

Label(ficha, text="Nombre:", bg="dark blue", fg="white", font=("Lato", 12)).place(x=10, y=100)
entry_nombre = Entry(ficha)
entry_nombre.place(x=150, y=100)

Label(ficha, text="Apellido:", bg="dark blue", fg="white", font=("Lato", 12)).place(x=10, y=140)
entry_apellido = Entry(ficha)
entry_apellido.place(x=150, y=140)

Label(ficha, text="DNI:", bg="dark blue", fg="white", font=("Lato", 12)).place(x=10, y=180)
entry_dni = Entry(ficha)
entry_dni.place(x=150, y=180)

Label(ficha, text="Alergias:", bg="dark blue", fg="white", font=("Lato", 12)).place(x=10, y=220)
entry_alergias = Entry(ficha)
entry_alergias.place(x=150, y=220)

Label(ficha, text="Cirugías Previas:", bg="dark blue", fg="white", font=("Lato", 12)).place(x=10, y=260)
entry_cirugias = Entry(ficha)
entry_cirugias.place(x=150, y=260)

Label(ficha, text="Lesiones Previas:", bg="dark blue", fg="white", font=("Lato", 12)).place(x=10, y=300)
entry_lesiones = Entry(ficha)
entry_lesiones.place(x=150, y=300)

# Inicia el bucle principal de Tkinter
ficha.mainloop()
