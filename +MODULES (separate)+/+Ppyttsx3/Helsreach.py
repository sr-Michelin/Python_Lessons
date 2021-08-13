import pyttsx3


def read_text(name):
    with open(name, 'r', encoding='windows-1251') as file:
        text = file.read()
        return text


engine = pyttsx3.init()
voice = engine.getProperty('voices')[0]
engine.setProperty('rate', 160)
print(voice.name)

engine.setProperty('voice', voice.id)

# engine.say(read_text(name='data/Dembski-Bowden Aaron. Helsreach - royallib.ru.txt'))
engine.say(read_text(name='data/Dembski-Bouden_Helsrich_RuLit_Net.txt'))

engine.runAndWait()
engine.stop()
