import numpy as np
import speech_recognition as sr
from text_analysis import Analysis
import os
import string
import random
from gtts import gTTS


class MyFirstAcquascape():
    def __init__(self, recognizer, microphone, limit):
        self.tanks_types = ["ryoboku", "iwagumi", "dutch acquarium"]
        self.rocks_types = ["red dragon stone", "grey dragon stone", "seryu stone", "artificial rocks", "african jade",
                           "lava rock", "black quarz", "pagoda"]
        self.plant_types = ["anubias", "hemianthus callitrichoides", "rotala indica", "rotala wallichii",
                            "Ludwigia palustris red", "glossostigma elatinoides", "java moss"]
        self.water_types = ["osmotic water", "salt water", "tap water", "bottled water"]
        self.woods_types = ["mangrovia", "edera", "torba", "dragon skin", "moore wood"]
        self.foods_types = {"flake feed": "red fishes", "food in tablet": "sword fishes", "mosquito larvae": "salmons", "vegetarian food": "brasses",
                            "omnivore tabs": "catfishes", "spirulina's food": "carps", "algaes": "eels",
                            "vegetables": "plaices", "meat": "piranhas", "veggie food": "herrings", "every kind of food": "tunas",
                            "natural food": "trouts"}
        self.shop_list = []
        self.memory_fertilize = []
        self.recognizer = recognizer
        self.microphone = microphone
        self.limit = limit
        self.parser = Analysis()

    def recognize_speech_from_mic(self, recognizer, microphone):
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response

    def hear(self):
        for j in range(self.limit):
            print('Speak!')
            guess = self.recognize_speech_from_mic(self.recognizer, self.microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            # print("I didn't catch that. What did you say?\n")

            # if there was an error, stop the game
            if guess["error"]:
                # print("ERROR: {}".format(guess["error"]))
                break

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))
        return guess

    def speak(self, sentence):
        language = 'en'
        myobj = gTTS(text=sentence, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg321.exe welcome.mp3")

    def start(self, sentence):
       replies = ["Hi I'am your First Acquascape Assistant, let's start your acquascape together",
                   "hi ask me to begin a new acquascape i'll be happy to help you"]
       sample = random.choice(replies)
       self.speak(sample)
       return True

    def end(self, sentence):
        replies = ["call me if you need me!", "see you next time", "have a good time", "bye bye", "bye",
                   "let me know how it goes"]
        sample = random.choice(replies)
        self.speak(sample)
        return False

    def thanksgiving(self, sentence):
        replies = ["you're welcome", "it's a pleasure", "no worries", "no problem", "don't mention it"]
        sample = random.choice(replies)
        self.speak(sample)
        return True

    def needs(self, sentence):
        self.speak("don't worry i'am here to help you")
        return True

    def new_acquascape(self, sentence):
        replies = ["so just look on the intrnet and choose one, but it has to be in extra light glass",
                   "ok first do a project on a piece of paper and choose the location, then you can make your onw idea about dimensions",
                   "oh wonderfull, now you can put it in its final position and begin to think about hardscape",
                   "mmhh, for the best result you should take inspiration from natural landscapes like crevasses and mountains",
                   "ok so begin to build your hardscape with rocks woods and allophane soil",
                   "i understand, in order to do thath think carefully about your own idea i can suggest you a dark forest landscapes",
                   " so the most beautyfull types of acquascape are ryoboku iwagumi and dutch acquarium, just google them",
                   ]
        sample = random.choice(replies)
        self.speak(sample)
        return True

    def hardscape(self, sentence):

        replies = ["just take your time and look on the internet to take some inspiration",
                   "in order to do a good hard scape you have to choose a good focal point",
                   "for agood hardscape you have to build a good sense of depth",
                   "for a wonderfull effect i suggest you to use fine white quarz",
                   "for a amazing fertilaztion e a good effect you have to use allophane soil",
                   "to build an original and stunning hardscape use little rocks and pieces of wood",
                   "the key for a good hardscape patience and sereniti",
                   "a good hardscape is difficult to make and stressfull but keep calm and contiunue piece after piece",
                   ]
        sample = random.choice(replies)
        self.speak(sample)
        return True

    def water(self, sentence):

        replies = ["the better choice for water is the osmotic water",
                   "it's better not use tap water", "osmotic water is almost allways the best choice",
                   "the first choice should be osmotic water, in case you could add some minerals",
                   "try to use all osmotic water, but you can use also a little of natural light bottled water",
                   "the quality of the water is very important, so use neutral osmotic water no tap water",
                   "osmotic water with the addiction of minerals is the best choice, light bottled water is acceptable"
                   ]
        sample = random.choice(replies)
        self.speak(sample)
        return True

    def water_change(self, sentence):

        replies = ["you allways have to change thirty percent of acquarium's water once per month",
                   "it's better to change the old waters tanks with new osmotic ones every thirty days",
                   "you should change like a one third of the water every month",
                   "you can use all osmotic water during the monthly change, in case you can add some specific minerals"
                   "it is better to use fresh osmotic water at a similar temperature respect to tank water and do regular changes",
                   "you can change water of the tank simply removing the thirty percent of tank water e adding the new osmotic one",
                   "you have to change one third of the water every month to keep the acquarium sane",
                   ]
        sample = random.choice(replies)
        self.speak(sample)
        return True

    def rocks(self, sentence):
        sample = random.choice(self.rocks_types)
        replie = "you could opt for " + sample
        self.speak(replie)
        return True

    def woods(self, sentence):
        sample = random.choice(self.woods_types)
        replie = "you could go for " + sample
        print(sample)
        self.speak(replie)
        return True

    def plants(self, sentence):
        sample = random.choice(self.plants_types)
        replie = "you could choose " + sample
        print(sample)
        self.speak(replie)
        return True

    def tank_types(self, sentence):
        sample = random.choice(self.tanks_types)
        replie = "you could pick " + sample
        print(sample)
        self.speak(replie)
        return False

    # food is object complement
    def find_complement(self, block):
        obj_compl = None
        try:
            obj_compl = block['dobj'] if 'dobj' in block.keys() else block['attr']
        except:
            try:
                obj_compl = block['pobj'] if 'pobj' in block.keys() else block['attr']
            except:
                return None
        return obj_compl

    def fish_food(self, sentence):
        block = self.parser.noun_chunks(sentence)
        print(block)
        obj_compl = self.find_complement(block)
        attempt = None
        while obj_compl is None:
            while guess is None:
                self.speak("I've not understood. Please repeat.")
                attempt = self.hear()
                attempt = attempt["transcription"]
            obj_compl = self.find_complement(self.parser.noun_chunks(attempt))

        obj_compl = obj_compl.lower()
        here = False
        for string in self.foods_types:
            if obj_compl in string or string in obj_compl:
                obj_compl = string
                here = True
        if here:
            self.speak("Yes, you can feed with " + obj_compl + " " + self.foods_types[obj_compl])
        else:
            self.speak("No, you can't!. It will harm fish's health, if you are not sure it's bettere to search on "
                       "the internet")
        return True

    def add_to_list(self, sentence):
        block = self.parser.noun_chunks(sentence)
        print(block)
        obj_compl = self.find_complement(block)
        attempt = None
        while obj_compl is None:
            while attempt is None:
                self.speak("I've not understood. Please repeat.")
                attempt = self.hear()
                attempt = attempt["transcription"]
            obj_compl = self.find_complement(self.parser.noun_chunks(attempt))
        obj_compl = obj_compl.lower()
        self.shop_list.append(obj_compl)
        self.speak("I added " + obj_compl + " to the shopping list")

        return True

    def tell_the_list(self, sentence):
        delimitator = " "
        list = delimitator.join(self.shop_list)
        self.speak("your shopping list is " + list)
        self.shop_list = []

        return True


    def find_date(self, block):
        cardinal = None
        try:
            cardinal = block['DATE'][0]
        except:
            return None
        return cardinal

    def fertilize(self, sentence):
        block = self.parser.entities(sentence)
        print(block)
        dates = self.find_date(block)
        attempt = None
        while dates is None:
            while attempt is None:
                self.speak("I've not understood. Please repeat.")
                attempt = self.hear()
                attempt = attempt["transcription"]
            dates = self.find_complement(self.parser.entities(attempt))
        self.memory_fertilize.append(dates)
        self.speak("I've added to fertilize your plants in " + dates)

        return True

    def memo_fertilize(self, sentence):
        self.speak("You have to fertilize your acquarium in ")
        for element in self.memory_fertilize:
            self.speak(element)
        self.memory_fertilize = []

        return True







