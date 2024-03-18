import datetime
import re
import requests
import pickle
import validators
from User import User
from Song import Song

def api(endpoint):
    """
    Función para acceder a la información de la base de datos utilizando un endpoint dado.
    Recibe:
      - endpoint: str
    Retorna:
      - data: dict[]
    """

    # se hace el request a la base de datos
    response = requests.request('GET', endpoint)
    
    # se transforma la respuesta en un diccionario
    dictionary = response.json()

    # se retorna el diccionario
    return dictionary

def open_data(file, edd):
    """
     Función para cargar los datos usando pickle
     Recibe:
         - file_name: str
         - edd: []
     Retorna:
         - edd: Obj[]  ==> Obj siendo Album, Playlist o Listener y Artist
     """
    try:
        with open(file, 'rb') as f:
            edd = pickle.load(f)
        return edd
    except:
        print('error')
        if FileNotFoundError:
            print('archivo no encontrado, reinicie la base de datos e inicie') 

def save_data(file_name, edd):
    """
    Función para guardar los datos usando pickle
    Recibe: N/A
    Retorna: void
    """
    with open(file_name, 'wb') as f:
            pickle.dump(edd, f)

def manage_options(options):
    """
    Función para mostrar, seleccionar y validar las opciones de un menú.
    Recibe:
      - options: str[]
    Retorna:
      - option: int
    """

    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    option = input("Ingrese el número de su opción: ")
    while not option.isnumeric() or int(option)-1 not in range(len(options)):
        option = input("Ingreso inválidos, ingrese el número de su opción: ")
    
    return int(option)

def valid_email(email):
    """
    Función para validar si el input dado califica bajo la estructura de un email
    Recibe:
        - email: str
    Retorna
        - valid_email: bool
    """
    # regex
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    return re.fullmatch(regex, email)

def valid_link(link):
    """
    Función para validar si el input dado califica bajo la estructura de un link
    Recibe:
        - link: str
    Retorna
        - valid_link: bool
    """    
    return validators.url(link)

def email_exists(email, users):
    """
    Función para validar si el email dado existe en la base de datos
    Recibe:
        - email: str
        - users: User[]
    Retorna:
        - email_exists: bool
        """
    return any(u.email == email for u in users)

def username_exists(username, users):
    """
    Función para validar si el username dado existe en la base de datos
    Recibe:
        - username: str
        - users: User[]
    Retorna:
        - username_exists: bool
        """
    return any(u.username == username for u in users)

def id_exists(id, items):
    """
    Función para validar si el id creado existe en la base de datos
    Recibe:
        - id: str
        - items: Obj[] ==> Obj siendo objetos de diferentes tipos según sea necesaria la validación
    Retorna:
        - id_exists: bool
    """
    return any(i.id == id for i in items)

def user_exists(user, users):
    """
    Función para validar si el user dado existe en la base de datos
    Recibe:
        - user: str
        - users: User[]
    Retorna:
        - user_exists: bool
    """
    return any(user.lower() in u.name.lower() for u in users)

def album_exists(album, albums):
    """
    Función para validar si el album dado existe en la base de datos
    Recibe:
        - album: str
        - albums: Album[]
    Retorna:
        - album_exists: bool
    """
    return any(album.lower() in a.name.lower() for a in albums)

def playlist_exists(playlist, playlists):
    """
    Función para validar si la playlist dada existe en la base de datos
    Recibe:
        - playlist: str
        - playlists: Playlist[]
    Retorna:
        - playlist_exists: bool
    """
    return any(playlist.lower() in p.name.lower() for p in playlists)

def song_exists(song, albums):
    """
    Función para validar si la canción dada existe en la base de datos
    Recibe:
        - song: str
        - albums: Album[]
    Retorna:
        - song_exists: bool
    """
    return any(song.lower() in t.name.lower() for a in albums for t in a.tracklist )

def possible_item(item, items):
    """
    Funcón para encontrar los items posibles en la base de datos que hacen match con el input dado
    Recibe:
        - item: str
        - items: Obj[] ==> Obj siendo objetos de diferentes tipos según sea necesaria la validación
    Retorna:
        - results: str[]
    """
    results = []
    for i in items:
        if i.active == True:
            if isinstance(i, User):
                if item.lower() in i.name.lower():            
                    results.append(f"{i.name} ({i.username})")
            elif isinstance(i, Song):
                if item.lower() in i.name.lower():
                    results.append(f"{i.name}")
            else:
                if item.lower() in i.name.lower():
                    results.append(f"{i.name}")
    return results

def find_user(id, users):
    """
    Función para encontrar a un usuario por el id
    Recibe:
        - id: str
        - users: User[]
    Retorna:
        - u: User
    """
    for u in users:
        if u.id == id:
            return u
        
def find_track(id, albums):
    """
    Función para encontrar a una canción por el id
    Recibe:
        - id: str
        - albums: Album[]
    Retorna:
        - t: Song
    """
    for a in albums:
        for t in a.tracklist:
            if t.id == id:
                return t

def find_album(id, albums):
    """
    Función para encontrar a un album por el id
    Recibe:
        - id: str
        - albums: Album[]
    Retorna:
        - a: Album
    """
    for a in albums:
        if a.id == id:
            return a
        
def find_playlist(id, playlists):
    """
    Función para encontrar a una playlist por el id
    Recibe:
        - id: str
        - playlists: Playlist[]
    Retorna:
        - p: Playlist
    """
    for p in playlists:
        if p.id == id:
            return p