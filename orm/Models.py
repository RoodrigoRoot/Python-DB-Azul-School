#Models. Son clases que sirven para representar a las tablas que vamos a crea/tener en nuestra BD
from sqlalchemy import Column, Integer, String, SmallInteger  # Importamos tipos de datos
from start import Base

class Pets(Base):

    __tablename__ = "Pets"

    id = Column(Integer, primary_key=True)  # Definimos la llave primaria y el tipo de dato
    name = Column(String)
    age = Column(Integer)


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "ID:{}\nMascota: {}\nEdad de: {} año(s)".format(self.id, self.name, self.age)


