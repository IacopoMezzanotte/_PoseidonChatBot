import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from my_first_acquascape import MyFirstAcquascape
import random
import pickle
import speech_recognition as sr


class notsure(Exception):
    pass


def chat():
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    continueConversation = True
    while continueConversation:
        print("User: ")
        print("do you want to enter in textual mode? y for yes")
        inputs = input()
        if inputs == 'y':
            print("textual mode")
            inp = input()
        else:
            guess = assistent.hear()
            inp = guess["transcription"]
        #try:
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                                                          truncating='post', maxlen=max_len))
        print(np.max(result))
        if np.max(result) < 0.5:
            raise notsure
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        print(tag)
        method = None
        method = getattr(assistent, tag[0])
        print(method)
        continueConversation = method(inp)
        '''
        except notsure:
            assistent.speak(
                "I'm not sure of what you have asked to me. Try with a different formulation of the sentence")
        except:
            assistent.speak("I didn't catch that. What did you say?")
        '''

print("Start messaging with the bot (type quit to stop)!")

if __name__ == '__main__':
    with open("intents.json") as file:
        data = json.load(file)
    PROMPT_LIMIT = 5
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    assistent = MyFirstAcquascape(recognizer, microphone, PROMPT_LIMIT)
    chat()