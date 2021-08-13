import pyttsx3


def read_text(name):
    with open(name, 'r', encoding='utf-8') as file:
        text = file.read()
        return text


engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('rate', 140)
print(voice.name)

engine.setProperty('voice', voice.id)

engine.say(read_text(name='Dembski-Bowden Aaron. Helsreach - royallib.ru.txt'))
engine.runAndWait()
engine.stop()
