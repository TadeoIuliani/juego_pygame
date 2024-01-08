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
    

def agregar_regristro(bd, nivel, usuario, puntaje):
    if nivel == 1:
        sentencia = f"""insert into nivel_1(nombre, puntaje) values('{usuario}', {puntaje}) """
    elif nivel == 2:
        sentencia = f"""insert into nivel_2(nombre, puntaje) values('{usuario}', {puntaje}) """
    elif nivel == 3:
        sentencia = f"""insert into nivel_3(nombre, puntaje) values('{usuario}', {puntaje}) """
    conectar_y_ejecutar(bd, sentencia)


def conectar_y_ejecutar(path, sentencia):
    if sentencia != None:
        retorno = []
        conexion = sqlite3.connect(path)
        respuesta = conexion.execute(sentencia)
        for fila in respuesta:
            retorno.append(fila)
        conexion.commit()
        conexion.close()
        
        return retorno

def traer_ranking(bd, nivel):
    retorno = []
    if nivel == 1:
        sentencia = f"""SELECT * from nivel_1 order by puntaje desc limit 4"""
    elif nivel == 2:
        sentencia = f"""SELECT * from nivel_2 order by puntaje desc limit 4"""
    elif nivel == 3:
        sentencia = f"""SELECT * from nivel_3 order by puntaje desc limit 4"""
    cursor = conectar_y_ejecutar(bd, sentencia)
    if cursor != None:
        return cursor

# ret = traer_ranking("ranking.db", 1)
# for fila in ret:
#     print(fila)