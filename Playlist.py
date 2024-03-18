from utils import find_user, find_track

class Playlist:
    def __init__(self, name, description, creator, tracks, id):
        self.name = name
        self.description = description
        self.creator = creator
        self.tracks = tracks
        self.id = id
        self.active = True
        self.likes = 0
        self.streams = 0

    def show_list(self, albums):
        msj = ""

        for i in range(len(self.tracks)):
            if find_track(self.tracks[i], albums).active == True:
                aux = find_track(self.tracks[i], albums)
                msj += aux.show()
        return msj

    def show(self, users, albums):
        return f"""
        Nombre: {self.name}
        Descripción: {self.description}
        Creador: {find_user(self.creator, users).name}
        Likes: {self.likes}
        Reproducciones: {self.streams}
        Lista de Canciones: {self.show_list(albums)}"""