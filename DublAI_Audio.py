import speech_recognition as sr
import librosa
import numpy as np
from sklearn.externals import joblib

# Carregando o modelo treinado
model = joblib.load("trained_model.pkl")

# Inicializando o reconhecedor de voz
r = sr.Recognizer()

# Capturando o áudio do microfone
with sr.Microphone() as source:
    print("Diga algo para ser traduzido e dublado:")
    audio = r.listen(source)

# Reconhecendo o texto da fala
text = r.recognize_google(audio)

# Tokenizando o áudio capturado do microfone
audio, sr = librosa.load(audio)
audio = audio.reshape(1, -1)

# Realizando a previsão com o modelo treinado
predicted_audio = model.predict(audio)

# Salvando o áudio dublado
librosa.output.write_wav("dubbed_audio.wav", predicted_audio, sr)

print("Áudio dublado salvo com sucesso!")
