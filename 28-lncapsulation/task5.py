"""5-vazifa: Private metod
# Robot klassini yarating va unda __boot_sequence() private metodini yozing.
# Uni tashqaridan chaqirishga harakat qiling (xatolik chiqadi), keyin esa _ClassName__method shaklida chaqirib ko‘ring.
"""


class Robot:
    def __init__(self, name):
        self.name = name


    def __boot_sequence(self):
        print(self.name)


r = Robot("Tesla")

r._Robot__boot_sequence
