import uuid
from utils import manage_options, email_exists, possible_item, valid_email, username_exists, id_exists, user_exists
from Listener import Listener
from Artist import Artist

class Profile_Management_Module:
    def __init__(self, interaction_management_module) -> None:
        self.interaction_management_module = interaction_management_module

    def register_new_user(self, users):
        """
        Función de registro de usuarios nuevos
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
        Retorna: void
        """
        name = input("Ingrese su nombre (o Nombre Artístico): ")
        
        email = input("Ingrese su correo electrónico: ")
        while email_exists(email, users) or not valid_email(email):
            email = input("Ingreso inválido, ingrese su correo electrónico: ")
        
        kind = input("Ingrese el tipo de usuario, Escucha (1) o Artista (2): ")
        while not kind.isnumeric() or int(kind) not in range(1,3):
            kind = input("Ingreso inválido, ingrese el tipo de usuario, Escucha (1) o Artista (2): ")
        kind = int(kind)

        if kind == 1:
            kind = "listener"
        else:
            kind = "musician"
        
        username = input("Ingrese su nombre de usuario (Máximo 17 caracteres): ")
        while username_exists(username, users) or len(username) not in range(0, 17):
            username = input("Ingreso inválido, ingrese su nombre de usuario: ")
        
        id = uuid.uuid4()
        
        while id_exists(id, users):
            id = uuid.uuid4()
        
        if kind == "listener":
            new_user = Listener(name, username, email, kind, id)
        else:
            new_user = Artist(name, username, email, kind, id)

        users.append(new_user)
        print("Usuario Registrado Exitosamente!\n")
        
    def search_user(self, users, active_user, albums, playlists):
        """
        Función de búsqueda de usuarios por nombre, permite acceder a la interacción con un perfil de usuario 
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            = active_user: Obj  ==> Obj siendo objeto Artist o Listener
            - albums: Album[]
            - playlists: Playlist[]
        Retorna: void
        """
        while True:
            user = input("Ingrese el nombre del usuario: ")
            
            if user_exists(user, users):
                results = possible_item(user, users)         
                access = manage_options(results)

                for u in users:
                    aux = f"{u.name} ({u.username})"
        
                    if aux == results[access-1]:
        
                        if u.kind == "musician":
                            print(u.show(users))
        
                        else:
                            print(u.show())

                        self.interaction_management_module.profile_interaction(u, active_user, albums, users, playlists)
                        break
                                         
            else:
                print("Usuario no encontrado")
            
            print(f"Deseas realizar otra búsqueda?")
            options = ["Si", "No"]                                    
            option = manage_options(options)
            if option == 2:
                break

    def change_user_data(self, users, active_user):
        """
        Función de cambio de información personal
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna:
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        """
        while True:
            options = ["Nombre", "Nombre de Usuario (username)", "Correo Electrónico (Email)", "Salir"]
            option = manage_options(options)
            
            if option == 1:
                name = input("Ingrese el nuevo nombre: ")
                active_user.name = name
                return active_user
            
            elif option == 2:
                username = input("Ingrese el nuevo nombre de usuario: ")
                while username_exists(username, users) or len(username) not in range(0, 17):
                    username = input("Ingreso inválido, ingrese su nombre de usuario: ")
                active_user.username = username
                return active_user
            
            elif option == 3:
                email = input("Ingrese el nuevo correo electrónico: ")
                while email_exists(email, users) or not valid_email(email):
                    email = input("Ingreso inválido, ingrese el nuevo correo electrónico: ")
                active_user.email = email
                return active_user
            
            else:
                break

        

    def delete_user(self, users, active_user):
        """
        Función de eliminación de usuario, se usa la eliminación lógica en este caso
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna:
            - users: Obj[]   ==> Obj siendo objetos Artist y Listener
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        """
        while True:
            username = input("Ingrese el nombre de usuario (username) del usuario que desea eliminar: ")
            if username_exists(username, users):
                for u in users:
                    if u.username == username:
                        print(f"Seguro que desea eliminar este usuario? {u.username}")
                        options = ["Si", "No"]
                        option = manage_options(options)
                        if option == 1:
                            if active_user == u:
                                print("No puedes eliminar el usuario activo! Deseas cambiar el usuario activo?")
                                option_a = manage_options(options)
                                if option_a == 1:
                                    active_user = self.change_user(users)
                                    continue
                                else:
                                    break
                            else:
                                u.active = False
                                if u.kind == "musician":
                                    for a in u.albums:
                                        a.active = False
                                        for t in a.tracklist:
                                            t.active = False
                                else:
                                    for p in u.playlists:
                                        p.active = False
                                return users, active_user
                        else:
                            break                               
            else:
                username = input("Usuario no existente, ingrese el nombre de usuario (username) del usuario que desea eliminar: ")

    def change_user(self, users):
        """
        Función de cambio de usuario, 
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
        Retorna:
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        """
        username = input("Ingrese el nombre de usuario (username) del usuario con el que quiere acceder al programa: ")
        while True:
            if username_exists(username, users):
                for u in users:
                    if u.username == username:
                        active_user = u
                        return active_user
            else:
                username = input("Usuario no existente, ingrese el nombre de usuario (username) del usuario con el que quiere acceder al programa: ")
        
            