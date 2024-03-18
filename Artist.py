from User import User

class Artist(User):
    def __init__(self, name, username, email, kind, id):
        super().__init__(name, username, email, kind, id)
        self.streams = 0
        self.likes = 0
        self.albums = []
        self.active = True

    def top10_songs(self):
        top10 = []
        tracks = []
        for a in self.albums:
            for t in a.tracklist:
                tracks.append(t)
        
        tracks = sorted(tracks, key=lambda x:x.streams, reverse=True)
        for i in range(0,10):
            top10.append(tracks[i])
        return top10
                
    def show_albums(self, users):
        msj = ""
        for album in self.albums:
            msj += album.show(users)
        return msj
    
    def show_top10(self):
        for t in self.top10_songs():
            t.show()

    def show(self, users):
        msj = super().show()
        msj += f"""
        Reproducciones Totales: {self.streams}
        Likes: {self.likes}
        Canciones más Reproducidas: {self.show_top10()}
        Albums: {self.show_albums(users)}
        """
        return msj