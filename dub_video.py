import librosa
import numpy as np
from sklearn.model_selection import train_test_split
import os
import re

# Carregando o modelo treinado
model = load_model("dub_model.h5")

# Carregando o vídeo a ser dublado
video, sr = librosa.load("path/to/video.mp4")

# Pre-processamento dos dados
video = np.expand_dims(video, axis=0)

# Gerando a dublagem
dubbed_audio = model.predict(video)

# Salvando a dublagem gerada
librosa.output.write_wav("dubbed_video.wav", dubbed_audio[0], sr)

# Sincronizando a dublagem com o vídeo
import moviepy.editor as mp

video = mp.VideoFileClip("path/to/video.mp4")
audio = mp.AudioFileClip("dubbed_video.wav")

video = video.set_audio(audio)
video.write_videofile("dubbed_video.mp4")
