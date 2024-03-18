
class User:
    def __init__(self, name, username, email, kind, id):
        self.name = name
        self.username = username
        self.email = email
        self.kind = kind
        self.id = id

    def show(self):
        return f"""
        Nombre: {self.name}
        Usuario: {self.username}
        Correo: {self.email}"""