from User import User

class Listener(User):
    def __init__(self, name, username, email, kind, id):
        super().__init__(name, username, email, kind, id)
        self.likes = {"albums": [], "artists": [], "songs": [], "playlists": []}
        self.streams = 0
        self.playlists = []
        self.active = True
    
    def show_playlists(self):
        msj = ""
        for playlist in self.playlists:
            msj += playlist.show()
        return msj

    def show(self):
        msj = super().show()
        msj += f"""
        Playlists Creadas: {len(self.playlists)}
        Likes: {len(self.likes["albums"]) + len(self.likes["artists"]) + len(self.likes["songs"]) + len(self.likes["playlists"])}
        Streams: {self.streams}
        """
        return msj