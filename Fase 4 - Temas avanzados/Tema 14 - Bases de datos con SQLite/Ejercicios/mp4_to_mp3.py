import os
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

def convertir_y_mostrar_tamaño():
    archivo_mp4 = filedialog.askopenfilename(title="Seleccionar archivo MP4",
                                              filetypes=[("Archivos MP4", "*.mp4")])
    if archivo_mp4:
        # Obtener la ruta del directorio del archivo de video
        directorio_video = os.path.dirname(archivo_mp4)
        
        video = mp.VideoFileClip(archivo_mp4)
        audio = video.audio
        # Combinar la ruta del directorio con el nombre del archivo MP3
        archivo_mp3 = os.path.join(directorio_video, "new_audio.mp3")
        audio.write_audiofile(archivo_mp3)
        audio.close()
        video.close()

        tamaño_bytes = os.path.getsize(archivo_mp3)
        tamaño_kb = tamaño_bytes / 1024  # bytes a kilobytes
        tamaño_mb = tamaño_kb / 1024  # kilobytes a megabytes

        resultado_label.config(text=f"Tamaño del archivo MP3: {tamaño_mb:.2f} MB")

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de MP4 a MP3")

# Crear un botón para seleccionar el archivo MP4 y convertirlo
convertir_button = tk.Button(root, text="Seleccionar archivo MP4 y convertir",
                              command=convertir_y_mostrar_tamaño)
convertir_button.pack(pady=20)

# Crear una etiqueta para mostrar el tamaño del archivo MP3 resultante
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()

