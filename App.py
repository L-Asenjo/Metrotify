from utils import manage_options, save_data, open_data, api
import pickle
from Profile_Management_Module import Profile_Management_Module
from Music_Management_Module import Music_Management_Module
from Statistics_Module import Statistics_Module
from Interaction_Management_Module import Interaction_Management_Module
from Artist import Artist
from Listener import Listener
from Playlist import Playlist
from Album import Album
from Song import Song

class App:
    def __init__(self):
        # edd
        self.users = []
        self.albums = []
        self.playlists = []
        self.users_obj = []
        self.albums_obj = []
        self.playlists_obj = []
        # modules
        self.interaction_management_module = Interaction_Management_Module()
        self.profile_management_module = Profile_Management_Module(self.interaction_management_module)
        self.music_management_module = Music_Management_Module(self.interaction_management_module)
        self.statistics_module = Statistics_Module()

    def save_data(self):
        """
        Función para guardar los datos usando pickle
        Recibe: N/A
        Retorna: void
        """
        save_data('users.txt', self.users_obj)
        save_data('albums.txt', self.albums_obj)
        save_data('playlists.txt', self.playlists_obj)

    def open_data(self):
        """
        Función para cargar los datos usando pickle
        Recibe: N/A
        Retorna: void
        """
        self.users_obj = open_data('users.txt', self.users_obj)
        self.albums_obj = open_data('albums.txt', self.albums_obj)
        self.playlists_obj = open_data('playlists.txt', self.playlists_obj)

    def register(self, users, albums, playlists):
        """
        Función para la creación de objetos con base en las listas de diccionarios obtenidas desde la api
        Recibe:
            - users: dict[]
            - albums: dict[]
            - playlists: dict[]
        Retorna: void
        """
        for u in users:
            name = u["name"]
            id = u["id"]
            email = u["email"]
            username = u["username"]
            type = u["type"]
            if type == "musician":
                new_user = Artist(name, username, email, type, id)
                self.users_obj.append(new_user)
            else:
                new_user = Listener(name, username, email, type, id)
                self.users_obj.append(new_user)
        
        for a in albums:
            name = a["name"]
            description = a["description"]
            cover = a["cover"]
            date = a["published"]
            genre = a["genre"]
            id = a["id"]
            artist = a["artist"]
            tracklist = []
            for s in a["tracklist"]:
                s_name = s["name"]
                duration = s["duration"]
                link = s["link"]
                id = s["id"]
                new_song = Song(s_name, duration, link, id)
                tracklist.append(new_song)
            new_album = Album(name, description, cover, date, genre, artist, tracklist, id)
            self.albums_obj.append(new_album)
        
        for p in playlists:
            name = p["name"]
            description = p["description"]
            creator = p["creator"]
            id = p["id"]
            tracks = p["tracks"]
            new_playlist = Playlist(name, description, creator, tracks, id)
            self.playlists_obj.append(new_playlist)

    def assign_items(self, users, albums, playlists):
        """
        Función para asignarle a un usuario los albums o playlists correspondientes según el tipo de usuario (albums => Artist, playlists => Listener)
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - playlists: Playlist[]
        Retorna: void
            """
        for u in users:
            if u.kind == "musician":
                for a in albums:
                    if a.artist == u.id:
                        u.albums.append(a)
            else:
                for p in playlists:
                    if p.creator == u.id:
                        u.playlists.append(p)

    def profile_management(self):
        """
        Función de menú para acceder al módulo de gestión de usuarios
        Recibe: N/A
        Retorna: void
        """
        while True:
            print(f"""
                                *****MODULO DE GESTION DE USUARIOS*****
                  """)
            options = ["Registrar Usuario", "Buscar Usuario", "Cambiar Información Personal", "Borrar Datos de la Cuenta", "Cambiar Usuario Activo", "Salir"]
            option = manage_options(options)
            print('')
            if option == 1:
                self.profile_management_module.register_new_user(self.users_obj)
            elif option == 2:
                self.profile_management_module.search_user(self.users_obj, self.active_user, self.albums_obj, self.playlists_obj)
            elif option == 3:
                self.active_user = self.profile_management_module.change_user_data(self.users_obj, self.active_user)
            elif option == 4:
                self.users_obj, self.active_user = self.profile_management_module.delete_user(self.users_obj, self.active_user)
            elif option == 5:
                self.active_user = self.profile_management_module.change_user(self.users_obj)
            else:
                break

    def music_management(self):
        """
        Función de menú para acceder al módulo de gestión musical
        Recibe: N/A
        Retorna: void
        """
        while True:
            print(f"""
                                *****MODULO DE GESTION MUSICAL*****
                  """)
            options = ["Crear", "Escuchar Música", "Salir"]
            option = manage_options(options)
            print('')
            if option == 1:
                if self.active_user.kind == "listener":
                    self.playlists_obj, self.active_user = self.music_management_module.create_playlist(self.users_obj, self.albums_obj, self.playlists_obj, self.active_user)
                else:
                    self.active_user, self.albums_obj = self.music_management_module.create_album(self.albums_obj, self.active_user)
            elif option == 2:
                self.music_management_module.search(self.users_obj, self.albums_obj, self.playlists_obj, self.active_user)
            else:
                break

    def statistics(self):
        """
        Función de menú para acceder al módulo de estadísticas
        Recibe: N/A
        Retorna: void
        """
        print(f"""
                                *****MODULO DE ESTADISTICA*****
                """)
        while True:
            options = ["Artistas con más Streams", "Álbumes con más Streams", "Canciones con más Streams", "Usuarios con más Streams", "Salir"]
            print('')
            option = manage_options(options)
            print('')
            if option == 1:
                self.statistics_module.show_streamed_artists(self.users_obj)
            elif option == 2:
                self.statistics_module.show_streamed_albums(self.albums_obj)
            elif option == 3:
                self.statistics_module.show_streamed_songs(self.albums_obj)
            elif option == 4:
                self.statistics_module.show_streamed_listeners(self.users_obj)
            else:
                break

    def menu(self):
        """
        Función de menú para acceder a los módulos del programa
        Recibe: N/A
        Retorna: void
        """
        while True:
            if len(self.users_obj) == 0 or len(self.albums_obj) == 0 or len(self.playlists_obj) == 0:
                options = ["Reiniciar Base de Datos e Iniciar (SI REALIZÓ ALGUNA MODIFICACION CON EL PROGRAMA, ESTA SERA ELIMINADA)", "Iniciar con Datos Modificados"]
                option = manage_options(options)
                print('')
                if option == 1:
                    self.users = api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
                    self.albums = api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
                    self.playlists = api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
                    self.register(self.users, self.albums, self.playlists)
                    self.assign_items(self.users_obj, self.albums_obj, self.playlists_obj)
                else:
                    self.open_data()
            else:
                break

        print(f"""
                            Bienvenido a Metrotify!
                Un ambiente en el que podrás publicar o escuchar música a tu gusto
            """)
        
        self.active_user = self.profile_management_module.change_user(self.users_obj)
        while self.active_user.active == False:
            self.active_user = self.profile_management_module.change_user(self.users_obj)

        while True:
            print(f"""
                                    *****MENU PRINCIPAL*****
            """)
            options = ["Gestión de Perfil", "Gestión Musical", "Indicadores (Estadísticas)", "Salir"]
            option = manage_options(options)
            print('')
            if option == 1:
                self.profile_management()
            elif option == 2:
                self.music_management()
            elif option == 3:
                self.statistics()
            else:
                print(f"""
                            *****GRACIAS POR USAR METROTIFY*****
                                            <3
                      """)
                self.save_data()
                break
    