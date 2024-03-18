from utils import manage_options, song_exists, user_exists, possible_item, album_exists, id_exists, playlist_exists, find_track, valid_link
import uuid
from Album import Album
from Playlist import Playlist
from Song import Song
import datetime

class Music_Management_Module:
    def __init__(self, interaction_management_module) -> None:
        self.interaction_management_module = interaction_management_module
    
    def create_album(self, albums, active_user):
        """
        Función de creación de albums (exclusiva para todos los User de tipo Artist) a base de inputs
        Recibe:
            - albums: Album[]
            - active_user: Artist(User)
        Retorna:
            - albums: Album[]
            - active_user: Artist(User)
        """
        name = input("Ingrese el nombre del nuevo álbum: ")
        description = input("Ingrese la descripción del nuevo álbum: ")
        cover = input("Ingrese el link de la imagen cover del álbum: ")
        while not valid_link(cover):
            cover = input("Ingreso inválido, ingrese el link de la imagen cover del álbum: ")
        date = datetime.datetime.now()
        genre = input("Ingrese el género predominante del nuevo álbum: ")
        artist = active_user.id
        id = uuid.uuid4()
        while id_exists(id, albums):
            id = uuid.uuid4()
        tracklist = []
        while True:
            song_name = input("Ingrese el nombre de la nueva canción: ")
            song_duration = input("Ingrese la duración de la canción (formato: minutos:segundos): ")
            while True:
                time_format = '%M:%S'
                try:
                    song_duration = datetime.datetime.strptime(song_duration, time_format)
                    break
                except ValueError:
                    song_duration = input("Ingreso inválido, ingrese la duración de la canción (formato: minutos:segundos): ")
            song_id = uuid.uuid4()
            for a in albums:
                while id_exists(song_id, a.tracklist):
                    song_id = uuid.uuid4()
            song_link = input("Ingrese el enlace (link) de la nueva canción: ")
            while not valid_link(song_link):
                song_link = input("Ingreso inválido, ingrese el enlace (link) de la nueva canción: ")
            new_song = Song(song_name, song_duration, song_id, song_link)
            tracklist.append(new_song)
            print(f"Deseas crear otra canción?")
            options = ["Si", "No"]                                    
            option = manage_options(options)
            if option == 2:
                break
        new_album = Album(name, description, cover, date, genre, artist, tracklist, id)
        active_user.albums.append(new_album)
        albums.append(new_album)

        return active_user, albums


    def create_playlist(self, users, albums, playlists, active_user):
        """
        Función de creación de playlists (exclusiva para todos los User de tipo Listener)
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - playlists: Playlist[]
            - active_user: Listener(User)
        Retorna:
            - playlists: Playlist[]
            - active_user: Listener(User)
        """
        name = input("Ingrese el nombre de la nueva lista de reproducción (playlist): ")
        description = input("Ingrese la descripción de la lista de reproducción (playlist): ")
        creator = active_user.id
        id = uuid.uuid4()
        while id_exists(id, playlists):
            id = uuid.uuid4()
        tracks = []
        while True:
            options = ["Búsqueda por Canción", "Búsqueda por Artista", "Búsqueda por Álbum", "Búsqueda por Playlist"]
            option = manage_options(options)
            if option == 1:    
                track = input("Ingrese el nombre de la canción: ")
                if song_exists(track, albums):
                    aux = []
                    for a in albums:
                        for t in a.tracklist:
                            aux.append(t)
                    results = possible_item(track, aux)         
                    access = manage_options(results)

                    for a in albums:
                        for t in a.tracklist:    

                            if t.name == results[access-1]:
                                print(f"Deseas agregar esta canción a la playlist? {t.show()}")
                                options = ["Si", "No"]                                    
                                option = manage_options(options)
                                if option == 1:
                                    tracks.append(t.id)
                                break
                                         
                else:
                    print("Canción no encontrada\n")
            elif option == 2:
                user = input("Ingrese el nombre del usuario: ")
            
                if user_exists(user, users):
                    musicians = []
                    # buscar todos los musicos
                    for u in users:
                        if u.kind == "musician":
                            musicians.append(u)
                    
                    results = possible_item(user, musicians)
                    access = manage_options(results)

                    for u in musicians:
                        aux = f"{u.name} ({u.username})"

                        if aux == results[access-1]:
                            results = []
                            for a in u.albums:
                                print(a.show(users))
                                for t in a.tracklist:
                                    results.append(t)
                            while True:    
                                track = input("Ingrese el nombre de la canción: ")
                                if song_exists(track, u.albums):
                                    results = possible_item(track, results)         
                                    access = manage_options(results)

                                    for a in u.albums:
                                        for t in a.tracklist:   
                                            if t.name == results[access-1]:
                                                print(f"Deseas agregar esta canción a la playlist? {t.show()}")
                                                options = ["Si", "No"]                                    
                                                option = manage_options(options)

                                                if option == 1:
                                                    tracks.append(t.id)
                                                
                                                break
                                    break
                                else:
                                    print("Canción no encontrada\n")
                            break
                                        
                else:
                    print("Usuario no encontrado\n")
            elif option == 3:
                album = input("Ingrese el nombre del álbum: ")
                
                if album_exists(album, albums):
                    results = possible_item(album, albums)
                    access = manage_options(results)

                    for a in albums:
                        if a.name == results[access-1]:
                            print(a.show(users))
                            results = []
                            for t in a.tracklist:
                                results.append(t)

                            while True:    
                                    track = input("Ingrese el nombre de la canción: ")
                                    if song_exists(track, albums):
                                        results = possible_item(track, results)
                                        access = manage_options(results)
                                        for t in a.tracklist:   
                                            if t.name == results[access-1]:
                                                print(f"Deseas agregar esta canción a la playlist? {t.show()}")
                                                options = ["Si", "No"]                                    
                                                option = manage_options(options)
                                                
                                                if option == 1:
                                                    tracks.append(t.id)
                                        
                                                break
                                        
                                        break
                                    else:
                                        print("Canción no encontrada\n")
                            break
                else:
                    print("Album no encontrado\n")
            else:
                playlist = input("Ingrese el nombre de la lista de reproducción (playlist): ")

                if playlist_exists(playlist, playlists):
                    results = possible_item(playlist, playlists)
                    access = manage_options(results)

                    for p in playlists:
                        if p.name == results[access-1]:
                            print(p.show(users, albums))
                            results = []
                            for t in p.tracks:
                                s = find_track(t, albums)
                                results.append(s)
                            
                            while True:
                                track = input("Ingrese el nombre de la canción: ")
                                if song_exists(track, albums):
                                    results = possible_item(track, results)         
                                    access = manage_options(results)

                                    for t in p.tracks:
                                        s = find_track(t, albums)
                                        if s.name == results[access-1]:
                                            print(f"Deseas agregar esta canción a la playlist? {s.show()}")
                                            options = ["Si", "No"]                                    
                                            option = manage_options(options)
                                            
                                            if option == 1:
                                                tracks.append(s.id)
                                            
                                            break
                                    
                                    break
                                else:
                                    print("Canción no encontrada\n")
                            
                            break
                else:
                    print("Lista de Reproducción no encontrada\n")
                                                    
           
            print(f"Deseas realizar otra búsqueda?")
            options = ["Si", "No"]                                    
            option = manage_options(options)
            if option == 2:
                break
        new_playlist = Playlist(name, description, creator, tracks, id)
        playlists.append(new_playlist)
        active_user.playlists.append(new_playlist)

        return playlists, active_user
    
    def search(self, users, albums, playlists, active_user):
        """
        Función de búsqueda de usuarios, albums, playlists y canciones, permite acceder al módulo de interacción correspondiente al tipo de búsqueda
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - playlists: Playlist[]
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        while True:
            options = ["Búsqueda por Canción", "Búsqueda por Artista", "Búsqueda por Álbum", "Búsqueda por Playlist"]
            option = manage_options(options)
            if option == 1:    
                track = input("Ingrese el nombre de la canción: ")
                if song_exists(track, albums):
                    aux = []
                    for a in albums:
                        for t in a.tracklist:
                            aux.append(t)

                    results = possible_item(track, aux)
                    results.append("Regresar")         
                    access = manage_options(results)

                    for a in albums:
                        for t in a.tracklist:    
                            if t.name == results[access-1]:
                                print(t.show())
                                self.interaction_management_module.song_interaction(t, active_user, users, albums)
                                break
                        
                else:
                    print("Canción no encontrada\n")

            elif option == 2:
                user = input("Ingrese el nombre del usuario: ")
            
                if user_exists(user, users):
                    for u in users:
                        results = possible_item(user, users)
                        results.append("Regresar")        
                        access = manage_options(results)

                        if access == len(results):
                            break

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
                    print("Usuario no encontrado\n")

            elif option == 3:
                album = input("Ingrese el nombre del álbum: ")
                if album_exists(album, albums):
                    results = possible_item(album, albums)
                    results.append("Regresar")
                    access = manage_options(results)

                    for a in albums:
                        if a.name == results[access-1]:
                            print(a.show(users))
                            self.interaction_management_module.album_interaction(a, active_user, users)
                            break
                            
                else:
                    print("Album no encontrado\n")

            else:
                playlist = input("Ingrese el nombre de la lista de reproducción (playlist): ")

                if playlist_exists(playlist, playlists):
                    results = possible_item(playlist, playlists)
                    results.append("Regresar")
                    access = manage_options(results)

                    for p in playlists:
                        if p.name == results[access-1]:
                            print(p.show(users, albums))
                            self.interaction_management_module.playlist_interaction(p, active_user, users, albums)
                            break
                else:
                    print("Lista de Reproducción no encontrada\n")
                                                    
           
            print(f"Deseas realizar otra búsqueda?")
            options = ["Si", "No"]                                    
            option = manage_options(options)
            if option == 2:
                break
    