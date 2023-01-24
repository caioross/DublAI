import numpy as np
from sklearn.metrics import accuracy_score
from keras.layers import LSTM, Dense, TimeDistributed, InputLayer
from keras.models import Sequential
from keras.optimizers import Adam

# Carregando os dados de treinamento
X_train = np.load("X_train.npy")
X_test = np.load("X_test.npy")
y_train = np.load("y_train.npy")
y_test = np.load("y_test.npy")

# Construindo o modelo
model = Sequential()
model.add(InputLayer(input_shape=(None, X_train.shape[-1])))
model.add(LSTM(128, return_sequences=True))
model.add(TimeDistributed(Dense(y_train.shape[-1], activation="softmax")))

# Compilando o modelo
model.compile(loss="categorical_crossentropy", optimizer=Adam(0.001), metrics=["accuracy"])

# Treinando o modelo
model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))

# Avaliando o modelo
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=-1)
y_test = np.argmax(y_test, axis=-1)
acc = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(acc * 100))
