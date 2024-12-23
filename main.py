from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage, Menu, filedialog
from tkinter import StringVar, Scrollbar, Frame, messagebox
from conexion_sqlite import Comunicacion
from time import strftime
import pandas as pd

class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Variables para la interfaz
        self.nombre_comun = StringVar()
        self.cantidad = StringVar()
        self.guardada = StringVar()
        self.tipo = StringVar()
        self.buscar_var = StringVar()  # Variable para el campo de búsqueda
        self.cantidad_modificar = StringVar()  # Variable para edición rápida de cantidad

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=5)
        self.base_datos = Comunicacion()
        self.widgets()

    def widgets(self):
        # Estilos de la interfaz
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview.Heading", font=('Arial', 12, 'bold'), background="#4D79FF", foreground="white", relief="raised")
        estilo.configure("Treeview", font=('Arial', 10), background="#EAECEE", foreground="black", fieldbackground="white", rowheight=25)
        estilo.map('Treeview', background=[('selected', '#4D79FF')], foreground=[('selected', 'white')])

        # Crear un marco principal con estilo
        self.frame_uno = Frame(self.master, bg='#F2F4F4', height=200, width=800, bd=5, relief="ridge")
        self.frame_uno.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master, bg='#F2F4F4', height=300, width=800, bd=5, relief="ridge")
        self.frame_dos.grid(column=0, row=1, sticky='nsew')

        self.frame_uno.columnconfigure([0, 1, 2], weight=1)
        self.frame_uno.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        # Título
        Label(self.frame_uno, text='Gestión Banco de Semillas', bg='#4D79FF', fg='white', font=('Helvetica', 18, 'bold')).grid(columnspan=3, row=0, pady=10)

        # Etiquetas y entradas de la tabla con fuentes uniformes
        Label(self.frame_uno, text='Nombre Común:', fg='black', bg='#F2F4F4', font=('Arial', 12)).grid(column=0, row=1, pady=5)
        Entry(self.frame_uno, textvariable=self.nombre_comun, font=('Arial', 12), relief="solid", highlightbackground="#4D79FF", highlightthickness=2).grid(column=1, row=1, pady=5)

        Label(self.frame_uno, text='Cantidad:', fg='black', bg='#F2F4F4', font=('Arial', 12)).grid(column=0, row=2, pady=5)
        Entry(self.frame_uno, textvariable=self.cantidad, font=('Arial', 12), relief="solid", highlightbackground="#4D79FF", highlightthickness=2).grid(column=1, row=2, pady=5)

        Label(self.frame_uno, text='Guardada en:', fg='black', bg='#F2F4F4', font=('Arial', 12)).grid(column=0, row=3, pady=5)
        Entry(self.frame_uno, textvariable=self.guardada, font=('Arial', 12), relief="solid", highlightbackground="#4D79FF", highlightthickness=2).grid(column=1, row=3, pady=5)

        Label(self.frame_uno, text='Tipo:', fg='black', bg='#F2F4F4', font=('Arial', 12)).grid(column=0, row=4, pady=5)
        Entry(self.frame_uno, textvariable=self.tipo, font=('Arial', 12), relief="solid", highlightbackground="#4D79FF", highlightthickness=2).grid(column=1, row=4, pady=5)

        # Buscar
        Label(self.frame_uno, text='Buscar:', fg='black', bg='#F2F4F4', font=('Arial', 12)).grid(column=0, row=5, pady=5)
        Entry(self.frame_uno, textvariable=self.buscar_var, font=('Arial', 12), relief="solid", highlightbackground="#4D79FF", highlightthickness=2).grid(column=1, row=5, pady=5)
        Button(self.frame_uno, text='BUSCAR', font=('Arial', 11, 'bold'), bg='#1ABC9C', fg='white', width=15, command=self.buscar_datos).grid(column=2, row=5, pady=5, padx=5)

        # Botones principales de la interfaz
        Button(self.frame_uno, text='AÑADIR DATOS', font=('Arial', 11, 'bold'), bg='#3498DB', fg='white', width=15, command=self.agragar_datos).grid(column=2, row=1, pady=5, padx=5)
        Button(self.frame_uno, text='LIMPIAR CAMPOS', font=('Arial', 11, 'bold'), bg='#E67E22', fg='white', width=15, command=self.limpiar_campos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text='EDITAR FILA', font=('Arial', 11, 'bold'), bg='#9B59B6', fg='white', width=15, command=self.editar_fila).grid(column=2, row=3, pady=5, padx=5)

        # Botón OTRO con menú desplegable
        self.boton_otro = Button(self.frame_uno, text='OTRO', font=('Arial', 11, 'bold'), bg='#2ECC71', fg='white', width=15, command=self.mostrar_menu_otro)
        self.boton_otro.grid(column=2, row=4, pady=5, padx=5)

        # Menú desplegable para el botón OTRO
        self.menu_otro = Menu(self.master, tearoff=0, bg='white', fg='black', font=('Arial', 10))
        self.menu_otro.add_command(label="Exportar a Excel", command=self.guardar_datos)
        self.menu_otro.add_command(label="Cargar Datos desde Excel", command=self.cargar_datos_excel)
        self.menu_otro.add_command(label="Estadísticas Rápidas", command=self.estadisticas_rapidas)
        self.menu_otro.add_command(label="Activar Edición Rápida", command=self.activar_edicion_rapida)

        # Configuración de la tabla `Treeview`
        self.tabla = ttk.Treeview(self.frame_dos, style="Treeview")
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_dos, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = ttk.Scrollbar(self.frame_dos, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        # Configurar las columnas y encabezados de la tabla
        self.tabla['columns'] = ('Nombre Común', 'Cantidad', 'Guardada en', 'Tipo')
        self.tabla.column('#0', minwidth=50, width=60, anchor='center')
        self.tabla.column('Nombre Común', minwidth=150, width=150, anchor='center')
        self.tabla.column('Cantidad', minwidth=100, width=100, anchor='center')
        self.tabla.column('Guardada en', minwidth=150, width=150, anchor='center')
        self.tabla.column('Tipo', minwidth=100, width=100, anchor='center')

        self.tabla.heading('#0', text='ID', anchor='center')
        self.tabla.heading('Nombre Común', text='Nombre Común', anchor='center')
        self.tabla.heading('Cantidad', text='Cantidad', anchor='center')
        self.tabla.heading('Guardada en', text='Guardada en', anchor='center')
        self.tabla.heading('Tipo', text='Tipo', anchor='center')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

        # Sección de edición rápida (inicialmente oculta)
        self.frame_edicion_rapida = Frame(self.frame_uno, bg='#F2F4F4')
        self.frame_edicion_rapida.grid(column=0, row=6, columnspan=3, pady=5, sticky='w')
        self.frame_edicion_rapida.grid_remove()  # Ocultar al inicio

        Label(self.frame_edicion_rapida, text='Cantidad a modificar:', fg='black', bg='#F2F4F4', font=('Arial', 12)).grid(column=0, row=0, sticky='w', pady=5)
        Entry(self.frame_edicion_rapida, textvariable=self.cantidad_modificar, font=('Arial', 12), width=10).grid(column=1, row=0, padx=5)

        Button(self.frame_edicion_rapida, text="AGREGAR", font=('Arial', 11, 'bold'), bg='#27AE60', fg='white', width=10, command=self.aumentar_cantidad).grid(column=2, row=0, padx=5)
        Button(self.frame_edicion_rapida, text="DISMINUIR", font=('Arial', 11, 'bold'), bg='#E74C3C', fg='white', width=10, command=self.disminuir_cantidad).grid(column=3, row=0, padx=5)

        # Cargar datos al iniciar
        self.actualizar_tabla()

    def mostrar_menu_otro(self, event=None):
        self.menu_otro.tk_popup(self.boton_otro.winfo_rootx(), self.boton_otro.winfo_rooty() + 30)

    def agragar_datos(self):
        nombre_comun = self.nombre_comun.get()
        cantidad = self.cantidad.get()
        guardada = self.guardada.get()
        tipo = self.tipo.get()
        if nombre_comun and cantidad and guardada and tipo != '':
            self.base_datos.inserta_datos(nombre_comun, cantidad, guardada, tipo)
            self.actualizar_tabla()
            self.limpiar_campos()
    
    def eliminar_todos(self):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM datos")
        self.conexion.commit()
        cursor.close()

    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        for i, dato in enumerate(datos):
            self.tabla.insert('', i, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4]))

    # Otros métodos como `eliminar_datos`, `editar_fila`, `guardar_datos` se mantienen igual...
    def buscar_datos(self):
        query = self.buscar_var.get().lower()
        self.tabla.delete(*self.tabla.get_children())  # Elimina todas las filas actuales de la tabla
        datos = self.base_datos.mostrar_datos()
        for i, dato in enumerate(datos):
            if query in str(dato[1]).lower() or query in str(dato[2]).lower() or query in str(dato[3]).lower() or query in str(dato[4]).lower():
                self.tabla.insert('', i, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4]))

    def obtener_fila(self, event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.nombre_comun.set(self.data['values'][0])
        self.cantidad.set(self.data['values'][1])
        self.guardada.set(self.data['values'][2])
        self.tipo.set(self.data['values'][3])

    def eliminar_datos(self, event=None):
        try:
            item = self.tabla.selection()[0]
            id_fila = self.tabla.item(item, 'text')
            x = messagebox.askquestion('Información', '¿Desea eliminar este registro?')
            if x == 'yes':
                self.base_datos.elimina_datos(id_fila)
                self.tabla.delete(item)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un elemento para eliminar.")

    def editar_fila(self):
        try:
            item = self.tabla.focus()
            id_fila = self.tabla.item(item, 'text')
            if id_fila:
                self.base_datos.actualiza_datos(
                    id_fila,
                    self.nombre_comun.get(),
                    self.cantidad.get(),
                    self.guardada.get(),
                    self.tipo.get()
                )
                self.actualizar_tabla()
            else:
                messagebox.showwarning("Advertencia", "Por favor, seleccione una fila para editar.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo editar el registro: {e}")

    def limpiar_campos(self):
        self.nombre_comun.set('')
        self.cantidad.set('')
        self.guardada.set('')
        self.tipo.set('')

    def guardar_datos(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        df = pd.DataFrame(datos, columns=['ID', 'Nombre Común', 'Cantidad', 'Guardada en', 'Tipo'])
        fecha = str(strftime('%d-%m-%y_%H-%M-%S'))
        df.to_excel(f'DATOS {fecha}.xlsx')
        messagebox.showinfo('Información', 'Datos guardados en Excel.')

    def cargar_datos_excel(self):
        archivo = filedialog.askopenfilename(title="Seleccionar Archivo Excel", filetypes=[("Archivos Excel", "*.xlsx *.xls")])
        if archivo:
            self.base_datos.eliminar_todos()  # Elimina los datos actuales para cargar los nuevos
            df = pd.read_excel(archivo)
            for _, fila in df.iterrows():
                self.base_datos.inserta_datos(fila['Nombre Común'], fila['Cantidad'], fila['Guardada en'], fila['Tipo'])
            messagebox.showinfo("Éxito", "Base de datos cargada correctamente desde el archivo Excel.")
            self.actualizar_tabla()


    def estadisticas_rapidas(self):
        datos = self.base_datos.mostrar_datos()
        if datos:
            total = len(datos)
            promedio = sum([float(dato[2]) for dato in datos]) / total
            messagebox.showinfo("Estadísticas Rápidas", f"Total de semillas: {total}\nPromedio de Cantidad: {round(promedio, 1)}")
        else:
            messagebox.showinfo("Estadísticas Rápidas", "No hay datos en la base de datos.")

    def activar_edicion_rapida(self):
        #"Muestra u oculta la sección de edición rápida"
        if self.frame_edicion_rapida.winfo_ismapped():
            self.frame_edicion_rapida.grid_remove()  # Oculta la sección
        else:
            self.frame_edicion_rapida.grid()  # Muestra la sección
    
    def aumentar_cantidad(self):
        try:
            cantidad_aumentar = int(self.cantidad_modificar.get())
            item = self.tabla.focus()
            if not item:
                messagebox.showwarning("Advertencia", "Por favor, seleccione una fila para modificar.")
                return
            valores = self.tabla.item(item, 'values')
            nueva_cantidad = int(valores[1]) + cantidad_aumentar
            id_fila = self.tabla.item(item, 'text')

            # Actualizar en la base de datos
            self.base_datos.actualiza_datos(id_fila, valores[0], nueva_cantidad, valores[2], valores[3])

            # Actualizar en la tabla
            self.tabla.item(item, values=(valores[0], nueva_cantidad, valores[2], valores[3]))
            self.cantidad_modificar.set('')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

    def disminuir_cantidad(self):
        try:
            cantidad_disminuir = int(self.cantidad_modificar.get())
            item = self.tabla.focus()
            if not item:
                messagebox.showwarning("Advertencia", "Por favor, seleccione una fila para modificar.")
                return
            valores = self.tabla.item(item, 'values')
            nueva_cantidad = max(0, int(valores[1]) - cantidad_disminuir)  # No permite cantidades negativas
            id_fila = self.tabla.item(item, 'text')

            # Actualizar en la base de datos
            self.base_datos.actualiza_datos(id_fila, valores[0], nueva_cantidad, valores[2], valores[3])

            # Actualizar en la tabla
            self.tabla.item(item, values=(valores[0], nueva_cantidad, valores[2], valores[3]))
            self.cantidad_modificar.set('')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")




if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Gestión Banco de Semillas')
    ventana.minsize(height=800, width=1200)
    ventana.geometry('800x500')
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    app = Ventana(ventana)
    app.mainloop()
