

class Song:
    def __init__(self, name, duration, link, id):
        self.name = name
        self.duration = duration
        self.link = link
        self.id = id
        self.active = True
        self.streams = 0
        self.likes = 0
    
    def show(self):
        return f"""
                Nombre: {self.name}
                Duración: {self.duration}
                Likes: {self.likes}
                Link: {self.link}
                Reproducciones: {self.streams}
                """
