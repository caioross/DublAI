from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/prepare_data', methods=['POST'])
def prepare_data():
    # Carregando arquivos de treinamento
    filenames_pt = []
    filenames_en = []
    for file in os.listdir("dublado"):
        if file.endswith(".mp4"):
            filenames_pt.append(os.path.join("dublado", file))
    for file in os.listdir("original"):
        if file.endswith(".mp4"):
            filenames_en.append(os.path.join("original", file))

    # Tokenizando os arquivos de treinamento
    samples_pt = []
    samples_en = []
    for file in filenames_pt:
        audio, sr = librosa.load(file)
        samples_pt.append(audio)
    for file in filenames_en:
        audio, sr = librosa.load(file)
        samples_en.append(audio)

    # Dividindo os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(samples_pt, samples_en, test_size=0.2, random_state=42)

    # Salvando os dados preparados
    np.save("X_train.npy", X_train)
    np.save("X_test.npy", X_test)
    np.save("y_train.npy", y_train)
    np.save("y_test.npy", y_test)
    return jsonify({"message": "Dados preparados com sucesso!"})

@app.route('/train_model', methods=['POST'])
def train_model():
    # Carregando os dados de treinamento
    X_train = np.load("X_train.npy")
    y_train = np.load("y_train.npy")

    # Construindo e treinando o modelo
    model = Sequential()
    # Adicionando camadas aqui ...
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=50)
