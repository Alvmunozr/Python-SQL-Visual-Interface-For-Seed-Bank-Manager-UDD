import sqlite3

class Comunicacion:
    def __init__(self):
        # Conexión a la base de datos
        self.conexion = sqlite3.connect('base_datos.db')

    def inserta_datos(self, nombre, cantidad, guardada, tipo):
        cursor = self.conexion.cursor()
        consulta = '''INSERT INTO datos (NOMBRE, CANTIDAD, GUARDADA, TIPO)
                      VALUES (?, ?, ?, ?)'''
        cursor.execute(consulta, (nombre, cantidad, guardada, tipo))
        self.conexion.commit()
        cursor.close()

    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        consulta = "SELECT * FROM datos"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cursor.close()
        return datos

    def elimina_datos(self, id_fila):
        cursor = self.conexion.cursor()
        consulta = '''DELETE FROM datos WHERE ID = ?'''
        cursor.execute(consulta, (id_fila,))
        self.conexion.commit()
        cursor.close()

    def actualiza_datos(self, id_fila, nombre, cantidad, guardada, tipo):
        cursor = self.conexion.cursor()
        consulta = '''UPDATE datos 
                      SET NOMBRE = ?, CANTIDAD = ?, GUARDADA = ?, TIPO = ? 
                      WHERE ID = ?'''
        cursor.execute(consulta, (nombre, cantidad, guardada, tipo, id_fila))
        self.conexion.commit()
        cursor.close()

    def eliminar_todos(self):
        cursor = self.conexion.cursor()
        consulta = "DELETE FROM datos"
        cursor.execute(consulta)
        self.conexion.commit()
        cursor.close()
