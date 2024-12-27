from flask import Flask, render_template, request
import random
import json
from keras.models import load_model
from keras.layers import LSTM
from keras.initializers import Orthogonal
import numpy as np
import pickle
from nltk.stem import WordNetLemmatizer
import nltk

# Download NLTK data
# nltk.download('popular')
lemmatizer = WordNetLemmatizer()

# Custom LSTM class to handle the 'time_major' argument
class CustomLSTM(LSTM):
    def __init__(self, *args, **kwargs):
        if 'time_major' in kwargs:
            kwargs.pop('time_major')
        super().__init__(*args, **kwargs)

# Add the custom LSTM to the custom objects
custom_objects = {'Orthogonal': Orthogonal, 'LSTM': CustomLSTM}

# Load the model with the custom objects
model = load_model('model_lstm.h5', custom_objects=custom_objects)

# Load intents and other required files
intents = json.loads(open('data.json').read())
words = pickle.load(open('texts.pkl', 'rb'))
classes = pickle.load(open('labels.pkl', 'rb'))

def clean_up_sentence(sentence):
    # pola tokenize - pisahkan kata-kata menjadi array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
# kembalikan kumpulan kata-kata: 0 atau 1 untuk setiap kata dalam kantong yang ada dalam kalimat


def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("bot.html")

# @app.route("/index.html")
# def index():
#     return render_template("index.html")

# @app.route("/tentang.html")
# def tentang():
#     return render_template("tentang.html")

# @app.route("/giji_dan_nutrisi.html")
# def giji_dan_nutrisi():
#     return render_template("giji_dan_nutrisi.html")

# @app.route("/kalkulator.html")
# def kalkulator():
#     return render_template("kalkulator.html")

# @app.route("/map.html")
# def map():
#     return render_template("map.html")

# @app.route("/pola_asuh_anak.html")
# def pola_asuh_anak():
#     return render_template("pola_asuh_anak.html")

# @app.route("/bot.html")
# def bot():
#     return render_template("bot.html")

# @app.route("/edukasi.html")
# def edukasi():
#     return render_template("edukasi.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)



if __name__ == "__main__":
    app.run(debug=True)
