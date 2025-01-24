import whisper

# Cargar el modelo
model = whisper.load_model("base")

# Transcribir el archivo de audio
result = model.transcribe("Reunion1.ogg")

# Imprimir el texto transcrito
print(result["text"])
