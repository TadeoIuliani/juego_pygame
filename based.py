import sqlite3

SENTENCIA_AGREGAR_REGISTRO = f"INSERT into ranking"
SENTENCIA_RETORNAR_RANKING = f"SELECT * from ranking"
SENTENCIA_RESETEO = f"DELETE from ranking"

def agregar_regristro(bd : str, usuario : str, puntaje : int):
    sentencia = SENTENCIA_AGREGAR_REGISTRO + f"(nombre, puntaje) values('{usuario}', {puntaje})"
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

def traer_ranking(bd : str):
    if bd is not None:
        sentencia = SENTENCIA_RETORNAR_RANKING + f" order by puntaje desc limit 4"

    cursor = conectar_y_ejecutar(bd, sentencia)
    if cursor != None:
        return cursor

def resetear_juego(bd):
    conectar_y_ejecutar(bd, SENTENCIA_RESETEO)


