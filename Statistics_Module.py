from utils import manage_options
import matplotlib.pyplot as plt

class Statistics_Module:
    def __init__(self) -> None:
        pass

    def show_streamed_artists(self, users):
        """
        Función para ver el top 5 de artistas más reproducidos,
        permite ver la información escrita o ver una gráfica de ella
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Artist y Listener
        Retorna: void
        """
        options = ["Ver Top 5 Artistas más reproducidos", "Ver Gráfica", "Regresar"]
        option = manage_options(options)

        top5 = []
        aux = []
        for u in users:
            if u.kind == "musician" and u.active == True:
                aux.append(u)
        aux = sorted(aux, key=lambda x:x.streams, reverse=True)
        
        for i in range(0, 5):
            top5.append(aux[i])

        if option == 1:
            for i in range(len(top5)):
                print(f"""          *****TOP 5 ARTISTAS CON MAS REPRODUCCIONES*****""")
                print(f"TOP {i+1}. {top5[i].name} (Streams: {top5[i].streams})")
        elif option == 2:
            names = []
            values = []
            for u in top5:
                names.append(u.name)
                values.append(u.streams)
            plt.bar(names, values)
            plt.xlabel("Top 5 Artistas")
            plt.ylabel("Reproducciones")
            plt.show()
        else:
            return

    def show_streamed_albums(self, albums):
        """
        Función para ver el top 5 de albums más reproducidos,
        permite ver la información escrita o ver una gráfica de ella
        Recibe:
            - albums: Album[]
        Retorna: void
        """
        options = ["Ver Top 5 Albums más reproducidos", "Ver Gráfica", "Regresar"]
        option = manage_options(options)

        top5 = []
        aux = []
        for a in albums:
            if a.active == True:
                aux.append(a)
        aux = sorted(albums, key=lambda x:x.streams, reverse=True)
        
        for i in range(0, 5):
            top5.append(aux[i])
            
        if option == 1:
            for i in range(len(top5)):
                print(f"""          *****TOP 5 ALBUMS CON MAS REPRODUCCIONES*****""")
                print(f"TOP {i+1}. {top5[i].name} (Streams: {top5[i].streams})")
        elif option == 2:
            names = []
            values = []
            for a in top5:
                names.append(a.name)
                values.append(a.streams)
            plt.bar(names, values)
            plt.xlabel("Top 5 Albums")
            plt.ylabel("Reproducciones")
            plt.show()
        else:
            return
        
    def show_streamed_songs(self, albums):
        """
        Función para ver el top 5 de canciones más reproducidas,
        permite ver la información escrita o ver una gráfica de ella
        Recibe:
            - albums: Album[]
        Retorna: void
        """
        options = ["Ver Top 5 Canciones más reproducidos", "Ver Gráfica", "Regresar"]
        option = manage_options(options)

        top5 = []
        aux = []
        for a in albums:
            if a.active == True:
                for t in a.tracklist:
                    aux.append(t)
        aux = sorted(aux, key=lambda x:x.streams, reverse=True)
        for i in range(0, 5):
            top5.append(aux[i])

        if option == 1:
            print(f"""          *****TOP 5 CANCIONES CON MAS REPRODUCCIONES*****""")
            for i in range(len(top5)):
                print(f"TOP {i+1}. {top5[i].name} (Streams: {top5[i].streams})")
        elif option == 2:
            names = []
            values = []
            for s in top5:
                names.append(s.name)
                values.append(s.streams)
            plt.bar(names, values)
            plt.xlabel("Top 5 Canciones")
            plt.ylabel("Reproducciones")
            plt.show()
        else:
            return
        
    def show_streamed_listeners(self, users):
        """
        Función para ver el top 5 de esucuchas con más items reproducidos,
        permite ver la información escrita o ver una gráfica de ella
        Recibe:
            - users: Obj[]  ==> Obj siendo objetos Arist y Listener
        Retorna: void
        """
        options = ["Ver Top 5 Escuchas que han hecho más reproducciones", "Ver Gráfica", "Regresar"]
        option = manage_options(options)

        top5 = []
        aux = []
        for u in users:
            if u.kind == "listener" and u.active == True:
                aux.append(u)
        aux = sorted(aux, key=lambda x:x.streams, reverse=True)

        for i in range(0, 5):
            top5.append(aux[i])
            
        if option == 1:
            print(f"""      *****TOP 5 ESCUCHAS QUE HAN HECHO MAS REPRODUCCIONES*****""")        
            for i in range(len(top5)):
                print(f"TOP {i+1}. {top5[i].name} (Streams: {top5[i].streams})")
        elif option == 2:
            names = []
            values = []
            for u in top5:
                names.append(u.name)
                values.append(u.streams)
            plt.bar(names, values)
            plt.xlabel("Top 5 Escuchas")
            plt.ylabel("Reproducciones")
            plt.show()
        else:
            return