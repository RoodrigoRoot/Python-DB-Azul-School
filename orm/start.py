#Crear Engine
#El Engine, me va a permitir conectarme a la base de datos.
#Tambien se va a encargar del dialecto a utilizar.
#Dialecto
#Son las variaciones que agrega cada motor de base de datos

#Session, me permite el poder realizar operaciones(transacciones) a nuestra base de datos
#Dichas operaciones son de manera atomica(Todo o Nada)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://tester:123456@localhost/azul')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()  # Nos permite hacer el mapeo de nuestras clases