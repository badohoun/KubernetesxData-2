import pickle

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

MAX_LEN = 150  # Nombre de mots maximal par SMS

tokenizer = None
model = load_model("artifacts/model")

# Attention : pour que cela fonctionne, il faut Python 3.8.0 !
with open("artifacts/tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)

def predict(X):
    if model:
        seq_x = tokenizer.texts_to_sequences(X)
        seq_matrix_x = pad_sequences(seq_x, maxlen=MAX_LEN, padding="post")
        return [float(x[0]) for x in model.predict(seq_matrix_x)]  # x[0] = probabilité classe positive
    return None