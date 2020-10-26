from Db import connection
from Users import UserDB, UserMethods

ADD = 1
DELETE = 2
LIST = 3
UPDATE = 4



def selected_option(con, option):
    with con.cursor() as cursor:

        if option == ADD:
            user = UserMethods.create_user()
            UserDB.insert_user(user, cursor)

        elif option == DELETE:
            UserDB.delete_user(cursor)

        elif option == LIST:
            UserDB.list_users(cursor)

        elif option == UPDATE:
            UserDB.update_user(cursor)

        con.commit()


def menu():
    menu = """1.-Agregar Usuario\n2.-Eliminar Usuario\n3.-Listar Usuario\n4.-Actualizar Usuario\n5.-Salir\nOpción: """
    con = connection()
    while True:
        print("**********Escoge una opción**********")
        option = input(menu)
        option = int(option)
        if option == 5:
            print("\nVuelva pronto\n")
            break
        selected_option(con, option)

menu()