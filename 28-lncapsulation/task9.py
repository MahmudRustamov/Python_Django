"""9-vazifa: Vorislik va protected metod
# Animal klassini yarating va unda _speak() protected metodi bo‘lsin.
# Dog klassi Animal dan voris bo‘lsin va _speak() metodini ichida chaqirsin.
# Tashqaridan ham chaqirib bo‘lishini ko‘rsating."""


class Animal:
    def __init__(self, sound):
        self.sound = sound

    def _speak(self):
        pass

class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound=sound)

