"""# 4-vazifa: Protected atribut
# Car klassini yarating, unda _mileage protected atribut bo‘lsin.
# Uni tashqaridan o‘qib bo‘lishini ko‘rsating, lekin nima uchun bu noto‘g‘ri amaliyot ekanini tushuntiring.
"""

class Car:
    def __init__(self, mileage):
        self._mileage = mileage


car = Car(135)
print(car._mileage)
