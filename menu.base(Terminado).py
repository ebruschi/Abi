from tkinter import *

ventana = Tk()
ventana.geometry("500x600")
ventana.configure(bg="dark blue")

# Crea el menú de la ventana
menu_superior = Menu(ventana)  # Añadir 'ventana' como argumento

# Se muestra la barra de menú en la ventana principal
ventana.config(menu=menu_superior)

# Se comienzan a crear las opciones
jugadores = Menu(menu_superior, tearoff=0)
socios = Menu(menu_superior, tearoff=0)
ayuda = Menu(menu_superior, tearoff=0)
salir = Menu(menu_superior, tearoff=0)
Categoria = Menu(menu_superior, tearoff=0)
hombre = Menu(Categoria, tearoff=0)
mujer = Menu(Categoria, tearoff=0)
Ninos = Menu(Categoria, tearoff=0)

# Agregar las opciones principales
menu_superior.add_cascade(label="Jugador", menu=jugadores)
menu_superior.add_cascade(label="Funcionalidad", menu=Categoria)
menu_superior.add_cascade(label="Socio", menu=socios)
menu_superior.add_cascade(label="Ayuda", menu=ayuda)
menu_superior.add_cascade(label="Salir", menu=salir)

# Se crean subopciones para archivo
jugadores.add_command(label="ficha medica")
jugadores.add_separator()
jugadores.add_command(label="legajo del jugador")

# Sub opción de socios
socios.add_command(label="Beneficios")
socios.add_separator()
socios.add_command(label="pagos")

# Sub opción de ayuda
ayuda.add_command(label="Acerca de...")
ayuda.add_separator()
ayuda.add_command(label="Historia del club")

# Sub opción categoría
Categoria.add_cascade(label="Informacion deportiva", menu=Ninos)
#Categoria.add_separator()
#Categoria.add_cascade(label="Categoria", menu=hombre)
#Categoria.add_separator()
#Categoria.add_cascade(label="Division", menu=mujer)
#Categoria.add_separator()


# Masculino
#hombre.add_command(label="Seniors")
#hombre.add_command(label="Veteranos")
#hombre.add_command(label="Femenino")

# Femenino
#mujer.add_command(label="Primera A")
#mujer.add_command(label="Primera B")
#mujer.add_command(label="Primera C")

# Niños
#Ninos.add_command(label="C-15")
#Ninos.add_command(label="C-13")
#Ninos.add_command(label="C-11")

ventana.mainloop()  
