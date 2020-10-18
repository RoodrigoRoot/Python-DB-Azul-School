import psycopg2
import hashlib
import getpass

TABLE_USERS = """ CREATE TABLE users(
id serial,
name varchar(20),
age smallint,
password varchar(80)
);
"""

def get_user_from_terminal_insert():
    name = input("Ingresa tu nombre: ")
    age = input("Ingresa tu edad: ")
    age = int(age)
    password = getpass.getpass("Ingresa tu contraseña: ")
    password = hashlib.sha256(password.encode()).hexdigest()#Cifrado de password

    return name, age, password
    

def get_user_from_terminal_update():
    id_user = input("Ingresa el id del usuario a modificar: ")
    id_user = int(id_user)
    name = input("Ingresa el nuevo nombre: ")
    age = input("Ingresa la nueva edad: ")
    age = int(age)
    password = getpass.getpass("Ingresa tu nueva contraseña: ")
    password = hashlib.sha256(password.encode()).hexdigest()#Cifrado de password

    return name, age, password, id_user


try:
    connection = psycopg2.connect("host='localhost' user='tester' password='123456' dbname='azul' ")
    print("Nos hemos conectado")
    
    #sql = "INSERT INTO users (name, age, password) VALUES('{}', {} ,'{}')".format(name, age, password)
    sql_insert = "INSERT INTO users (name, age, password) VALUES(%s, %s, %s)"
    sql_select = "SELECT * FROM users" 
    sql_update = "UPDATE users SET name=%s, age=%s, password=%s WHERE id=%s;"

    with  connection.cursor() as cursor:
        #cursor.execute(TABLE_USERS)
        #cursor.execute(sql, get_user_from_terminal())       
        #connection.commit()
        #print("Usuario Guardado")
        print("Usuarios antes de modificar alguno")
        cursor.execute(sql_select)
        for user in cursor.fetchall():
            print(user)
        cursor.execute(sql_update, get_user_from_terminal_update())
        connection.commit()
        
        print("Usuarios después de modificar alguno")
        
        cursor.execute(sql_select)
        for user in cursor.fetchall():
            print(user)

    connection.close()
except psycopg2.Error as err:
    #print("La base de datos no existe. Favor de Revisar")
    print(err)