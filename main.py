#!/usr/bin/env python3

import speech_recognition as sr
import random
import pyttsx3


def say_and_print(*args):
    for arg in args:
        engine.say(arg)
    engine.runAndWait()


def rand_and_say():
    # random operation
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    res = num1 + num2

    say_and_print(num1, "pluss", num2)

    return num1, num2, res


engine = pyttsx3.init()
voice = engine.getProperty('voices')[34]  # the french voice
engine.setProperty('voice', voice.id)

num1, num2, res = rand_and_say()

# get audio from the microphone

r = sr.Recognizer()
with sr.Microphone() as source:
    while 1:
        print("Speak:")
        audio = r.listen(source)

        try:
            answer = r.recognize_google(audio, language='fr-FR')
            print("You said {}, correct answer {}".format(answer, res))
            if answer.strip() == str(res):
                say_and_print("Bravo")

                num1, num2, res = rand_and_say()

            else:
                say_and_print("incorrect")
        except:
            print("Error")
            continue
