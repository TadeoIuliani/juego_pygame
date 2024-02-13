import sqlite3

# with sqlite3.connect("ranking.db") as conexion:
#     try:
#         sentencia = """
#                     CREATE TABLE nivel_3(
#                     nombre text,
#                     puntaje integer
#                     )
#                     """
#         conexion.execute(sentencia)
#         conexion.commit()
#         print("Se creo correctamente")
#     except:
#         print("error !!!")


SENTENCIA_AGREGAR_REGISTRO = f"INSERT into nivel_"
SENTENCIA_RETORNAR_RANKING = f"SELECT * from nivel_"
SENTENCIA_RESETEO_NIVEL = f"DELETE from nivel_"

def agregar_regristro(bd : str, nivel : int, usuario : str, puntaje : int):
    if nivel > 0 and nivel < 4:
        sentencia = SENTENCIA_AGREGAR_REGISTRO + f"{nivel}(nombre, puntaje) values('{usuario}', {puntaje})"
    conectar_y_ejecutar(bd, sentencia)


def conectar_y_ejecutar(path : str, sentencia : str):
    if sentencia != None and path != None:
        retorno = []
        conexion = sqlite3.connect(path)
        respuesta = conexion.execute(sentencia)
        for fila in respuesta:
            retorno.append(fila)
        conexion.commit()
        conexion.close()
        return retorno

def traer_ranking(bd : str, nivel : int):
    if nivel > 0 and nivel < 4:
        sentencia = SENTENCIA_RETORNAR_RANKING + f"{nivel} order by puntaje desc limit 4"

    cursor = conectar_y_ejecutar(bd, sentencia)
    if cursor != None:
        return cursor

def resetear_juego(bd):
    conectar_y_ejecutar(bd, SENTENCIA_RESETEO_NIVEL + "1")
    conectar_y_ejecutar(bd, SENTENCIA_RESETEO_NIVEL + "2")
    conectar_y_ejecutar(bd, SENTENCIA_RESETEO_NIVEL + "3")
