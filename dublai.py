from flask import Flask, request, jsonify
import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense
import moviepy.editor as mp

app = Flask(__name__)

@app.route('/prepare_data', methods=['POST'])
def prepare_data():
    filenames_pt = []
    filenames_en = []
    for file in os.listdir("dublado"):
        if file.endswith(".mp4"):
            filenames_pt.append(os.path.join("dublado", file))
    for file in os.listdir("original"):
        if file.endswith(".mp4"):
            filenames_en.append(os.path.join("original", file))
    samples_pt = []
    samples_en = []
    for file in filenames_pt:
        audio, sr = librosa.load(file)
        samples_pt.append(audio)
    for file in filenames_en:
        audio, sr = librosa.load(file)
        samples_en.append(audio)
    X_train, X_test, y_train, y_test = train_test_split(samples_pt, samples_en, test_size=0.2, random_state=42)
    np.save("X_train.npy", X_train)
    np.save("X_test.npy", X_test)
    np.save("y_train.npy", y_train)
    np.save("y_test.npy", y_test)
    return jsonify({"message": "Dados preparados com sucesso!"})

@app.route('/train_model', methods=['POST'])
def train_model():
    X_train = np.load("X_train.npy")
    y_train = np.load("y_train.npy")
    model = Sequential()
    model.add(LSTM(256, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dense(y_train.shape[1]))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=50)
    model.save("dub_model.h5")
    return jsonify({"message": "Modelo treinado e salvo com sucesso!"})

@app.route('/dub_video', methods=['POST'])
def dub_video():
    
video, sr = librosa.load("path/to/video.mp4")
video = np.expand_dims(video, axis=0)
dubbed_audio = model.predict(video)
librosa.output.write_wav("dubbed_video.wav", dubbed_audio[0], sr)


video = mp.VideoFileClip("path/to/video.mp4")
audio = mp.AudioFileClip("dubbed_video.wav")
video = video.set_audio(audio)
video.write_videofile("dubbed_video.mp4")
return jsonify({"message": "Vídeo dublado com sucesso!"})

if name == 'main':
app.run(debug=True)
