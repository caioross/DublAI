import librosa
import numpy as np
from sklearn.model_selection import train_test_split
import os

# Lista de caminhos dos arquivos de treinamento
filenames_original = []
filenames_dublado = []

# Carregando arquivos de treinamento
for file in os.listdir("original"):
    if file.endswith(".mp4"):
        filenames_original.append(os.path.join("original", file))

for file in os.listdir("dublado"):
    if file.endswith(".mp4"):
        filenames_dublado.append(os.path.join("dublado", file))

# Tokenizando os arquivos de treinamento
samples_original = []
samples_dublado = []

for file in filenames_original:
    audio, sr = librosa.load(file)
    samples_original.append(audio)

for file in filenames_dublado:
    audio, sr = librosa.load(file)
    samples_dublado.append(audio)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(samples_original, samples_dublado, test_size=0.2, random_state=42)

# Salvando os dados preparados
np.save("X_train.npy", X_train)
np.save("X_test.npy", X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)
