from utils import manage_options, find_album, find_track, find_user, find_playlist
import webbrowser

class Interaction_Management_Module:
    def __init__(self) -> None:
        pass

    def profile_interaction(self, user, active_user, albums, users, playlists):
        """
        Función para la interacción con perfiles,
        permite llamar a la función para escuchar música desde un perfil,
        permite darle like a cualquier perfil
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - playlists: Playlist[]
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        while True:
            if user.kind == "musician":    
                print("\n¿Qué deseas hacer?")
                options = ["Esuchar Música", "Dar like al perfil", "Regresar"]
                option = manage_options(options)
                if option == 1:
                    self.listen_music_profile(user, active_user)
                    print("Fin de la reproducción")
                elif option == 2:
                    if active_user.kind == "listener":
                        if user.id not in active_user.likes["artists"]:
                            user.likes += 1
                            active_user.likes["artists"].append(user.id)
                            print("¡Se ha guardado tu like!")
                        else:
                            print("\nYa has dado like a este artista. ¿Deseas eliminarlo?")
                            options = ["Si", "No"]
                            option = manage_options(options)
                            if option == 1:
                                user.likes -= 1
                                active_user.likes["artists"].remove(user.id)
                    else:
                        print("No puedes dar like como artista")
                else:
                    break
            else:
                print("\n¿Qué deseas hacer?")
                options = ["Ver playlists", "Ver likes", "Regresar"]
                option = manage_options(options)
                if option == 1:
                    results = []
                    for p in user.playlists:
                        print(p.show(users, albums))
                        results.append(p.name)
                    print("¿A qué playlist deseas acceder?")
                    access = manage_options(results)
                    
                    for p in user.playlists:
                        if p.name == results[access-1]:
                            print(p.show(users, albums))
                            self.playlist_interaction(p, active_user, users, albums)
                    
                elif option == 2:
                    print("Albums likeados: ")
                    for l in user.likes["albums"]:
                        if find_album(l, albums).active == True:
                            print(f"""
    {find_album(l, albums).name}""")
                    print("Artistas likeados: ")
                    for l in user.likes["artists"]:
                        if find_user(l, users).active == True:
                            print(f"""
    {find_user(l, users).name}""")
                    print("Canciones likeadas: ")
                    for l in user.likes["songs"]:
                        if find_album(l, albums).active == True:
                            print(f"""
    {find_album(l, albums).name}""")
                    print("PLaylists likeadas: ")
                    for l in user.likes["playlists"]:
                        if find_playlist(l, playlists).active == True:
                            print(f"""
    {find_playlist(l, playlists).name}""")
                else:
                    break
    

    def playlist_interaction(self, p, active_user, users, albums):
        """
        Función para la interacción con playlists,
        permite llamar a la funcion para esuchar una playlist,
        permite darle like a la playlist
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - p: Playlist
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        while True:    
            print("\n¿Qué deseas hacer?")
            options = ["Escuchar la Lista de Reproducción", "Dar like", "Regresar"]
            option = manage_options(options)
            if option == 1:
                self.listen_music_playlist(p, active_user, users, albums)
                print("Fin de la reproducción")
            elif option == 2:
                if active_user.kind == "listener":
                    if p.id not in active_user.likes["playlists"]:
                        p.likes += 1
                        active_user.likes["playlists"].append(p.id)
                        print("¡Se ha guardado tu like!")
                    else:
                        print("\nYa has dado like a esta lista de reproducción. ¿Deseas eliminarlo?")
                        options = ["Si", "No"]
                        option = manage_options(options)
                        if option == 1:
                            p.likes -= 1
                            active_user.likes["playlists"].remove(p.id)
                else:
                    print("No puedes dar like como artista")
            else:
                break
        
    def song_interaction(self, song, active_user, users, albums):
        """
        Función para la interacción con canciones,
        permite llamar a la funcion para esuchar una canción,
        permite darle like a la canción
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - song: Song
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        while True:    
            print("\n¿Qué deseas hacer?")
            options = ["Escuchar la Canción", "Dar like", "Regresar"]
            option = manage_options(options)
            if option == 1:
                self.listen_music_song(song, active_user, users, albums)
                print("Fin de la reproducción")
            elif option == 2:
                if active_user.kind == "listener":
                    if song.id not in active_user.likes["songs"]:
                        song.likes += 1
                        active_user.likes["songs"].append(song.id)
                        print("¡Se ha guardado tu like!")
                    else:
                        print("\nYa has dado like a esta canción. ¿Deseas eliminarlo?")
                        options = ["Si", "No"]
                        option = manage_options(options)
                        if option == 1:
                            song.likes -= 1
                            active_user.likes["songs"].remove(song.id)
                else:
                    print("No puedes dar like como artista")
            else:
                break

    def album_interaction(self, album, active_user, users):
        """
        Función para la interacción con albums,
        permite llamar a la funcion para esuchar una playlist,
        permite darle like a el album
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - album: Album
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        while True:    
            print("\n¿Qué deseas hacer?")
            options = ["Escuchar Música", "Dar like", "Regresar"]
            option = manage_options(options)
            if option == 1:
                self.listen_music_album(album, active_user, users)
                print("Fin de la reproducción")
            elif option == 2:
                if active_user.kind == "listener":
                    if album.id not in active_user.likes["albums"]:
                        album.likes += 1
                        active_user.likes["albums"].append(album.id)
                        print("¡Se ha guardado tu like!")
                    else:
                        print("\nYa has dado like a este álbum. ¿Deseas eliminarlo?")
                        options = ["Si", "No"]
                        option = manage_options(options)
                        if option == 1:
                            album.likes -= 1
                            active_user.likes["albums"].remove(album.id)
                else:
                    print("No puedes dar like como artista")
            else:
                break

    def listen_music_profile(self, user, active_user):
        """
        Función para escuchar música desde un perfil,
        permite escuchar una canción en específico de los álbums creados por el artista
        Recibe:
            - user: Artist(User)
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        options = []
        for a in user.albums:
            options.append(a.name)
        options.append("Regresar")
        print("\n¿Qué album quieres escuchar?")
        option = manage_options(options)

        if option == len(options):
            return

        for a in user.albums:
            if a.name == options[option-1]:
                tracks = []
                for t in a.tracklist:
                    tracks.append(t.name)
                tracks.append("Regresar")
                print("\n¿Qué canción quieres escuchar?")
                track = manage_options(tracks)

                for t in a.tracklist:
                    if t.name == tracks[track-1]:
                        try:
                            webbrowser.open(t.link, new=1)
                        except:
                            print("Ocurrió un error al intentar reproducir la canción.")
                        t.streams += 1
                        a.streams += 1
                        user.streams += 1
                        if active_user.kind == "listener":
                            active_user.streams += 1
                        break
                    
                break
        

    def listen_music_playlist(self, playlist, active_user, users, albums):
        """
        Función para escuchar una playlist,
        permite escuchar toda una playlist,
        permite escuchar una canción específica de la playlist
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - playlist: Playlist
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        options = ["Esuchar Lista de Reproducción Completa", "Escuchar una Canción", "Regresar"]
        print("\n¿Qué deseas hacer?")
        option = manage_options(options)

        if option == 1:
            for t in playlist.tracks:
                try:
                    webbrowser.open(find_track(t, albums).link, new=1)
                except:
                    print("Ocurrió un error al intentar reproducir la playlist.")
                find_track(t, albums).streams += 1
                playlist.streams +=1
                if active_user.kind == "listener":
                    active_user.streams += 1
                for a in albums:
                    if t in a.tracklist:
                        a.streams += 1
                        find_user(a.artist, users).streams += 1
                        break
        
        elif option == 2:
            tracks = []
            for t in playlist.tracks:
                tracks.append(find_track(t, albums).name)
            print("\nIngrese la canción que desea escuchar")
            track = manage_options(tracks)
            for t in playlist.tracks:
                if find_track(t, albums).name == tracks[track-1]:
                    try:
                        webbrowser.open(find_track(t, albums).link, new=1)
                    except:
                        print("Ocurrió un error al intentar reproducir la canción.")
                    find_track(t, albums).streams += 1
                    playlist.streams += 1
                    if active_user.kind == "listener":
                        active_user.streams += 1
                    for a in albums:
                        if t in a.tracklist:
                            a.streams += 1
                            find_user(a.artist, users).streams += 1
                            break
                    break

    def listen_music_song(self, song, active_user, users, albums):
        """
        Función para escuchar una canción
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - albums: Album[]
            - song: Song
            - active_user: Obk  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        song.streams += 1
        if active_user.kind == "listener":
            active_user.streams += 1
        for a in albums:
            if song in a.tracklist:
                try:
                    webbrowser.open(song.link, new=1)
                except:
                    print("Ocurrió un error al intentar reproducir la canción.")
                a.streams += 1
                find_user(a.artist, users).streams += 1
                break

    def listen_music_album(self, album, active_user, users):
        """
        Función para escuchar un album,
        permite escuchar todo un album,
        permite escuchar una canción específica del album
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
            - album: Album
            - active_user: Obj  ==> Obj siendo objeto Artist o Listener
        Retorna: void
        """
        options = ["Escuchar Album Completo", "Escuchar una Canción", "Regresar"]
        print("\n¿Qué deseas hacer?")
        option = manage_options(options)

        if option == 1:
            for t in album.tracklist:
                try:
                    webbrowser.open(t.link, new=1)
                except:
                    print("Ocurrió un error al intentar reproducir el álbum.")
                t.streams += 1
                if active_user.kind == "listener":
                    active_user.streams += 1
                album.streams += 1
                find_user(album.artist, users).streams += 1

        elif option == 2:
            tracks = []
            for t in album.tracklist:
                tracks.append(t.name)
            print("\nIngrese la canción que desea escuchar")
            track = manage_options(tracks)
            for t in album.tracklist:
                if t.name == tracks[track-1]:
                    try:
                        webbrowser.open(t.link, new=1)
                    except:
                        print("Ocurrió un error al intentar reproducir la canción.")
                    t.streams += 1
                    if active_user.kind == "listener":
                        active_user.streams += 1
                    album.streams += 1
                    find_user(album.artist, users).streams += 1
                    break