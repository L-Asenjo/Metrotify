from User import User
from Playlist import Playlist
from Song import Song
from Album import Album

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
            elif isinstance(i, Playlist):
                if item.lower() in i.name.lower():
                    results.append(f"{i.name}")
            elif isinstance(i, Album):
                if item.lower() in i.name.lower():
                    results.append(f"{i.name}")        
    return results