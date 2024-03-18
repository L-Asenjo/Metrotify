from utils import find_user

class Album:
    def __init__(self, name, description, cover, date, genre, artist, tracklist, id):
        self.name = name
        self.description = description
        self.cover = cover
        self.date = date
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist
        self.id = id
        self.active = True
        self.likes = 0
        self.streams = 0

    def show_tracks(self):
        msj = ""
        for track in self.tracklist:
            if track.active == True:
                msj += track.show()
        return msj

    def show(self, users):
        return f"""
            Nombre: {self.name}
            Descripción: {self.description}
            Cubierta: {self.cover}
            Fecha de Lanzamiento: {self.date}
            Género Predominante: {self.genre}
            Artista Autor: {find_user(self.artist, users).name}
            Likes: {self.likes}
            Reproducciones: {self.streams}
            Tracklist: {self.show_tracks()}"""