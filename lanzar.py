from pytube import YouTube

yt = YouTube("https://youtu.be/iE3kD4X_Fwg")

print("Titulo: ",yt.title)
print("Numero de visitas: ",yt.views)
print("Longitud del video: ",yt.length,"segundos")
print("Descripción: ",yt.description)
print("Valoraciones: ",yt.rating)