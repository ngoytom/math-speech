import speech_recognition
import pyttsx3
import random
from pygame import mixer
from playsound import playsound
from mathQuestions import math_questions

question, answer = random.choice(list(math_questions.items()))

print(question[:-4])
print(answer)

mixer.init()
recognizer = speech_recognition.Recognizer()
mixer.music.load(f'sounds/{question}')
mixer.music.queue('sounds/countdown.mp3')
mixer.music.play(loops = 0)
    
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic, timeout=10)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Predicted Text: {text}")
            split_text = text.split(" ")
            print(split_text)

            if answer in split_text:
                mixer.music.stop()
                mixer.music.load('sounds/rightanswer.mp3')
                mixer.music.play()
                #Add Arduino Code
            else:
                mixer.music.stop()
                mixer.music.load('sounds/wronganswer.mp3')
                mixer.music.play()
                #Add Arduino Code
                    
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
    except speech_recognition.WaitTimeoutError:
        print("Timeout Error")
        mixer.music.stop()
        mixer.music.load('sounds/wronganswer.mp3')
        mixer.music.play()
