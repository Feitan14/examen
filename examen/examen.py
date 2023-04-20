import tkinter as tk
import sqlite3

# crear una conexión a la base de datos
conn = sqlite3.connect('BDExportaciones.db')

# crear una tabla si aún no existe
conn.execute('''CREATE TABLE IF NOT EXISTS TBPedimentos
                (IDExpo INTEGER PRIMARY KEY AUTOINCREMENT,
                 Transporte VARCHAR(30),
                 Aduana VARCHAR(30))''')

# función para agregar un nuevo pedimento a la tabla
def agregar_pedimento():
    transporte = transporte_entry.get()
    aduana = aduana_entry.get()
    conn.execute("INSERT INTO TBPedimentos (Transporte, Aduana) VALUES (?, ?)", (transporte, aduana))
    conn.commit()
    status_label.config(text="Pedimento agregado")

# función para eliminar un pedimento de la tabla
def eliminar_pedimento():
    id_expo = id_expo_entry.get()
    conn.execute("DELETE FROM TBPedimentos WHERE IDExpo = ?", (id_expo,))
    conn.commit()
    status_label.config(text="Pedimento eliminado")

# función para buscar pedimentos por aduana
def buscar_pedimentos():
    aduana = aduana_entry.get()
    cursor = conn.execute("SELECT * FROM TBPedimentos WHERE Aduana = ?", (aduana,))
    result = cursor.fetchall()
    if result:
        status_label.config(text="")
        for row in result:
            pedimentos_listbox.insert(tk.END, row)
    else:
        status_label.config(text="No se encontraron pedimentos para esta aduana")

# crear la ventana principal de Tkinter
root = tk.Tk()

# agregar un campo de entrada para el transporte
transporte_label = tk.Label(root, text='Transporte:')
transporte_label.pack()
transporte_entry = tk.Entry(root)
transporte_entry.pack()

# agregar un campo de entrada para la aduana
aduana_label = tk.Label(root, text='Aduana:')
aduana_label.pack()
aduana_entry = tk.Entry(root)
aduana_entry.pack()

# agregar un botón para agregar un nuevo pedimento
agregar_button = tk.Button(root, text='Agregar', command=agregar_pedimento)
agregar_button.pack()

# agregar un campo de entrada para el IDExpo del pedimento a eliminar
id_expo_label = tk.Label(root, text='IDExpo:')
id_expo_label.pack()
id_expo_entry = tk.Entry(root)
id_expo_entry.pack()

# agregar un botón para eliminar un pedimento existente
eliminar_button = tk.Button(root, text='Eliminar', command=eliminar_pedimento)
eliminar_button.pack()

# agregar un botón para buscar pedimentos por aduana
buscar_button = tk.Button(root, text='Buscar', command=buscar_pedimentos)
buscar_button.pack()

# agregar una lista para mostrar los pedimentos encontrados por la búsqueda
pedimentos_listbox = tk.Listbox(root, height=10)
pedimentos_listbox.pack()

# agregar una etiqueta para mostrar el estado de la operación
status_label = tk.Label(root, text="")
status_label.pack()

# iniciar el bucle principal de Tkinter
root.mainloop()
