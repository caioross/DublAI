import librosa
import numpy as np
from sklearn.model_selection import train_test_split
import os
import re
import googletrans

# Carregando o modelo treinado
model = load_model("modelo.h5")

# Carregando o vídeo a ser dublado
video, sr = librosa.load("original.mp4")

# Traduzindo o texto
translator = googletrans.Translator()
translated_text = translator.translate(text, dest='pt').text

# Pre-processamento dos dados
video = np.expand_dims(video, axis=0)

# Gerando a dublagem
dubbed_audio = model.predict(video)

# Salvando a dublagem gerada
librosa.output.write_wav("dublado.wav", dubbed_audio[0], sr)

# Sincronizando a dublagem com o vídeo
import moviepy.editor as mp

video = mp.VideoFileClip("original.mp4")
audio = mp.AudioFileClip("dublado.wav")

video = video.set_audio(audio)
video.write_videofile("dublado.mp4")
