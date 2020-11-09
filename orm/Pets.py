from Models import Pets
from start import session


class PetsMethods:

    def get_id_pet(function):
        def wrapper(cls):
            id_pet = int(input("Ingrese el id de la mascota: "))
            return function(cls, id_pet)
        return wrapper


    @classmethod
    def create_pet(cls):
        try:
            name = input("Ingrese el nombre de la mascota: ")
            age = int(input("Ingrese la edad de la mascota: "))
            pet = Pets(name, age)
            session.add(pet)
            session.commit()
            print("Mascota agregada")   
        except Exception as e:
            print(e)
            print("La Mascota no puede ser agregada") 
        
    @classmethod
    def show_all_pets(cls):
        pets = session.query(Pets).all()
        print("-------Mascotas Registradas---------")
        for pet in pets:
            print(pet)
            print("-------------------------")

    @classmethod
    @get_id_pet
    def show_pet(cls, id_pet):
        pet = session.query(Pets).get(id_pet)
        print(pet)
    

    @classmethod
    @get_id_pet
    def delete_pet(cls, id_pet):
        pet = session.query(Pets).get(id_pet)
        print(pet)
        session.delete(pet)
        session.commit()
        print("Mascota eliminada")

    
    @classmethod
    @get_id_pet
    def update_pet(cls, id_pet):
        pet = session.query(Pets).get(id_pet)
        pet.name = input("Ingrese el nombre de la mascota: ")
        pet.age = int(input("Ingrese la edad de la mascota: "))
        session.commit()
        print("Mascota Actualizada")


    @classmethod
    def filter_name_pet(cls):
        name = input("Ingrese el nombre de la mascota: ")
        pets = session.query(Pets).filter(Pets.name==name)
        for pet in pets:
            print(pet)

    @classmethod
    def filter_first_name_pet(cls):
        name = input("Ingrese el nombre de la mascota: ")
        pets = session.query(Pets).filter(Pets.name==name).first()
        print(pets)
    
    @classmethod
    def filter_age_pet(cls):
        age = int(input("Ingrese la edad de las mascotas: "))#3
        pets = session.query(Pets).filter(Pets.age>=age).first()
        for pet in pets:
            print(pet)

#PetsMethods.create_pet()
PetsMethods.show_all_pets() #Aquí me mostrará todas las mascotas
#PetsMethods.delete_pet() # Aquí voy a eliminar una mascota
PetsMethods.update_pet()
PetsMethods.show_all_pets() #Me volverá a mostrar todas las mascotas
#PetsMethods.show_pet()
#PetsMethods.filter_name_pet() #este me devuelve todos los registros que coincidan con el nombre
#PetsMethods.filter_first_name_pet() #Este me devuelve un solo registro de los que coincidan con ese nombre
#PetsMethods.filter_age_pet()