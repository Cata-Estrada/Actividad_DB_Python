import sqlite3

# 1. Conexión a la base de datos 
# Crea la base de datos y llamala "colegio.db"

cursor = conn.cursor()

# 2. Crear tablas (relación 1:N -> Un curso tiene muchos estudiantes)
cursor.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
""")
# Completa la creación de la tabla estudiantes
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER ------- KEY AUTOINCREMENT,
    ------ TEXT NOT NULL,
    edad -------,
    curso_id INTEGER,
    -------- KEY (curso_id) REFERENCES cursos(id)
)
""")

# 3. Funciones CRUD

#CREAR
def crear_curso(nombre):
    cursor.execute("INSERT INTO cursos (nombre) VALUES (?)", (nombre,))
    conn.commit()

def crear_estudiante(nombre, edad, curso_id):
    # Completa la consulta SQL donde estan las "----"
    cursor.execute("---------------------",(nombre, edad, curso_id))
    conn.commit()

#LEER
def ver_estudiantes():
    cursor.execute("""
    SELECT estudiantes.id, estudiantes.nombre, estudiantes.edad, cursos.nombre
    FROM estudiantes
    JOIN cursos ON estudiantes.curso_id = cursos.id
    """)
    for fila in cursor.fetchall():
        print(fila)

        
#ACTUALIZAR
def actualizar_estudiante(id_estudiante, nueva_edad):
    # Completa la consulta SQL que hace falta en las "----"
    cursor.execute("------ estudiantes SET edad = ? WHERE id = ?", (nueva_edad, id_estudiante))
    conn.commit()

#ELIMINAR
def eliminar_estudiante(id_estudiante):
    # Completa la consulta SQL que hace falta en las "----"
    cursor.execute("------ FROM ----------- WHERE -- = ?", (id_estudiante,))
    conn.commit()

# 4. Prueba de la base de datos

    crear_curso("Matemáticas")
    crear_curso("Historia")

    # Crear dos estudiantes mas
    crear_estudiante("Ana", 20, 1)

    print("\nLista de estudiantes:")
    # añade la funcion que permite ver estudiantes

    print("\nActualizando edad de Ana...")
    #añade la funcion que permite actualizar estudiantes

    ver_estudiantes()

    print("\nEliminando estudiante con ID 2...")
    #añade la funcion que permite eliminar estudiantes

    ver_estudiantes()

    # Cerrar conexión
    conn.close()
