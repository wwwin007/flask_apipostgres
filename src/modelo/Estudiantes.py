from modelo.Coneccion import conexion2023
from flask import jsonify, request

def buscar_estu(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM estudiantes WHERE ci = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()

        if datos != None:
            estu = {'cedula_identidad': datos[0], 'nombre': datos[1],
                       'apell_pat': datos[2], 'apell_mat': datos[3],
                       'procedencia': datos[4]}
            return estu
        else:
            return None
    except Exception as ex:
            raise ex
    

class ModeloEstudiante:
    @classmethod
    def listar_Estudiante(self):
        try:
            conn = conexion2023()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM estudiantes")
            datos = cursor.fetchall()
            estudiantes = []

            for fila in datos:
                estu = {'cedula_identidad': fila[0],
                       'nombre': fila[1],
                       'apell_pat': fila[2],
                       'apell_mat': fila[3],
                       'procedencia': fila[4]}
                estudiantes.append(estu)

            conn.close()

            return jsonify({'estudiantes': estudiantes, 'mensaje': "estudiantes listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})
    
    @classmethod
    def lista_Estudiante(self,codigo):
        try:
            usuario = buscar_estu(codigo)
            if usuario != None:
                return jsonify({'usuarios': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def registrar_estudiante(self):
        try:
            usuario = buscar_estu(request.json['ci_e'])
            if usuario != None:
                return jsonify({'mensaje': "Cedula de identidad  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT INTO estudiantes values(%s,%s,%s,%s,%s)', (request.json['ci_e'], request.json['nombre_e'], request.json['apell_pat_e'],
                                                                            request.json['apell_mat_e'], request.json['procedencia_e']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    
    @classmethod
    def actualizar_estudiante(self,codigo):
        try:
            usuario = buscar_estu(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE estudiantes SET nombre=%s, apell_pat=%s, apell_mat=%s,
                procedencia=%s WHERE ci=%s""",
                        (request.json['nombre_e'], request.json['apell_pat_e'], request.json['apell_mat_e'], request.json['procedencia_e'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "estudiante actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "estudiante  no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def eliminar_estuy(self,codigo):
        try:
            usuario = buscar_estu(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM estudiantes WHERE ci = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "estudiantes eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "estudiante no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})