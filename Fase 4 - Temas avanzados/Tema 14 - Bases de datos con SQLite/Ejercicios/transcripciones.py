import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import whisper
import os

def transcribe_audio(audio_file):
    with open(audio_file, "rb") as audio_file:
        audio_data = audio_file.read()
    
    try:
        text = whisper.transcribe(audio_data, language="es-ES") # Cambia el idioma según sea necesario
        return text
    except Exception as e:
        return f"No se pudo obtener la transcripción; {e}"

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.wav;*.mp3;*.ogg;*.flac;*.m4a;*.mp4")])
    if filepath:
        if os.path.exists(filepath) and os.path.isfile(filepath):
            transcription = transcribe_audio(filepath)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, transcription)
        else:
            messagebox.showwarning("Advertencia", "El archivo seleccionado no existe o no es un archivo válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Transcriptor de Audio")

# Crear y posicionar los elementos de la interfaz gráfica
label = tk.Label(root, text="Transcripción de Audio", font=("Arial", 14))
label.pack(pady=10)

browse_button = tk.Button(root, text="Seleccionar Archivo", command=browse_file)
browse_button.pack(pady=5)

text_box = tk.Text(root, height=10, width=50)
text_box.pack(padx=10, pady=10)

# Ejecutar el bucle de eventos de la ventana
root.mainloop()
